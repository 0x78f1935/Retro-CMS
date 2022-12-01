<template>
  <v-app>
    <v-navigation-drawer app v-if="$store.getters.access_token">
      <!-- -->
    </v-navigation-drawer>

    <v-app-bar app v-if="$store.getters.access_token">
      <!-- -->
    </v-app-bar>

    <!-- Sizes your content based upon application components -->
    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app v-if="!$store.getters.access_token">
      <v-col class="text-center" cols="12">
        2022 - {{ new Date().getFullYear() }} —
        <strong
          ><a href="https://github.com/0x78f1935/Retro-CMS" target="_blank"
            >Retro CMS</a
          ></strong
        >
      </v-col>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
