import { GetterTree } from 'vuex';
import {
  ChallengesState,
  Challenge,
}
  from './types';
import { RootState } from '../types';
import { ChallengeCategory } from '../challengeCategories/types';

const getters: GetterTree<ChallengesState, RootState> = {
  getChallengeFromSlug(state) {
    return (slugStr: string): Challenge|undefined => state.challenges.find(
      (chal: Challenge) => chal.title_slug === slugStr,
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
  getChallengeById(state) {
    return (challengeId: string): Challenge|undefined => state.challenges.find(
      (chall: Challenge) => chall.challenge_id === challengeId,
    );
  },
  getLastChallenges(state) {
    return state.challenges.sort((a, b) => a.updated_at - b.updated_at).slice(0, 5);
  },
  getChallengeLink(state, _, rootState) {
    return (challengeId: string): string|undefined => {
      const challenge = state.challenges.find(
        (chal: Challenge) => chal.challenge_id === challengeId,
      );
      const category = challenge && rootState.challengeCategories
        && rootState.challengeCategories.challengeCategories.find(
          (cat: ChallengeCategory) => cat.category_id === challenge.category_id,
        );
      return challenge && category && `/challenges/${category.title_slug}/${challenge.title_slug}`;
    };
  },
};
export default getters;
