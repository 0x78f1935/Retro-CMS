import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  access_token: null,
  sso_ticket: null,
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
  sso_ticket: (state) => state.sso_ticket,
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
    state.sso_ticket = null;
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
  setSSOTicket(state, value) {
    state.sso_ticket = value;
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
