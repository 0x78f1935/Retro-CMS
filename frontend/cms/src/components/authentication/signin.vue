<template>
    <v-card
      class="mx-auto mt-10"
      max-width="344"
    >
      <v-card-text>
        <p class="text-h4 text--primary">
          Sign In
        </p>
      </v-card-text>

      <v-form ref="form" v-model="valid" lazy-validation>
        <v-text-field
            v-model="name"
            :counter="10"
            :rules="nameRules"
            label="Username"
            required
        ></v-text-field>

        <v-text-field
            v-model="password"
            :rules="emailRules"
            label="Passwprd"
            type="password"
            required
        ></v-text-field>
  </v-form>

      <v-card-actions>
        <v-btn
          variant="text"
          color="deep-purple-accent-4"
        >
          Connect
        </v-btn>
      </v-card-actions>
    </v-card>
  </template>
  
  <script lang='ts'>
  import { defineComponent } from 'vue'
  
  
  export default defineComponent({
    name: 'SignIn',
  })
  </script>
  