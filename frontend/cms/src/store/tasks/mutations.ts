import { MutationTree } from "vuex";
import { TaskState } from "./interface";

export enum TaskMutations {
    SET_TASKS = "SET_TASKS",
}

export const mutations: MutationTree<TaskState> = {
    [ TaskMutations.SET_TASKS ] (state, payload: object[]) {
        state.tasks = payload;
    },
}
