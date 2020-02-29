import Vue from 'vue';
import { ActionTree } from 'vuex';
import {
  ChallengeCategoriesState,
  ChallengeCategory,
} from './types';
import { RootState } from '../types';
import api from '../api';


const actions: ActionTree<ChallengeCategoriesState, RootState> = {
  getChallengeCategories({ commit }): void {
    api.get('challenge-categories').then((res) => {
      const categories: ChallengeCategory[] = res && res.data;
      commit('setChallengeCategories', categories);
    });
  },
  insertChallengeCategory({ commit }, inputs: ChallengeCategory): void {
    api.post('challenge-categories', inputs).then((res) => {
      const challengeInserted: ChallengeCategory = res && res.data;
      commit('insertChallengeCategory', challengeInserted);
    });
  },
  postChallengeCategory({ commit }, edited: ChallengeCategory): void {
    api.post(`challenge-categories/${edited.category_id}`, edited).then((res) => {
      const challengeCategoryEdited: ChallengeCategory = res && res.data;
      commit('setChallengeCategory', challengeCategoryEdited);
      Vue.toasted.show(`'${edited.title}' Challenge category edited`);
    });
  },
  deleteChallengeCategory({ commit }, categoryId: string): void {
    api.delete(`challenge-categories/${categoryId}`).then(() => {
      commit('deleteChallengeCategory', categoryId);
    });
  },
};
export default actions;
