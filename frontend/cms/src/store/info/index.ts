import { Module } from "vuex";
import { RootState } from "../interface";
import { InfoState } from "./interface";
import { getters } from "./getters";
import { mutations } from "./mutations";

const state: InfoState = {
    app_long_name: "",
    app_short_name: "",
    app_name_logo: "",
    assets_ran: "",
    assets_status: "",
    converter_ran: "",
    converter_status: "",
}

export const info: Module<InfoState, RootState> = {
    state,
    getters,
    mutations,
}