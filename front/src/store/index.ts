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
  getConfig({ commit }): void {
    api().get('config').then((res) => {
      const version: string = res && res.data && res.data.version;
      commit('setVersion', version);
      const isAuthenticated = res && res.data && res.data.authenticated;
      commit('setIsAuthenticated', isAuthenticated);
      if (isAuthenticated) {
        const user: User = res && res.data && res.data.currentUser;
        commit('setCurrentUser', user);
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
  setVersion(state, version: string) {
    state.version = version;
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
