<template>
  <ClientView/>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import ClientView from '@/components/client/index.vue';

export default defineComponent({
  name: 'MeView',

  components: {
    ClientView
  },
});
</script>
