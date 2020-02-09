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
  setChallengeCategory(state, editChallengeCategory: ChallengeCategory) {
    const index = state.challengeCategories
      .findIndex((cat: ChallengeCategory) => cat.category_id === editChallengeCategory.category_id);
    state.challengeCategories.splice(index, 1, editChallengeCategory);
  },
  setHintsText(state, { challengeId, hintList }: {
    challengeId: string; hintList: {index: number; text: string}[];
  }) {
    const index = state.challenges
      .findIndex((chall: Challenge) => chall.challenge_id === challengeId);
    const editedChallenge = { ...state.challenges[index] };
    hintList.forEach((hint: {index: number; text: string}) => {
      editedChallenge.hints[hint.index].text = hint.text;
    });
    state.challenges.splice(index, 1, editedChallenge);
  },
};
export default mutations;
