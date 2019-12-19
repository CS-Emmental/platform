import { ActionTree } from 'vuex';
import { ChallengesState, ChallengeCategory } from './types';
import { RootState } from '../types';
import api from '../api';


const actions: ActionTree<ChallengesState, RootState> = {
  getChallengeCategories({ commit }): void {
    api().get('challenge-categories').then((res) => {
      const categories: ChallengeCategory[] = res && res.data;
      commit('setChallengeCategories', categories);
    });
  },
};
export default actions;
