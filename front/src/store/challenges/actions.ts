import Vue from 'vue';
import { ActionTree } from 'vuex';
import {
  ChallengesState, ChallengeCategory, Challenge, ChallengeParticipation,
} from './types';
import { RootState } from '../types';
import api from '../api';


const actions: ActionTree<ChallengesState, RootState> = {
  getChallengeCategories({ commit }): void {
    api.get('challenge-categories').then((res) => {
      const categories: ChallengeCategory[] = res && res.data;
      commit('setChallengeCategories', categories);
    });
  },
  getChallenges({ commit }): void {
    api.get('challenges').then((res) => {
      const challenges: Challenge[] = res && res.data;
      commit('setChallenges', challenges);
    });
  },
  postChallenge({ commit }, edited: Challenge): void {
    api.post(`challenges/${edited.challenge_id}`, edited).then((res) => {
      const challengeEdited: Challenge = res && res.data;
      commit('setChallenge', challengeEdited);
      Vue.toasted.show(`'${edited.title}' Challenge edited`);
    });
  },
  insertChallenge({ commit }, inputs: Challenge): void {
    api.post('challenges', inputs).then((res) => {
      const challengeInserted: Challenge = res && res.data;
      commit('insertChallenge', challengeInserted);
    });
  },
  deleteChallenge({ commit }, challengeId: string): void {
    api.delete(`challenges/${challengeId}`).then(() => {
      commit('deleteChallenge', challengeId);
    });
  },
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
  postParticipation({ commit }, edited: ChallengeParticipation): void {
    api.post(`challenge-participations/${edited.participation_id}`, edited).then((res) => {
      const participationEdited: ChallengeParticipation = res && res.data;
      commit('setParticipation', participationEdited);
    });
  },
  insertChallengeCategory({ commit }, inputs: ChallengeCategory): void {
    api.post('challenge-category', inputs).then((res) => {
      const challengeInserted: Challenge = res && res.data;
      commit('insertChallengeCategory', challengeInserted);
    });
  },
  postChallengeCategory({ commit }, edited: ChallengeCategory): void {
    api.post(`challenge-category/${edited.category_id}`, edited).then((res) => {
      const challengeCategoryEdited: ChallengeCategory = res && res.data;
      commit('setChallengeCategory', challengeCategoryEdited);
      Vue.toasted.show(`'${edited.title}' Challenge category edited`);
    });
  },
  deleteChallengeCategory({ commit }, categoryId: string): void {
    api.delete(`challenge-category/${categoryId}`).then(() => {
      commit('deleteChallengeCategory', categoryId);
    });
  },
};
export default actions;
