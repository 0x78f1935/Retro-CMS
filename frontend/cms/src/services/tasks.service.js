import api from "./api";
import { TaskMutations } from "@/store/tasks/mutations";

class TaskService {
  poll(store) {
    return api.get("/v1/system/tasks").then((response) => {
      if (response.status == 200) {
        store.commit(TaskMutations.SET_TASKS, response.data);
      }
    });
  }

  execute(store, task_id) {
    return api.post("/v1/system/tasks", { id: task_id })
    .then((response) => {
      if (response.status == 200) {
        console.log(response.data);
        return;
      }
      console.error("Something went wrong, Try again!");
      console.error(response.data);
    });
  }
}

export default new TaskService();
