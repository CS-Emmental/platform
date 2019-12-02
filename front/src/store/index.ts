import Vue from 'vue';
import Vuex from 'vuex';
import API from '@/store/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    challengeCategories: [],
  },
  mutations: {
    setChallengeCategories(state, categories) {
      state.challengeCategories = categories;
    },
  },
  actions: {
    getChallengeCategories({commit}) {
      API().get('challenge-categories').then((res) => {
        commit('setChallengeCategories', res.data);
      });
    },
  },
  modules: {
  },
});
