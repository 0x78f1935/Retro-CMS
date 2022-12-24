<template>
  <v-container>
    <v-row justify="space-around">
      <v-card class="mx-auto">
        <v-img :src="require('@/assets/construction.png')" class="white--text align-end"
          gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)" height="200px">
          <v-card-title>Maintenance</v-card-title>
        </v-img>
        <v-card-text v-bind:style="{ textAlign: 'center' }">
          <span class="align-center">
            This retro is under Maintenance, try again in a few minutes, If this is a requiring problem,
            Please contact the System administrator.
          </span>
        </v-card-text>
        <PromotionFooter />
      </v-card>
    </v-row>
  </v-container>
</template>
<script>
import PromotionFooter from "@/components/client/promotion";

export default {
  name: "MaintenanceView",

  components: {
    PromotionFooter
  }
}
</script>