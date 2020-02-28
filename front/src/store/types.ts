import { ChallengesState } from './challenges/types';
import { ChallengeParticipationsState } from './challengeParticipations/types';
import { ChallengeCategoriesState } from './challengeCategories/types';

export interface RootState {
  version: string;
  currentUser?: User;
  isAuthenticated: boolean;
  challenges?: ChallengesState;
  challengeParticipations?: ChallengeParticipationsState;
  challengeCategories?: ChallengeCategoriesState;
}

export interface User {
  user_id: string;
  username: string;
  email: string;
  firstname: string;
  lastname: string;
  permissions: string[];
  created_at: number;
}
