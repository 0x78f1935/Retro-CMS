<template>
  <v-timeline align="start">
    <v-timeline-item v-for="(task, i) in tasks" :key="i" :dot-color="card[i].color" :icon="card[i].icon" fill-dot>
      <v-card :loading="task.running">
        <v-card-title :class="['text-h6', `bg-${card[i].color}`]">
          {{ task.name }}
        </v-card-title>
        <v-card-text class="bg-white text--primary">
          <p>{{ task.description }}</p>
        </v-card-text>
        <v-card-actions>          
          <v-btn :color="card[i].color" variant="outlined" :disabled="task.running">
            Start {{ task.sysname }}
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
      },
      {
        color: 'purple-lighten-2',
        icon: 'mdi-book-variant',
      },
      {
        color: 'green-lighten-1',
        icon: 'mdi-airballoon',
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
    }

  },
};
</script>