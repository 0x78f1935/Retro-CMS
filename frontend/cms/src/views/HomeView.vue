<template>
  <v-container style="height: 100%">
    <v-row no-gutters style="height: 100%">
      <v-col :cols="cols[0]" v-if="cols[0] !=0 " style="placeSelf: center">
        <NitroImager :figure="$store.getters.random_look" expression="wave" :dance="2"/>
        <registerVue style="maxWidth: 100%" />
      </v-col>
      <v-col :cols="cols[1]" v-if="cols[1] != 0" style="placeSelf: center">

      </v-col>

      <v-col :cols="cols[2]" style="placeSelf: center">
        <Signin style="maxWidth: 400px" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Signin from '../components/authentication/signin.vue';
import registerVue from '@/components/authentication/register.vue';
import NitroImager from '@/components/Imager.vue';

export default defineComponent({
  name: 'HomeView',

  components: {
    Signin,
    registerVue,
    NitroImager
  },

  computed: {
    cols() {
      const { xs, sm, md, lgAndUp } = this.$vuetify.display;
      var res;
      if (xs) {
        res = [0, 0, 12];
      }
      else if (sm) {  // Small screens
        res = [0, 7, 5];
      }
      else if (md) {  // Normal size
        res = [3, 4, 5];
      }
      else if (lgAndUp) {  // Large and up
        res = [3, 5, 4];
      }
      return res;
    },
  }
});
</script>
