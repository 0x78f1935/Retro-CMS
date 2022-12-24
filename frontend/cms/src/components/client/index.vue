<template>
  <NitroClient v-if="canPlay" />
  <v-container v-else>
    <v-row dense v-if="$store.getters.scope.includes('retro:admin') || $store.getters.scope.includes('retro:owner')">
      <v-card class="mx-auto">
        <v-img :src="require('@/assets/construction.png')" class="white--text align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" height="200px">
          <v-card-title>Configure CMS</v-card-title>
        </v-img>

        <v-card-text v-bind:style="{ textAlign: 'center' }">
          <span class="red white--text align-center">
            The client couldn't load because the retro is missing required assets or might not be
            configured yet!
          </span>
        </v-card-text>

        <v-card-text max-width="600">
          <ConfiguratorIndex />
        </v-card-text>
      </v-card>
    </v-row>
    <v-row dense v-else>
      <MaintenanceView/>
    </v-row>
  </v-container>
</template>
  
<script>
import NitroClient from "@/components/client/client.vue";
import ConfiguratorIndex from "@/components/client/configurator/index.vue";
import MaintenanceView from "@/components/MaintenanceView";

function initialState() {
  return {
    //
  };
}

export default {
  name: "ClientView",

  data: function () {
    return initialState();
  },

  components: {
    NitroClient,
    MaintenanceView,
    ConfiguratorIndex,
  },

  computed: {
    canPlay() {
      if (this.$store.getters.assets_ran && this.$store.getters.converter_ran) {
        return true;
      }
      return false
    }
  }
};
</script>