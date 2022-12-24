<template>
    <v-timeline align-top :dense="$vuetify.display.smAndDown">
      <v-timeline-item v-for="task in tasks" :key="task.id" large color="transparent">
  
        <template v-slot:icon>
          <v-btn v-if="task.running" icon color="primary" loading disabled></v-btn>
          <v-btn v-else-if="task.exit_code == 404" icon color="grey" @click="execute(task.id); status();">
            <v-icon>mdi-tray-arrow-down</v-icon>
          </v-btn>
          <v-btn v-else-if="task.exit_code != 0" icon color="red" @click="execute(task.id); status();">
            <v-icon>mdi-restart-alert</v-icon>
          </v-btn>
          <v-btn v-else icon color="green" @click="execute(task.id); status();">
            <v-icon>mdi-check-outline</v-icon>
          </v-btn>
        </template>
  
        <template v-slot:opposite>
          <span v-if="task.running">Running ...</span>
          <span v-else-if="task.exit_code == 404">Install {{task.name}}</span>
          <span v-else-if="task.exit_code != 0">Error ..</span>
          <span v-else>Initialized</span>
        </template>
  
        <v-card class="elevation-2" :loading="task.running">
          <v-card-title class="text-h5">
            {{task.name}}
          </v-card-title>
          <v-card-text>
            {{task.description}}
          </v-card-text>
          <v-card-actions>
            <v-containger v-if="task.running"></v-containger>
            <v-btn v-else-if="task.exit_code == 404" text color="grey" @click="execute(task.id); status();">
              <v-icon>mdi-tray-arrow-down</v-icon>
              Start Task!
            </v-btn>
            <v-btn v-else-if="task.exit_code != 0" text color="red" @click="execute(task.id); status();">
              <v-icon>mdi-restart-alert</v-icon>
              Retry Task!
            </v-btn>
            <v-btn v-else text color="green" @click="execute(task.id); status();">
              <v-icon>mdi-check-outline</v-icon>
              Rerun Task!
            </v-btn>
          </v-card-actions>
        </v-card>
  
      </v-timeline-item>
    </v-timeline>
  </template>
      
  <script>
  import axios from "axios";
  
  function initialState() {
    return {
      tasks: [ ]
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
  
    beforeMount () {
      clearInterval(this.polling)
    },
  
    created () {
      this.pollData()
    },
  
    methods: {
      pollData () {
        this.polling = setInterval(() => {
          this.status();
        }, 10000)
      },
      status() {
        axios
          .get("/api/v1/system/tasks",{
            headers: {
              Authorization: `Bearer ${this.$store.getters.access_token}`
            }
          })
          .then((response) => {
            if (response.status == 200) {
              this.$data.tasks = response.data;
              return;
            }
            console.error("Something went wrong, Try again!");
            console.error(response.data);
          })
          .catch((e) => {
            if (e.response.data["message"]) {
              console.error(e.response.data.message);
              this.$data.message = e.response.data.message;
            }
          });
      },
      execute(task_id) {
        axios
          .post("/api/v1/system/tasks", { id: task_id }, {
            headers: {
              Authorization: `Bearer ${this.$store.getters.access_token}`
            },
          })
          .then((response) => {
            if (response.status == 200) {
              console.log(response.data);
              return;
            }
            console.error("Something went wrong, Try again!");
            console.error(response.data);
          })
          .catch((e) => {
            if (e.response.data["message"]) {
              console.error(e.response.data.message);
              this.$data.message = e.response.data.message;
            }
          });
      }
  
    },
  };
  </script>