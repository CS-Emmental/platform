import Vue from 'vue';
import Vuex, { StoreOptions, ActionTree, MutationTree } from 'vuex';
import { RootState, User } from './types';
import { challenges } from './challenges/index';
import api from './api';
import router from '../router';

Vue.use(Vuex);

const actions: ActionTree<RootState, RootState> = {
  login({ commit }): void {
    api().get('login').then((res) => {
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

const store: StoreOptions<RootState> = {
  state: {
    version: '1.0.0',
    currentUser: undefined,
    isAuthenticated: false,
  },
  actions,
  mutations,
  modules: {
    challenges,
  },
};

export default new Vuex.Store<RootState>(store);
