<template>
  <v-app>
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4 xl3>
            <v-card class="elevation-12">
              <v-toolbar dark color="accent">
                <v-toolbar-title>Register form</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <v-form ref="form">
                  <v-text-field
                    :rules="$store.getters.rules.auth.username"
                    v-model="collection.username"
                    prepend-icon="mdi-account"
                    name="username"
                    label="Username"
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    :rules="$store.getters.rules.auth.email"
                    v-model="collection.email"
                    prepend-icon="mdi-at"
                    name="mail"
                    label="E-Mail"
                    type="text"
                  ></v-text-field>
                  <v-text-field
                    :rules="$store.getters.rules.auth.password"
                    v-model="collection.password"
                    id="password"
                    prepend-icon="mdi-lock"
                    name="password"
                    label="Password"
                    type="password"
                  ></v-text-field>
                  <v-text-field
                    :rules="[
                      // Rules for the password
                      (v) => !!v || `Password is required`,
                      (v) => v == collection.password || `Password must match`,
                      (v) => v.length > 5 || `Min 6 characters`,
												(v) => (v && /\d/.test(v)) || `At least one digit`,  // eslint-disable-line
												(v) => (v && /[A-Z]{1}/.test(v)) || `At least one Capital letter`,  // eslint-disable-line
												(v) => (v && /[^A-Za-z0-9]/.test(v)) || `At least one special character`,  // eslint-disable-line
                      (v) => v.length < 37 || `Max 36 characters`,
                    ]"
                    v-model="collection.verify"
                    id="password"
                    prepend-icon="mdi-autorenew"
                    name="password"
                    label="Verify Password"
                    type="password"
                  ></v-text-field>
                </v-form>
              </v-card-text>
              <v-card-actions>
                <v-btn color="secondary" @click="$emit('login')">Back</v-btn>
                <v-spacer></v-spacer>
                <v-btn color="accent" @click="register()">Register</v-btn>
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
      username: "", // The username of the account
      email: "", // Holds the email of the account
      password: "", // The password of the account
      verify: "", // The verified password of the account
    },
  };
}

import axios from "axios";

export default {
  name: "RegisterView",

  data: function () {
    return initialState();
  },

  methods: {
    register() {
      if (this.$refs.form.validate()) {
        axios
          .post("/api/v1/users", {
            username: this.$data.collection.username,
            mail: this.$data.collection.email,
            password: this.$data.collection.password,
          })
          .then((response) => {
            if (response.status == 200) {
              this.$emit("success");
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
