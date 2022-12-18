import { RuleState } from "./rules/interface";
import { UserState } from "./user/interface";

export interface RootState {
    user: UserState,
    rules: RuleState
}