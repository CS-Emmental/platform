import { GetterTree } from 'vuex';
import {
  ChallengeParticipationsState,
  ChallengeParticipation,
}
  from './types';
import { Challenge } from '../challenges/types';
import { RootState } from '../types';

const getters: GetterTree<ChallengeParticipationsState, RootState> = {
  getParticipationByChallengeId(state) {
    return (challengeId: string): ChallengeParticipation|undefined => state.currentuserPartipations
      .find(
        (participation: ChallengeParticipation) => participation.challenge_id === challengeId,
      );
  },
  getParticipationFinalScore(state, _, rootState) {
    return (participationId: string): number => {
      const participation = state.currentuserPartipations
        .find(part => part.participation_id === participationId);
      const challenge = participation && rootState.challenges && rootState.challenges.challenges
        .find((chall: Challenge) => chall.challenge_id === participation.challenge_id);
      if (!challenge || !participation) {
        return 0;
      }
      let progress = 0;
      participation.found_flags.forEach((index) => {
        progress += challenge.flags[index].reward;
      });
      let malus = 0;
      participation.used_hints.forEach((index) => {
        malus += challenge.hints[index].cost;
      });

      return (progress - malus) * challenge.total_points;
    };
  },
};
export default getters;
