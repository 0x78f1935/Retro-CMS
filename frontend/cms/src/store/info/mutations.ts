import { MutationTree } from "vuex";
import { InfoState } from "./interface";

export enum InfoMutations {
    SET_APP_LONG_NAME = "SET_APP_LONG_NAME",
    SET_APP_SHORT_NAME = "SET_APP_SHORT_NAME",
    SET_APP_NAME_LOGO = "SET_APP_NAME_LOGO",
}

export const mutations: MutationTree<InfoState> = {
    [ InfoMutations.SET_APP_LONG_NAME ] (state, payload: string) {
        state.app_long_name = payload;
    },
    [ InfoMutations.SET_APP_SHORT_NAME ] (state, payload: string) {
        state.app_short_name = payload;
    },

    [ InfoMutations.SET_APP_NAME_LOGO ] (state, payload: string) {
        state.app_name_logo = payload;
    },
}
