<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('@/assets/construction.png')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">Welcome to Retro CMS</h1>

        <p class="subheading font-weight-regular">
          For help and collaboration with other Retro developers,
          <br />please join our online
          <a href="https://github.com/0x78f1935/Retro-CMS" target="_blank"
            >GitHub Community</a
          >
        </p>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">What's next?</h2>

        <v-row justify="center">
          <a
            href="https://github.com/users/0x78f1935/projects/1"
            class="subheading mx-3"
            target="_blank"
          >
            Road Map CMS
          </a>
        </v-row>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">Important Links</h2>

        <v-row justify="center">
          <a
            href="https://arcturus.dev/"
            class="subheading mx-3"
            target="_blank"
          >
            Arcturus Emulator
          </a>
        </v-row>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">Enter Hotel</h2>

        <v-row justify="center">
          Welcome, {{ $store.getters.account.email }}!
        </v-row>

        <v-row justify="center" v-if="$store.getters.sso_ticket">
          <v-btn
            color="primary"
            :href="$store.getters.sso_ticket"
            class="subheading mx-3"
            target="_blank"
          >
            Check In
          </v-btn>
        </v-row>
        <v-row justify="center" v-else>
          <v-progress-circular
            indeterminate
            color="accent"
          ></v-progress-circular>
        </v-row>

        <v-row class="red darken-2 text-center" v-if="message">
          <span class="white--text"
            ><strong>{{ message }}</strong></span
          >
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
function initialState() {
  return {
    message: "", // Holds response message if having one
  };
}

import axios from "axios";

export default {
  name: "RetroView",

  data: function () {
    return initialState();
  },

  created() {
    this.ticket();
  },

  methods: {
    ticket() {
      axios
        .get("/api/v1/users/sso")
        .then((response) => {
          if (response.status == 200) {
            this.$store.commit("setSSOTicket", response.data["auth_ticket"]);
            return;
          }
          console.error(response.data);
          this.$data.message = "Something went wrong, Try again!";
        })
        .catch((e) => {
          if (e.response.data["message"]) {
            console.error(e.response.data.message);
            this.$data.message = e.response.data.message;
          }
        });
    },
  },
};
</script>
