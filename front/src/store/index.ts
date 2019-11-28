import Vue from 'vue';
import Vuex from 'vuex';
import API from '@/store/api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    challengeGroups: [],
  },
  mutations: {
    setChallengeGroups(state, groups) {
      state.challengeGroups = groups;
    },
  },
  actions: {
    getChallengeGroups({commit}) {
      API().get('challenge-groups').then((res) => {
        commit('setChallengeGroups', res.data);
      }).catch((error) => {
        console.log(error);
      });
    },
  },
  modules: {
  },
});
