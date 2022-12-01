<template>
  <RetroView v-if="$store.getters.access_token" />
  <AuthenticateView
    v-else-if="$data.show_login"
    @register="show_login = false"
  />
  <RegisterView
    v-else-if="!$data.show_login"
    @login="show_login = true"
    @success="show_login = true"
  />
</template>

<script>
import AuthenticateView from "@/components/landingpage/AuthenticateView.vue";
import RegisterView from "@/components/landingpage/RegisterView.vue";
import RetroView from "@/components/landingpage/RetroView.vue";

function initialState() {
  return {
    show_login: true, // Indicator if login menu is shown, By default, user will see this page when not authenticated
  };
}

export default {
  name: "HomePage",

  components: {
    AuthenticateView,
    RegisterView,
    RetroView,
  },

  data: function () {
    return initialState();
  },
};
</script>
