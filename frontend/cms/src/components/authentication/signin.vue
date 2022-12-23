<template>
  <v-container align="center" style="width: 100%">
    <v-card title="Sign In" :subtitle="`Type your ${$store.getters.app_short_name} ID and Password`" variant="text" color="white" align="start">
      <v-form ref="form">
        <v-text-field :rules="$store.getters.rule_username" v-model="collection.email" :prepend-icon="email_icon" name="username" label="Username" type="text" align="center">
          <template v-slot:prepend>
            <v-img src="/c_images/album1584/TPIX2.png" width="100%"></v-img>
          </template>
        </v-text-field>
        <v-text-field :rules="[$store.getters.rule_required]" v-model="collection.password" id="password" :prepend-icon="pwd_icon" name="password" label="Password" type="password" align="center">
          <template v-slot:prepend>
            <v-img src="/c_images/archive/room_icon_password.gif" width="100%"></v-img>
          </template>
        </v-text-field>
      </v-form>
      <v-card-actions v-bind:style="{justifyContent: 'start'}">
        <v-btn @click="login()" width="50%" variant="elevated" class="ml-8" v-bind:style="{backgroundColor: '#167CBB', outline: 'auto', outlineStyle: 'groove'}">
          Connect
        </v-btn>
        <v-spacer/>
        <v-btn @click="register()" width="auto" variant="elevated" class="ml-4" v-bind:style="{backgroundColor: '#167CBB', outline: 'auto', outlineStyle: 'groove'}" color="success" icon>
          Register
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>
  
<script lang='ts'>
import { defineComponent } from 'vue'
import { UserActions } from "@/store/user/actions";
import { SystemMutations } from "@/store/system/mutations";

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
// JRL17.png, lol error
export default defineComponent({
  name: 'SignIn',

  data: function () {
    return initialState();
  },

  computed: {
    email_icon () {
      if (this.$store.getters.assets_ran && this.$store.getters.assets_status == 0) {
        return '/c_images/album1584/TPIX2.png'
      }
      return 'mdi-at'
    },
    pwd_icon () {
      if (this.$store.getters.assets_ran && this.$store.getters.assets_status == 0) {
        return '/c_images/archive/room_icon_password.gif'
      }
      return 'mdi-lock'
    }
  },

  methods: {
    async login() {
      const { valid } = await (this.$refs.form as HTMLFormElement).validate();
      if (valid) {
        this.$store.dispatch(UserActions.USER_LOGIN, { username: this.$data.collection.email, password: this.$data.collection.password});
      }
    },
    register() {
      this.$store.commit(SystemMutations.SET_SHOW_REGISTER, true);
    }
  },
})
</script>
  