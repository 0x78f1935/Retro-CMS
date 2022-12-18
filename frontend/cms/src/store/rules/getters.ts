/* eslint-disable @typescript-eslint/ban-types */
import { GetterTree } from "vuex";
import { RootState } from "../interface";
import { RuleState } from "./interface";

export const getters: GetterTree<RuleState, RootState> = {
    rule_required (state): Function { return state.required; },
    rule_username (state): Array<Function> { return state.username; },
    rule_email (state): Array<Function> { return state.email; },
    rule_password (state): Array<Function> { return state.password; },
}