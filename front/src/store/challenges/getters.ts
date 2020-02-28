import { GetterTree } from 'vuex';
import {
  ChallengesState,
  Challenge,
}
  from './types';
import { RootState } from '../types';
import { slug } from '../utils';

const getters: GetterTree<ChallengesState, RootState> = {
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
  getChallengeById(state) {
    return (challengeId: string): Challenge|undefined => state.challenges.find(
      (chall: Challenge) => chall.challenge_id === challengeId,
    );
  },
};
export default getters;
