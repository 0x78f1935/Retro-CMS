<template>
  <v-app>
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 xl3>
            <v-card class="elevation-12">
              <v-toolbar dark color="accent">
                <v-toolbar-title>Login form</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form ref="form">
                  <v-text-field
                    :rules="$store.getters.rules.auth.email"
                    v-model="collection.email"
                    prepend-icon="mdi-at"
                    name="mail"
                    label="E-Mail"
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    :rules="[$store.getters.rules.generic.required]"
                    v-model="collection.password"
                    id="password"
                    prepend-icon="mdi-lock"
                    name="password"
                    label="Password"
                    type="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn color="secondary" @click="$emit('register')"
                  >New Guest</v-btn
                >
                <v-spacer></v-spacer>
                <v-btn color="accent" @click="login()">Check In</v-btn>
              </v-card-actions>
              <v-card-text class="red darken-2 text-center" v-if="message">
                <span class="white--text"
                  ><strong>{{ message }}</strong></span
                >
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
function initialState() {
  return {
    message: "", // Holds response message if having one
    collection: {
      // Contains data collected through out the wizard
      email: "", // Holds the email of the account
      password: "", // The password of the account
    },
  };
}

import axios from "axios";

export default {
  name: "AuthenticateView",

  data: function () {
    return initialState();
  },

  methods: {
    login() {
      if (this.$refs.form.validate()) {
        axios
          .post("/api/v1/users/login", {
            mail: this.$data.collection.email,
            password: this.$data.collection.password,
          })
          .then((response) => {
            if (response.status == 200) {
              this.$store.commit("setEmail", this.$data.collection.email);
              this.$store.commit("setAccessToken", response.data.access_token);
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
      }
    },
  },
};
</script>
