import api from "./api";
import { InfoMutations } from "@/store/info/mutations";

class PublicService {
  getPublicContent(store) {
    return api.get("/v1/info/app").then((response) => {
      if (response.status == 200) {
        store.commit(InfoMutations.SET_APP_LONG_NAME, response.data.name_long);
        store.commit(
          InfoMutations.SET_APP_SHORT_NAME,
          response.data.name_short
        );
        store.commit(InfoMutations.SET_APP_NAME_LOGO, response.data.logo);
        store.commit(InfoMutations.SET_ASSET_RAN, response.data.assets_ran);
        store.commit(
          InfoMutations.SET_ASSET_STATUS,
          response.data.assets_status
        );
        store.commit(
          InfoMutations.SET_CONVERTER_RAN,
          response.data.converter_ran
        );
        store.commit(
          InfoMutations.SET_CONVERTER_STATUS,
          response.data.converter_status
        );
        store.commit(InfoMutations.SET_RANDOM_LOOK, response.data.random_look);
      }
    });
  }
}

export default new PublicService();
