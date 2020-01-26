import Vue from 'vue';
import { ActionTree } from 'vuex';
import { ChallengesState, ChallengeCategory, Challenge } from './types';
import { RootState } from '../types';
import api from '../api';


const actions: ActionTree<ChallengesState, RootState> = {
  getChallengeCategories({ commit }): void {
    api().get('challenge-categories').then((res) => {
      const categories: ChallengeCategory[] = res && res.data;
      commit('setChallengeCategories', categories);
    });
  },
  getChallenges({ commit }): void {
    api().get('challenges').then((res) => {
      const challenges: Challenge[] = res && res.data;
      commit('setChallenges', challenges);
    });
  },
  postChallenge({ commit }, edited: Challenge): void {
    api().post(`challenges/${edited.challenge_id}`, edited).then((res) => {
      const challengeEdited: Challenge = res && res.data;
      commit('setChallenge', challengeEdited);
      Vue.toasted.show(`'${edited.title}' Challenge edited`);
    });
  },
  insertChallenge({ commit }, inputs: Challenge): void {
    api().post('challenges', inputs).then((res) => {
      const challengeInserted: Challenge = res && res.data;
      commit('insertChallenge', challengeInserted);
    });
  },
  deleteChallenge({ commit }, challengeId: string): void {
    api().delete(`challenges/${challengeId}`).then(() => {
      commit('deleteChallenge', challengeId);
    });
  },
};
export default actions;
