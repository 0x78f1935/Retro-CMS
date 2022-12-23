import { MutationTree } from "vuex";
import { SystemState } from "./interface";

export enum SystemMutations {
    SET_SHOW_REGISTER = "SHOW_REGISTER",
    SET_SHOW_LOADING = "SHOW_LOADING",
}

export const mutations: MutationTree<SystemState> = {
    [ SystemMutations.SET_SHOW_REGISTER ] (state, payload: boolean) {
        state.showRegister = payload;
    },
    [ SystemMutations.SET_SHOW_LOADING ] (state, payload: boolean) {
        state.showLoading = payload;
    },
}
