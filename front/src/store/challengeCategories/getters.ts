import { GetterTree } from 'vuex';
import {
  ChallengeCategoriesState,
  ChallengeCategory,
}
  from './types';
import { RootState } from '../types';
import { slug } from '../utils';

const getters: GetterTree<ChallengeCategoriesState, RootState> = {
  getCategoryFromSlug(state) {
    return (slugStr: string): ChallengeCategory|undefined => state.challengeCategories.find(
      (cat: ChallengeCategory) => slug(cat.title) === slugStr,
    );
  },
  getCategoryById(state) {
    return (categoryId: string): ChallengeCategory|undefined => state.challengeCategories.find(
      (cat: ChallengeCategory) => cat.category_id === categoryId,
    );
  },
};
export default getters;
