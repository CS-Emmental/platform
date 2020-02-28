import { Module } from 'vuex';
import { ChallengeParticipationsState } from './types';
import { RootState } from '../types';
import actions from './actions';
import mutations from './mutations';
import getters from './getters';

export const state: ChallengeParticipationsState = {
  currentuserPartipations: [],
};

const namespaced = true;

export const challengeParticipations: Module<ChallengeParticipationsState, RootState> = {
  namespaced,
  state,
  actions,
  mutations,
  getters,
};
