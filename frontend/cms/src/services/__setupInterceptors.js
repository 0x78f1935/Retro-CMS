import instance from "./api";
import TokenService from "./__token.service";
import { AuthenticationMutations } from "@/store/user/mutations";

const setup = (store) => {
  instance.interceptors.request.use(
    (config) => {
      const token = TokenService.getAccessToken(store);
      if (token) {
        config.headers["Authorization"] = `Bearer ${token}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

  instance.interceptors.response.use(
    (res) => {
      return res;
    },
    async (err) => {
      const originalConfig = err.config;
      if (originalConfig.url !== "/v1/users/login" && err.response) {
        // Token expired
        if (err.response.status === 401 && !originalConfig._retry) {
          originalConfig._retry = true; // Bounce

          try {
            const rs = await instance.post("/v1/users/refresh", {
              headers: {
                Authorization: `Bearer ${TokenService.getRefreshToken(store)}`,
              },
            });

            const { access_token, refresh_token } = rs.data;
            store.commit(
              AuthenticationMutations.SET_ACCESS_TOKEN,
              access_token
            );
            store.commit(
              AuthenticationMutations.SET_REFRESH_TOKEN,
              refresh_token
            );
            return instance(originalConfig);
          } catch (_error) {
            return Promise.reject(_error);
          }
        }
      }

      return Promise.reject(err);
    }
  );
};

export default setup;
