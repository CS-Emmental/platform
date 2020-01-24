import { MutationTree } from 'vuex';
import { ChallengesState, ChallengeCategory, Challenge } from './types';

const mutations: MutationTree<ChallengesState> = {
  setChallengeCategories(state, categories: ChallengeCategory[]) {
    state.challengeCategories = categories.map(
      (cat: ChallengeCategory) => ({ ...cat }),
    );
  },
  setChallenges(state, challenges: Challenge[]) {
    state.challenges = challenges.map(
      (chal: Challenge) => ({ ...chal }),
    );
  },
  setChallenge(state, editedChallenge: Challenge) {
    const index = state.challenges
      .findIndex((chall: Challenge) => chall.challenge_id === editedChallenge.challenge_id);
    state.challenges.splice(index, 1, editedChallenge);
  },
  insertChallenge(state, insertedChallenge: Challenge) {
    state.challenges.push(insertedChallenge);
  },
};
export default mutations;
