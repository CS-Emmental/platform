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
};
export default mutations;
