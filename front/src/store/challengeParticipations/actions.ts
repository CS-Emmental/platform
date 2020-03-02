import { ActionTree } from 'vuex';
import {
  ChallengeParticipationsState, ChallengeParticipation,
} from './types';
import { RootState } from '../types';
import api from '../api';


const actions: ActionTree<ChallengeParticipationsState, RootState> = {

  getCurrentuserChallengeParticipations({ commit }): void {
    api.get('challenge-participations/current-user').then((res) => {
      const participations: ChallengeParticipation[] = res && res.data;
      commit('setCurrentuserChallengeParticipations', participations);
    });
  },
  startChallengeParticipation({ commit }, challengeId: string): void {
    api.post('challenge-participations', { challenge_id: challengeId }).then((res) => {
      const participation: ChallengeParticipation = res && res.data;
      commit('insertCurrentuserChallengeParticipation', participation);
    });
  },
  restartChallengeParticipation({ commit }, participationId: string): void {
    api.post(`challenge-participations/${participationId}/restart-instance`).then((res) => {
      const participation: ChallengeParticipation = res && res.data;
      commit('setParticipation', participation);
    });
  },
  stopChallengeParticipation({ commit }, participationId: string): void {
    api.post(`challenge-participations/${participationId}/stop-instance`).then((res) => {
      const participation: ChallengeParticipation = res && res.data;
      commit('setParticipation', participation);
    });
  },
  postParticipation({ commit }, edited: ChallengeParticipation): void {
    api.post(`challenge-participations/${edited.participation_id}`, edited).then((res) => {
      const participationEdited: ChallengeParticipation = res && res.data;
      commit('setParticipation', participationEdited);
    });
  },
  useHints({ commit }, updated: ChallengeParticipation): void {
    api.post(
      `/challenge-participations/${updated.participation_id}/hints`,
      updated.used_hints,
    ).then((res) => {
      const hintList: { index: number; text: string }[] = res && res.data;
      commit('setParticipation', updated);
      commit('challenges/setHintsText', { challengeId: updated.challenge_id, hintList });
    });
  },
  submitFlag({ commit }, { participationId, index, secret }: {
    participationId: string; index: number; secret: string;
  }): void {
    api.post(
      `challenge-participations/${participationId}/flags`,
      {
        index,
        secret,
      },
    ).then((res) => {
      const participationEdited: ChallengeParticipation = res && res.data;
      commit('setParticipation', participationEdited);
    });
  },
};
export default actions;
