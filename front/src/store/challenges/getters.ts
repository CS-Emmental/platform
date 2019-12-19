import { GetterTree } from 'vuex';
import { ChallengesState, ChallengeCategory } from './types';
import { RootState } from '../types';

export const getters: GetterTree<ChallengesState, RootState> = {
  getCategoryFromKebab(state) {
    return (kebabStr: string): ChallengeCategory | undefined => {
      return state.challengeCategories.find((cat: ChallengeCategory) => cat.kebab === kebabStr);
    }
  }
};