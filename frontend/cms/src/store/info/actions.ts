import { ActionTree } from "vuex";
import { RootState } from "../interface";
import PublicService from "@/services/public.service";
import { InfoState } from "./interface";

export enum InfoActions {
    PUBLIC = "PUBLIC",
}

export const actions: ActionTree<InfoState, RootState> = {
    [InfoActions.PUBLIC] (state) {
        PublicService.getPublicContent(state);
    },
}
