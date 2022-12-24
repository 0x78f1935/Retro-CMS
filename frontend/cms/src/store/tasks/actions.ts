import { ActionTree } from "vuex";
import { RootState } from "../interface";
import { TaskState } from "./interface";
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
import TaskService from "@/services/tasks.service";

export enum TaskActions {
    POLL = "POLL_TASKS",
    EXECUTE = "EXECUTE_TASKS",
}

export const actions: ActionTree<TaskState, RootState> = {
    [TaskActions.POLL] (state) {
        TaskService.poll(state);
    },

    [TaskActions.EXECUTE] (state, { task_id }) {
        TaskService.execute(state, task_id);
    },
}
