import { GetterTree } from 'vuex';
import {
  ChallengesState,
  ChallengeCategory,
  Challenge,
  ChallengeParticipation,
}
  from './types';
import { RootState } from '../types';
import { slug } from '../utils';

const getters: GetterTree<ChallengesState, RootState> = {
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
  getChallengeFromSlug(state) {
    return (slugStr: string): Challenge|undefined => state.challenges.find(
      (chal: Challenge) => slug(chal.title) === slugStr,
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
  getParticipationByChallengeId(state) {
    return (challengeId: string): ChallengeParticipation|undefined => state.currentuserPartipations
      .find(
        (participation: ChallengeParticipation) => participation.challenge_id === challengeId,
      );
  },
};
export default getters;
