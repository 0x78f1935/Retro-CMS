import Vuex, { StoreOptions } from 'vuex';
import { RootState } from './interface';
import { user } from '@/store/user';
import { rules } from '@/store/rules';
import { info } from '@/store/info';
import { system } from '@/store/system';
import { tasks } from '@/store/tasks';

const store: StoreOptions<RootState> = {
  modules: {
    user,
    rules,
    info,
    system,
    tasks
  }
}

export default new Vuex.Store<RootState>(store);
