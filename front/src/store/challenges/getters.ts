import { GetterTree } from 'vuex';
import { ChallengesState, ChallengeCategory, Challenge } from './types';
import { RootState } from '../types';

const getters: GetterTree<ChallengesState, RootState> = {
  getCategoryFromKebab(state) {
    return (slugStr: string): ChallengeCategory|undefined => state.challengeCategories.find(
      (cat: ChallengeCategory) => cat.slug === slugStr,
    );
  },
  getCategoryById(state) {
    return (categoryId: string): ChallengeCategory|undefined => state.challengeCategories.find(
      (cat: ChallengeCategory) => cat.category_id === categoryId,
    );
  },
  getChallengeFromKebab(state) {
    return (slugStr: string): Challenge|undefined => state.challenges.find(
      (chal: Challenge) => chal.slug === slugStr,
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
