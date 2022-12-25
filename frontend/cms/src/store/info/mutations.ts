import { MutationTree } from "vuex";
import { InfoState } from "./interface";

export enum InfoMutations {
    SET_APP_LONG_NAME = "SET_APP_LONG_NAME",
    SET_APP_SHORT_NAME = "SET_APP_SHORT_NAME",
    SET_APP_NAME_LOGO = "SET_APP_NAME_LOGO",
    SET_ASSET_RAN = "SET_ASSET_RAN",
    SET_ASSET_STATUS = "SET_ASSET_STATUS",
    SET_CONVERTER_RAN = "SET_CONVERTER_RAN",
    SET_CONVERTER_STATUS = "SET_CONVERTER_STATUS",
    SET_IMAGER_RAN = "SET_IMAGER_RAN",
    SET_IMAGER_STATUS = "SET_IMAGER_STATUS",
    SET_RANDOM_LOOK = "SET_RANDOM_LOOK"
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

    [ InfoMutations.SET_ASSET_RAN ] (state, payload: string) {
        state.assets_ran = payload;
    },

    [ InfoMutations.SET_ASSET_STATUS ] (state, payload: string) {
        state.assets_status = payload;
    },

    [ InfoMutations.SET_CONVERTER_RAN ] (state, payload: string) {
        state.converter_ran = payload;
    },

    [ InfoMutations.SET_CONVERTER_STATUS ] (state, payload: string) {
        state.converter_status = payload;
    },

    [ InfoMutations.SET_IMAGER_RAN ] (state, payload: string) {
        state.imager_ran = payload;
    },

    [ InfoMutations.SET_IMAGER_STATUS ] (state, payload: string) {
        state.imager_status = payload;
    },

    [ InfoMutations.SET_RANDOM_LOOK ] (state, payload: string) {
        state.random_look = payload;
    },
}
