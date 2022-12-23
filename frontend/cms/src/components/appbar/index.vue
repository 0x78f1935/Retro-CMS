<template>
  <v-app-bar app>
    <v-img :src="$store.getters.app_name_logo" max-height="50" max-width="150"></v-img>
    <v-spacer></v-spacer>
    <v-btn>HOME</v-btn>
    <v-btn>COMMUNITY</v-btn>
    <v-btn>SHOP</v-btn>
    <v-btn>ABOUT HABBO</v-btn>
  </v-app-bar>
</template>
    
<script>
import { InfoActions } from "@/store/info/actions";

function initialState() {
  return {

  };
}

export default {
  name: "AppBar",

  data: function () {
    return initialState();
  },

  components: {
    //
  },

  created() {
    this.$store.dispatch(InfoActions.PUBLIC);
  },
};
</script>
  