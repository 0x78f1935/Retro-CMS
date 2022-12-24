import { GetterTree } from "vuex";
import { RootState } from "../interface";
import { TaskState } from "./interface";

export const getters: GetterTree<TaskState, RootState> = {
    tasks (state): object[] { return state.tasks; },
}