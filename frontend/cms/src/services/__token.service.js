import { AuthenticationMutations } from "@/store/user/mutations";

class TokenService {
  getRefreshToken(store) {
    return store.getters.refresh_token;
  }
  getAccessToken(store) {
    return store.getters.access_token;
  }

  updateAccessToken(store, token) {
    store.commit(AuthenticationMutations.SET_ACCESS_TOKEN, token);
  }

  updateRefreshToken(store, token) {
    store.commit(AuthenticationMutations.SET_REFRESH_TOKEN, token);
  }

  clearAuth(store) {
    store.commit(AuthenticationMutations.CLEAR_AUTH);
  }

  setScope(store, scope) {
    store.commit(AuthenticationMutations.SET_SCOPE, scope);
  }

  setSSO(store, SSO) {
    store.commit(AuthenticationMutations.SET_SSO_TOKEN, SSO);
  }
}

export default new TokenService();
