<template>
  <v-img src="/c_images/archive/jukka_guest2.gif" height="150" v-if="!has_imager"></v-img>
  <v-img :src="render()" height="150" v-else></v-img>
</template>
<script>
export default {
  name: "NitroImager",

  props: {
    figure: {
      type: String,
      default() {
        return 'ha-1003-88.lg-285-89.ch-3032-1334-109.sh-3016-110.hd-180-1359.ca-3225-110-62.wa-3264-62-62.hr-891-1342.0';
      }
    },
    actions: {
      type: String,
      default() {
        // You may render multiple actions with a comma separater

        // Example: ``&action=wlk,wav,drk=1``
        // ##### Posture
        // | key | description |
        // | ------ | ------ |
        // | std | Renders the standing posture |
        // | wlk,mv | Renders the walking posture |
        // | sit | Renders the sitting posture |
        // | lay | Renders the laying posture |
        return 'std';
      }
    },
    gesture: {
      type: String,
      default() {
        // | key | description |
        // | ------ | ------ |
        // | std | Renders the standard gesture |
        // | agr | Renders the aggravated gesture |
        // | sad | Renders the sad gesture |
        // | sml | Renders the smile gesture |
        // | srp | Renders the surprised gesture |
        return 'std';
      }
    },
    direction: {
      type: Number,
      default: 2,  // Number in the range of (0 - 7)
    },
    headDirection: {
      type: Number,
      default: 2,  // Number in the range of (0 - 7)
    },
    headOnly: {
      type: Number,
      default: 0,  // 1 to only render the head, 0 for full body
    },
    expression: {
      type: String,
      default() {
        // | key | description |
        // | ------ | ------ |
        // | wav,wave | Renders the waving expression |
        // | blow | Renders the kissing expression |
        // | laugh | Renders the laughing expression |
        // | respect | Renders the respect expression |
        return '';
      }
    },
    carry: {
      type: String,
      default() {
        // To hold a certain drink, use an equal separator with the hand item id. You can only render one of these options at a time
        // | key | description |
        // | ------ | ------ |
        // | crr,cri | Renders the carry action |
        // | drk,usei | Renders the drink action |
        return '';
      }
    },
    imgFormat: {
      type: String,
      default() {
        // A value of png or gif. Gif will render all frames of the figure
        return 'png';
      }
    },
    size: {
      type: String,
      default() {
        // | key | description |
        // | ------ | ------ |
        // | s | Renders the small size (0.5) |
        // | n | Renders the normal size (1) |
        // | l | Renders the large size (2) |
        return 'l';
      }
    },
    dance: {
      type: Number,
      default: 0,  // A dance id of 0-4 to render, Expression cannot be set when dance has been enabled
    },
    effect: {
      type: Number,
      default: 0,  // An effect id to render
    }
  },

  computed: {
    has_imager() {
      return this.$store.getters.imager_ran;
    },
    random_look() {
      return this.$store.getters.random_look;
    }
  },

  methods: {
    render() {
      const base_link = `http://127.0.0.1:8889/?figure=${this.$props.figure}&action=${this.$props.actions},${this.$props.expression},${this.$props.carry}&gesture=${this.$props.gesture}&direction=${this.$props.direction}&head_direction=${this.$props.headDirection}&headonly=${this.$props.headDirection}&img_format=${this.$props.imgFormat}&size=${this.$props.size}&dance=${this.$props.dance}&effect=${this.$props.effect}`;
      return base_link
    }
  },

}
</script>