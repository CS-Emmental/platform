import { MutationTree } from 'vuex';
import { ChallengesState, ChallengeCategory } from './types';

const mutations: MutationTree<ChallengesState> = {
  setChallengeCategories(state, categories: ChallengeCategory[]) {
    state.challengeCategories = categories.map(
      (cat: ChallengeCategory) => ({ ...cat, kebab: cat.title.toLowerCase().replace(' ', '-') }),
    );
  },
};
export default mutations;
