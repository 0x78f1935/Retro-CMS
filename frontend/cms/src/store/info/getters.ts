import { GetterTree } from "vuex";
import { RootState } from "../interface";
import { InfoState } from "./interface";

export const getters: GetterTree<InfoState, RootState> = {
    app_long_name (state): string { return state.app_long_name; },
    app_short_name (state): string { return state.app_short_name; },
    app_name_logo (state): string { return state.app_name_logo; },
    assets_ran (state): string { return state.assets_ran; },
    assets_status (state): string { return state.assets_status; },
    converter_ran (state): string { return state.converter_ran; },
    converter_status (state): string { return state.converter_status; },
    random_look (state): string { return state.random_look; },
}