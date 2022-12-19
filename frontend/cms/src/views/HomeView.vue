<template>
  <v-container class="bg-surface-variant" fill-height>
    <v-row no-gutters>

      <v-col :cols="cols[0]" v-if="cols[0] !=0 ">
        <v-sheet class="pa-2 ma-2">
          .v-col-{{ cols[0] }}
        </v-sheet>
      </v-col>

      <v-col :cols="cols[1]" v-if="cols[1] != 0">
        <v-sheet class="pa-2 ma-2">
          .v-col-{{ cols[1] }}
        </v-sheet>
      </v-col>

      <v-col :cols="cols[2]">
        <v-sheet class="pa-2 ma-2">
          .v-col-{{ cols[2] }}
          <Signin/>
          <registerVue/>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Signin from '../components/authentication/signin.vue';
import registerVue from '@/components/authentication/register.vue';

// Components
import HelloWorld from '../components/HelloWorld.vue';

export default defineComponent({
  name: 'HomeView',

  components: {
    Signin,
    registerVue
  },

  computed: {
    cols () {
      const { xs, sm, md, lgAndUp  } = this.$vuetify.display;
      var res;
      if( xs ) {
        res = [0, 0, 12];
      }
      else if(sm) 
      {  // Small screens
        res = [0, 7, 5];
      }
      else if (md)
      {  // Normal size
        res = [3, 5, 4];
      }
      else if (lgAndUp)
      {  // Large and up
        res = [3, 6, 3];
      }
      return res;
    },
  }
});

    Signin</script>
