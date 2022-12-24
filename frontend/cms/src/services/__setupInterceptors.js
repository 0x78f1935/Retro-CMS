import instance from "./api";
import TokenService from "./__token.service";
import { AuthenticationMutations } from "@/store/user/mutations";
import router from "@/router";
import axios from "axios";

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
            const _refresh_token = TokenService.getRefreshToken(store);
            axios.defaults.headers.common['Authorization'] = `Bearer ${_refresh_token}`;
            const rs = await axios.post("/api/v1/users/refresh").catch(() => {router.push('/');});

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
