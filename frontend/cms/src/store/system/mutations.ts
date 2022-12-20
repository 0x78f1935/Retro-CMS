import { MutationTree } from "vuex";
import { SystemState } from "./interface";

export enum SystemMutations {
    SET_SHOW_REGISTER = "SHOW_REGISTER",
}

export const mutations: MutationTree<SystemState> = {
    [ SystemMutations.SET_SHOW_REGISTER ] (state, payload: boolean) {
        state.showRegister = payload;
    },
}
