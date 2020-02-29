import { MutationTree } from 'vuex';
import {
  ChallengeCategoriesState,
  ChallengeCategory,
} from './types';

const mutations: MutationTree<ChallengeCategoriesState> = {
  setChallengeCategories(state, categories: ChallengeCategory[]) {
    state.challengeCategories = categories;
  },
  insertChallengeCategory(state, insertedChallengeCategory: ChallengeCategory) {
    state.challengeCategories.push(insertedChallengeCategory);
  },
  setChallengeCategory(state, editChallengeCategory: ChallengeCategory) {
    const index = state.challengeCategories
      .findIndex((cat: ChallengeCategory) => cat.category_id === editChallengeCategory.category_id);
    state.challengeCategories.splice(index, 1, editChallengeCategory);
  },
  deleteChallengeCategory(state, categoryId: string) {
    const index = state.challengeCategories
      .findIndex((cat: ChallengeCategory) => cat.category_id === categoryId);
    state.challengeCategories.splice(index, 1);
  },
};
export default mutations;
