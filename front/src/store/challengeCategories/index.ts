import { Module } from 'vuex';
import { ChallengeCategoriesState } from './types';
import { RootState } from '../types';
import actions from './actions';
import mutations from './mutations';
import getters from './getters';

export const state: ChallengeCategoriesState = {
  challengeCategories: [],
};

const namespaced = true;

export const challengeCategories: Module<ChallengeCategoriesState, RootState> = {
  namespaced,
  state,
  actions,
  mutations,
  getters,
};
