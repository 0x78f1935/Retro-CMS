import { ActionTree } from "vuex";
import { RootState } from "../interface";
import { UserState } from "./interface";
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
import AuthService from "@/services/auth.service";
import { UserMutations } from "./mutations";

export enum SystemActions {
    PRUNE = "CLEAR_STORE",
}

export enum UserActions {
    USER_LOGIN = "AUTH_USER",
    USER_LOGOUT = "OUT_USER",
    USER_REGISTER = "REG_USER",
}

export const actions: ActionTree<UserState, RootState> = {
    [SystemActions.PRUNE] (state) {
        state.commit("CLEAR_USER");
        state.commit("CLEAR_AUTH");
    },

    [UserActions.USER_LOGIN] (state, {username, password}) {
        state.commit(UserMutations.SET_USERNAME, username);
        AuthService.login(state, username, password);
        AuthService.sso(state);
    },

    [UserActions.USER_LOGOUT] (state) {
        AuthService.logout(state);
        state.dispatch(SystemActions.PRUNE);
    },

    async [UserActions.USER_REGISTER] (state, {username, email, password}) {
        state.commit(UserMutations.SET_EMAIL, email);
        state.commit(UserMutations.SET_USERNAME, username);
        await AuthService.register(state, username, email, password);
        state.dispatch(UserActions.USER_LOGIN, {username, password});
    }
}
