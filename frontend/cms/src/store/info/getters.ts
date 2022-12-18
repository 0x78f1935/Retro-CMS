import { GetterTree } from "vuex";
import { RootState } from "../interface";
import { InfoState } from "./interface";

export const getters: GetterTree<InfoState, RootState> = {
    app_long_name (state): string { return state.app_long_name; },
    app_short_name (state): string { return state.app_short_name; },
    app_name_logo (state): string { return state.app_name_logo; },
}