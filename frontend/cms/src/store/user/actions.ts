import { ActionTree } from "vuex";
import { RootState } from "../interface";
import { UserState } from "./interface";

export enum SystemActions {
    PRUNE = "CLEAR_STORE",
}

export const actions: ActionTree<UserState, RootState> = {
    [SystemActions.PRUNE] (state) {
        state.commit("CLEAR_USER");
        state.commit("CLEAR_AUTH");
    },
}
