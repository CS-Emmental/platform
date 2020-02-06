import { MutationTree } from 'vuex';
import {
  ChallengesState, ChallengeCategory, Challenge, ChallengeParticipation,
} from './types';

const mutations: MutationTree<ChallengesState> = {
  setChallengeCategories(state, categories: ChallengeCategory[]) {
    state.challengeCategories = categories;
  },
  setChallenges(state, challenges: Challenge[]) {
    state.challenges = challenges;
  },
  setChallenge(state, editedChallenge: Challenge) {
    const index = state.challenges
      .findIndex((chall: Challenge) => chall.challenge_id === editedChallenge.challenge_id);
    state.challenges.splice(index, 1, editedChallenge);
  },
  insertChallenge(state, insertedChallenge: Challenge) {
    state.challenges.push(insertedChallenge);
  },
  deleteChallenge(state, challengId: string) {
    const index = state.challenges
      .findIndex((chall: Challenge) => chall.challenge_id === challengId);
    state.challenges.splice(index, 1);
  },
  setCurrentuserChallengeParticipations(state, participations: ChallengeParticipation[]) {
    state.currentuserPartipations = participations;
  },
  insertCurrentuserChallengeParticipation(state, participation: ChallengeParticipation) {
    state.currentuserPartipations.push(participation);
  },
  setParticipation(state, edited: ChallengeParticipation) {
    const index = state.currentuserPartipations
      .findIndex((p: ChallengeParticipation) => p.participation_id === edited.participation_id);
    state.currentuserPartipations.splice(index, 1, edited);
  },
  insertChallengeCategory(state, insertedChallengeCategory: ChallengeCategory) {
    state.challengeCategories.push(insertedChallengeCategory);
  },
  setChallengeCategory(state, editedChallengeCategory: ChallengeCategory) {
    const index = state.challengeCategories
      .findIndex((ct: ChallengeCategory) => ct.category_id === editedChallengeCategory.category_id);
    state.challengeCategories.splice(index, 1, editedChallengeCategory);
  },
};
export default mutations;
