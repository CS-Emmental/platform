import { MutationTree } from 'vuex';
import {
  ChallengeParticipationsState, ChallengeParticipation,
} from './types';

const mutations: MutationTree<ChallengeParticipationsState> = {
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
};
export default mutations;
