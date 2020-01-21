import { Module } from 'vuex';
import { ChallengesState } from './types';
import { RootState } from '../types';
import actions from './actions';
import mutations from './mutations';
import getters from './getters';

export const state: ChallengesState = {
  challengeCategories: [],
  challenges: [],
};

const namespaced = true;

export const challenges: Module<ChallengesState, RootState> = {
  namespaced,
  state,
  actions,
  mutations,
  getters,
};
