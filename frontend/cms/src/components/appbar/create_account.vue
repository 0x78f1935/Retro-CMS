<template>
  <v-dialog v-model="showRegister" persistent origin="center center"
    >
    <v-row>
      <v-col v-bind:style="{ textAlign: '-webkit-center'}">

        <v-card min-height="550" max-width="550" v-bind:style="{ backgroundImage: 'url(\'' + '/c_images/archive/h03.gif' + '\')', backgroundPosition: 'center center' }" class="d-flex flex-column">
          <v-card-title class="ml-5 pt-0">Register</v-card-title>
          <v-spacer></v-spacer>
          <v-card-text class="ml-5 pt-0">
            <v-form ref="form">
              <v-text-field
                :rules="$store.getters.rule_username"
                v-model="collection.username"
                prepend-icon="mdi-account"
                name="username"
                label="Username"
                type="text"
              ></v-text-field>
              <v-text-field
                :rules="$store.getters.rule_email"
                v-model="collection.email"
                prepend-icon="mdi-at"
                name="email"
                label="E-Mail"
                type="text"
              ></v-text-field>
              <v-text-field
                :rules="$store.getters.rule_password"
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
          <v-card-actions class="mb-5">
            <v-spacer></v-spacer>
            <v-btn color="red" variant="elevated" @click="close_dialog">
              Close
            </v-btn>
            <v-btn color="green-darken-1" variant="elevated" @click="submit_dialog">
              Join
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-dialog>

</template>
    
<script lang='ts'>
import { SystemMutations } from '@/store/system/mutations';
import { defineComponent } from 'vue'

function initialState() {
  return {
    dialog: false,  // Indicator if dialog is open
    collection: {
      // Contains data collected through out the wizard
      username: "", // The username of the account
      email: "", // Holds the email of the account
      password: "", // The password of the account
      verify: "", // The verified password of the account
    },
  };
}

export default defineComponent({
  name: 'CreateAccount',

  data: function () {
    return initialState();
  },

  methods: {
    close_dialog() {
      this.$store.commit(SystemMutations.SET_SHOW_REGISTER, false);
    },
    submit_dialog() {
      this.close_dialog();
    }
  },

  computed: {
    showRegister: {
      // getter
      get() {
        return this.$store.getters.showRegister;
      },
      // setter
      set(newValue) {
        // Note: we are using destructuring assignment syntax here.
        this.$store.commit(SystemMutations.SET_SHOW_REGISTER, newValue);
      }
    }
  },
})
</script>
    