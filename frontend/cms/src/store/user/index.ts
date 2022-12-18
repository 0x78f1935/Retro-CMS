import { Module } from "vuex";
import { RootState } from "../interface";
import { UserState } from "./interface";
import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

const state: UserState = {
    username: "",
    email: "",
    access_token: "",
    refresh_token: "",
    sso_token: "",
    scope: []
}

export const user: Module<UserState, RootState> = {
    state,
    getters,
    mutations,
    actions
}