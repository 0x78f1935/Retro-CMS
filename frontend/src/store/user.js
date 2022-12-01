import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  access_token: null,
  account: {
    email: "",
    username: "",
  },
  profile: {
    darkmode: false,
  },
  scopes: [],
};

const getters = {
  access_token: (state) => state.access_token,
  account: (state) => state.account,
  profile: (state) => state.profile,
  scopes: (state) => state.scopes,
  authenticated: (state) =>
    state.access_token != null || state.account.username != "" ? true : false,
};

const actions = {
  clearState({ commit }) {
    commit("resetUserState");
  },
};

const mutations = {
  resetUserState(state) {
    state.access_token = null;
    state.account = {
      email: "",
      username: "",
    };
    state.profile = {
      darkmode: false,
    };
    state.scopes = [];
  },
  setAccessToken(state, value) {
    state.access_token = value;
  },
  setEmail(state, value) {
    state.account.email = value;
  },
  setUsername(state, value) {
    state.account.username = value;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
