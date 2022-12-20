import { GetterTree } from "vuex";
import { RootState } from "../interface";
import { SystemState } from "./interface";

export const getters: GetterTree<SystemState, RootState> = {
    showRegister (state): boolean { return state.showRegister; },
}