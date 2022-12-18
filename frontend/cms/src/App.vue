<template>
  <v-app v-bind:style="{ backgroundImage: 'url(' + require('@/assets/wallpapertip_habbo-wallpaper_202535.png') + ')', backgroundSize: 'cover', backgroundPosition: 'center center' }">
    <AppBar/>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import AppBar from "@/components/appbar/index.vue";

export default defineComponent({
  name: 'App',

  components: {
    AppBar
  },
})
</script>