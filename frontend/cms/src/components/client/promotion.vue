<template>
  <v-container>
    <v-row dense>
      <v-col v-for="card in cards" :key="card.title" :cols="card.flex">
        <v-card class="mx-auto" :href="card.href" target="_blank" height="100px">
          <v-img :src="card.src" class="white--text align-end" gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="100px">
            <v-card-title v-text="card.title"></v-card-title>
          </v-img>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
  
<script>
function initialState() {
  return {
    cards: [
      { title: 'undeƒined', src: require('@/assets/github.png'), flex: 6, href: "https://github.com/0x78f1935/Retro-CMS" },
      { title: 'krews', src: require('@/assets/discord.png'), flex: 6, href: "https://discord.gg/BzfFsTp" },
    ],
  };
}

export default {
  name: "PromotionFooter",

  data: function () {
    return initialState();
  },
};
</script>