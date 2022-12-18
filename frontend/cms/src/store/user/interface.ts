export interface UserState {
    username: string,
    email: string,
    access_token: string,
    refresh_token: string,
    sso_token: string,
    scope: string[]
}