import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  rules: {
    generic: {
      required: (value) => !!value || "Field is required.",
    },

    auth: {
      username: [
        // Rules for the username
        (v) => !!v || "Username is required",
        (v) => v.length < 17 || "Max 16 characters",
        (v) => v.length > 4 || "Min 5 characters",
        (v) => /^([A-Za-z0-9\_]+)$/.test(v) || "Only: aBc_0123",  // eslint-disable-line
      ],
      email: [
        (v) => !!v || "E-mail address is required",
        (v) =>
          /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
          "Must be a valid e-mail address",
      ],
      password: [
        // Rules for the password
        (v) => !!v || "Password is required",
        (v) => v.length > 5 || "Min 6 characters",
        (v) => (v && /\d/.test(v)) || "At least one digit",  // eslint-disable-line
        (v) => (v && /[A-Z]{1}/.test(v)) || "At least one Capital letter",  // eslint-disable-line
        (v) => (v && /[^A-Za-z0-9]/.test(v)) || "At least one special character",  // eslint-disable-line
        (v) => v.length < 37 || "Max 36 characters",
      ],
    },
  },
};

const getters = {
  rules: (state) => state.rules,
};

export default {
  state,
  getters,
};
