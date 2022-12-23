import api from "./api";
import TokenService from "./__token.service";

class AuthService {
  login(store, username, password) {
    return api
      .post("/v1/users/login", {
        username,
        password,
      })
      .then((response) => {
        if (response.status == 200) {
          TokenService.updateAccessToken(store, response.data.access_token);
          TokenService.updateRefreshToken(store, response.data.refresh_token);
        }
      });
  }

  logout(store) {
    TokenService.clearAuth(store);
  }

  register(store, username, email, password) {
    return api.post("/v1/users", {
      username,
      email,
      password,
    });
  }

  sso(store) {
    return api.get("/v1/users/sso").then((response) => {
      if (response.status == 200) {
        TokenService.setSSO(store, response.data.auth_ticket);
        TokenService.setScope(store, response.data.scope);
      }
    });
  }
}

export default new AuthService();
