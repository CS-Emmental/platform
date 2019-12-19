import { GetterTree } from 'vuex';
import { ChallengesState, ChallengeCategory } from './types';
import { RootState } from '../types';

const getters: GetterTree<ChallengesState, RootState> = {
  getCategoryFromKebab(state) {
    return (kebabStr: string): ChallengeCategory | undefined => state.challengeCategories.find(
      (cat: ChallengeCategory) => cat.kebab === kebabStr,
    );
  },
};
export default getters;
