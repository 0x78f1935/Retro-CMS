import { MutationTree } from "vuex";
import { UserState } from "./interface";

export enum UserMutations {
    CLEAR_USER = "PRUNE_USER",
    SET_EMAIL = "SET_EMAIL",
}

export enum AuthenticationMutations {
    CLEAR_AUTH = "PRUNE_AUTH",
    SET_ACCESS_TOKEN = "SET_ACCESS_TOKEN",
    SET_SSO_TOKEN = "SET_SSO_TOKEN",
    SET_SCOPE = "SET_SCOPE",
}

export const mutations: MutationTree<UserState> = {
    [ UserMutations.SET_EMAIL ] (state, payload: string) {
        state.email = payload;
    },
    [ UserMutations.CLEAR_USER ] (state) {
        state.username = "";
        state.email = "";
    },

    [ AuthenticationMutations.CLEAR_AUTH ] (state) {
        state.access_token = "";
        state.sso_token = "";
        state.scope = [];
    },
    [ AuthenticationMutations.SET_ACCESS_TOKEN ] (state, payload: string) {
        state.access_token = payload;
    },
    [ AuthenticationMutations.SET_SSO_TOKEN ] (state, payload: string) {
        state.sso_token = payload;
    },
    [ AuthenticationMutations.SET_SCOPE ] (state, payload: string[]) {
        state.scope = payload;
    }
}
