<template>
  <v-container align="center" style="width: 100%">
    <v-btn text class="mt-4" size="x-large" color="success" style="width: 100%" v-if="$vuetify.display.xs" @click="toggle()">
      Join for free
    </v-btn>
    <v-container v-else>
      <v-img src="/c_images/archive/join_free_anim_uk.gif" width="125" @click="toggle()"/>
    </v-container>
  </v-container>
</template>
  
<script lang='ts'>
import { SystemMutations } from '@/store/system/mutations';
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'SignIn',

  methods: {
    toggle() {
      this.$store.commit(SystemMutations.SET_SHOW_REGISTER, !this.$store.getters.showRegister);
    }
  }
})
</script>
  