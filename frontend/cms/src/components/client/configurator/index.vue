<template>
  <v-timeline align="top" :dense="$vuetify.display.smAndDown">
    <v-timeline-item v-for="(task, i) in tasks" :key="i" :dot-color="card[i].color" :icon="card[i].icon" fill-dot>

      <template v-slot:icon>
        <v-btn v-if="task.running" icon loading disabled :color="card[i].loadColor" />
        <v-icon v-else-if="task.exit_code == 404">mdi-tray-arrow-down</v-icon>
        <v-icon v-else-if="task.exit_code != 0" color="red">mdi-restart-alert</v-icon>
        <v-icon v-else color="green">mdi-check-outline</v-icon>
      </template>

      <template v-slot:opposite>
        <span v-if="task.running">Running ...</span>
        <span v-else-if="task.exit_code == 404">Idle</span>
        <span v-else-if="task.exit_code != 0">Error ..</span>
        <span v-else>Initialized</span>
      </template>

      <v-card :loading="task.running">

        <template v-slot:loader="{ isActive }">
          <v-progress-linear :active="isActive" :color="card[i].loadColor" height="4" indeterminate />
        </template>

        <v-card-title :class="['text-h6', `bg-${card[i].color}`]">
          {{ task.name }}
        </v-card-title>
        <v-card-text class="bg-white text--primary">
          <p>{{ task.description }}</p>
        </v-card-text>

        <v-card-actions>
          <v-container v-if="task.running"></v-container>
          <v-btn v-else-if="task.exit_code == 404" text :color="card[i].color" @click="execute(task.id);"
            :disabled="canExecute(task)">
            <v-icon color="primary">mdi-tray-arrow-down</v-icon>
            Start {{ task.sysname }}!
          </v-btn>
          <v-btn v-else-if="task.exit_code != 0" text color="red" @click="execute(task.id);"
            :disabled="canExecute(task)">
            <v-icon color="red">mdi-restart-alert</v-icon>
            Retry {{ task.sysname }}!
          </v-btn>
          <v-btn v-else text color="green" @click="execute(task.id);" :disabled="canExecute(task)">
            <v-icon color="green">mdi-check-outline</v-icon>
            Rerun {{ task.sysname }}!
          </v-btn>
        </v-card-actions>

      </v-card>
    </v-timeline-item>
  </v-timeline>
</template>
      
<script>
import { TaskActions } from '@/store/tasks/actions';

function initialState() {
  return {
    card: [
      {
        color: 'red-lighten-2',
        icon: 'mdi-star',
        loadColor: 'red-darken-2'
      },
      {
        color: 'purple-lighten-2',
        icon: 'mdi-book-variant',
        loadColor: 'purple-darken-2'
      },
      {
        color: 'green-lighten-1',
        icon: 'mdi-airballoon',
        loadColor: 'green-darken-1'
      },
      {
        color: 'indigo-lighten-2',
        icon: 'mdi-buffer',
        loadColor: 'indigo-darken-2'
      },
    ],
  };
}

export default {
  name: "ConfiguratorIndex",

  data: function () {
    return initialState();
  },

  mounted() {
    this.status()
  },

  beforeUnmount() {
    clearInterval(this.polling)
  },

  created() {
    this.pollData();
  },

  computed: {
    tasks() {
      return this.$store.getters.tasks;
    }
  },

  methods: {
    pollData() {
      this.polling = setInterval(() => {
        this.status();
      }, 1000)
    },
    status() {
      this.$store.dispatch(TaskActions.POLL);
    },
    execute(task_id) {
      this.$store.dispatch(TaskActions.EXECUTE, task_id);
    },
    canExecute(task) {
      if (!task.running) {
        if (task.sysname === 'downloader') {
          // Enable downloader always, can't hurt to download additional assets
          return false;
        }
        else if (task.sysname === 'converter') {
          const required_task = this.$store.getters.tasks[0];
          if (required_task.has_ran && required_task.sysname == 'downloader' && required_task.exit_code === 0) {
            return false;
          }
        }
        else if (task.sysname === 'emulator') {
          const required_task = this.$store.getters.tasks[1];
          if (required_task.has_ran && required_task.sysname == 'converter' && required_task.exit_code === 0) {
            return false;
          }
        }
      }
      return true; // Disables button when True
    }
  },
};
</script>