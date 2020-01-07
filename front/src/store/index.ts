import Vue from 'vue';
import Vuex, {
  StoreOptions, ActionTree, MutationTree, GetterTree,
} from 'vuex';
import { RootState, User } from './types';
import { challenges } from './challenges/index';
import api from './api';
import router from '../router';

Vue.use(Vuex);

const actions: ActionTree<RootState, RootState> = {
  login({ commit }, inputs): void {
    api().post('login', inputs).then((res) => {
      const user: User = res && res.data;
      commit('setCurrentUser', user);
      commit('setIsAuthenticated', true);
      router.push('/');
      // eslint-disable-next-line
      location.reload();
    });
  },
  getCurrentUser({ commit }): void {
    api().get('current-user').then((res) => {
      const user: User = res && res.data;
      commit('setCurrentUser', user);
      if (user) {
        commit('setIsAuthenticated', true);
      }
    });
  },
  logout({ commit }): void {
    api().get('logout').then(() => {
      commit('setCurrentUser', undefined);
      commit('setIsAuthenticated', false);
      router.push('/');
      // eslint-disable-next-line
      location.reload();
    });
  },
};

const mutations: MutationTree<RootState> = {
  setCurrentUser(state, user: User) {
    state.currentUser = user;
  },
  setIsAuthenticated(state, isAuthenticated: boolean) {
    state.isAuthenticated = isAuthenticated;
  },
};

const getters: GetterTree<RootState, RootState> = {
  hasPermission(state) {
    return (permission: string): boolean => state.currentUser !== undefined
      && state.currentUser.permissions.includes(permission);
  },
};

const store: StoreOptions<RootState> = {
  state: {
    version: '0.0.1',
    currentUser: undefined,
    isAuthenticated: false,
  },
  actions,
  mutations,
  getters,
  modules: {
    challenges,
  },
};

export default new Vuex.Store<RootState>(store);
