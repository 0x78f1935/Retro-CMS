<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('@/assets/construction.png')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">Welcome to Retro CMS</h1>

        <p class="subheading font-weight-regular">
          For help and collaboration with other Retro developers,
          <br />please join our online
          <a href="https://github.com/0x78f1935/Retro-CMS" target="_blank"
            >GitHub Community</a
          >
        </p>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">What's next?</h2>

        <v-row justify="center">
          <a
            href="https://github.com/users/0x78f1935/projects/1"
            class="subheading mx-3"
            target="_blank"
          >
            Road Map CMS
          </a>
        </v-row>
      </v-col>

      <v-col class="mb-5" cols="12">
        <h2 class="headline font-weight-bold mb-3">Important Links</h2>

        <v-row justify="center">
          <a
            href="https://arcturus.dev/"
            class="subheading mx-3"
            target="_blank"
          >
            Arcturus Emulator
          </a>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "RetroView",
};
</script>
