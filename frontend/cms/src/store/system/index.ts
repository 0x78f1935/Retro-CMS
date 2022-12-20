import { Module } from "vuex";
import { RootState } from "../interface";
import { SystemState } from "./interface";
import { getters } from "./getters";
import { mutations } from "./mutations";

const state: SystemState = {
    showRegister: false,
}

export const system: Module<SystemState, RootState> = {
    state,
    getters,
    mutations,
}