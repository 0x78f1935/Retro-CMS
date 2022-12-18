<template>
  <section>
    <signin />
    <registerVue/>
  </section>
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
});

    Signin</script>
