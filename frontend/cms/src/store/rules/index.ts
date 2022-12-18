import { Module } from "vuex";
import { RootState } from "../interface";
import { RuleState } from "./interface";
import { getters } from "./getters";

const state: RuleState = {
    required: (value: string) => !!value || "Field is required.",
    username: [
        // Rules for the username
        (v: string) => !!v || "Username is required",
        (v: string) => v.length < 17 || "Max 16 characters",
        (v: string) => v.length > 4 || "Min 5 characters",
        (v: string) => /^([A-Za-z0-9\_]+)$/.test(v) || "Only: aBc_0123",  // eslint-disable-line
      ],
    email: [
        (v: string) => !!v || "E-mail address is required",
        (v: string) =>
            /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) ||
            "Must be a valid e-mail address",
    ],
    password: [
        // Rules for the password
        (v: string) => !!v || "Password is required",
        (v: string) => v.length > 5 || "Min 6 characters",
        (v: string) => (v && /\d/.test(v)) || "At least one digit",  // eslint-disable-line
        (v: string) => (v && /[A-Z]{1}/.test(v)) || "At least one Capital letter",  // eslint-disable-line
        (v: string) => (v && /[^A-Za-z0-9]/.test(v)) || "At least one special character",  // eslint-disable-line
        (v: string) => v.length < 37 || "Max 36 characters",
    ],
}

export const rules: Module<RuleState, RootState> = {
    state,
    getters,
}