import { MutationTree } from 'vuex';
import { ChallengesState, ChallengeCategory, Challenge } from './types';

const mutations: MutationTree<ChallengesState> = {
  setChallengeCategories(state, categories: ChallengeCategory[]) {
    state.challengeCategories = categories.map(
      (cat: ChallengeCategory) => ({ ...cat, slug: cat.title.toLowerCase().replace(/ /g, '-') }),
    );
  },
  setChallenges(state, challenges: Challenge[]) {
    state.challenges = challenges.map(
      (chal: Challenge) => ({ ...chal, slug: chal.title.toLowerCase().replace(/ /g, '-') }),
    );
  },
  setChallenge(state, editedChallenge: Challenge) {
    const index = state.challenges
      .findIndex((chall: Challenge) => chall.challenge_id === editedChallenge.challenge_id);
    state.challenges.splice(index, 0, editedChallenge);
  },
};
export default mutations;
