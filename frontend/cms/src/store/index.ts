import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './interface';
import { user } from '@/store/user';
import { rules } from '@/store/rules';
import { info } from '@/store/info';

const store: StoreOptions<RootState> = {
  modules: {
    user,
    rules,
    info
  }
}

export default new Vuex.Store<RootState>(store);
