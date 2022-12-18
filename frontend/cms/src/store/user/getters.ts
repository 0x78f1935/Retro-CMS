import { GetterTree } from "vuex";
import { RootState } from "../interface";
import { UserState } from "./interface";

export const getters: GetterTree<UserState, RootState> = {
    username (state): string { return state.username; },
    email (state): string { return state.email; },
    access_token (state): string { return state.access_token; },
    refresh_token (state): string { return state.refresh_token; },
    sso_token (state): string { return state.sso_token; },
    scope (state): string[] { return state.scope; },
}