import Vue from "vue";
import Vuex from "vuex";
import user from "./user";
import rules from "./rules";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters: {},
  mutations: {},
  actions: {},
  modules: {
    user,
    rules,
  },
});
