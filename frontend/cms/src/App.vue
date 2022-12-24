<template>
  <!-- <v-app v-bind:style="{ backgroundImage: 'url(' + require('@/assets/wallpapertip_habbo-wallpaper_202535.png') + ')', backgroundSize: 'cover', backgroundPosition: 'center center' }"> -->
  <v-app v-bind:style="{ background: 'radial-gradient(#0270e0, #005ab4 )', backgroundSize: 'cover', backgroundPosition: 'center center' }">
    <!-- AppBar -->
    <AppBar/>

    <!-- Main View -->
    <v-main v-bind:style="{zIndex: 10}">
      <router-view/>
    </v-main>

    <!-- Dialogs -->
    <create_accountVue/>

    <!-- Background -->
    <v-container v-bind:style="{backgroundImage: 'url(\'' + '/c_images/reception/background_left_xmas22.png' + '\')', position: 'absolute', minHeight: '100vh', minWidth: '100vw', backgroundPosition: 'bottom left', zIndex: 0}" v-if="$vuetify.display.smAndUp"/>
    <!-- <v-container v-bind:style="{backgroundImage: 'url(\'' + '/c_images/archive/h03.gif' + '\')', position: 'absolute', minHeight: '100vh', minWidth: '100vw', backgroundPosition: 'center center', zIndex: 1}" v-if="$vuetify.display.lgAndUp"/> -->
    <v-container v-bind:style="{backgroundImage: 'url(\'' + '/c_images/reception/xmas15_background_hotel_right.png' + '\')', position: 'absolute', minHeight: '100vh', minWidth: '100vw', backgroundPosition: 'bottom right', zIndex: 2}"/>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import AppBar from "@/components/appbar/index.vue";
import create_accountVue from './components/appbar/create_account.vue';

export default defineComponent({
  name: 'App',

  components: {
    AppBar,
    create_accountVue
  },
})
</script>