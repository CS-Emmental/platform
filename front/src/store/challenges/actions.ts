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
};
export default actions;
