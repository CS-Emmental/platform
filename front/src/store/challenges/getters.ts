import { GetterTree } from 'vuex';
import { ChallengesState, ChallengeCategory, Challenge } from './types';
import { RootState } from '../types';

const getters: GetterTree<ChallengesState, RootState> = {
  getCategoryFromKebab(state) {
    return (kebabStr: string): ChallengeCategory | undefined => state.challengeCategories.find(
      (cat: ChallengeCategory) => cat.kebab === kebabStr,
    );
  },
  getChallengesByCategory(state) {
    return (categoryId: string): Challenge[] => state.challenges.filter(
      (chal: Challenge) => chal.category_id === categoryId,
    );
  },
  getChallengesCountByCategory(state) {
    return (categoryId: string): number => state.challenges.filter(
      (chal: Challenge) => chal.category_id === categoryId,
    ).length;
  },
};
export default getters;
