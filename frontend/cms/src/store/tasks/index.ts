import { Module } from "vuex";
import { RootState } from "../interface";
import { TaskState } from "./interface";
import { getters } from "./getters";
import { mutations } from "./mutations";
import { actions } from "./actions";

const state: TaskState = {
    tasks: []
}

export const tasks: Module<TaskState, RootState> = {
    state,
    getters,
    mutations,
    actions
}