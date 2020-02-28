import { MutationTree } from 'vuex';
import {
  ChallengesState, Challenge,
} from './types';

const mutations: MutationTree<ChallengesState> = {
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
