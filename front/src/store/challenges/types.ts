export interface ChallengesState {
  challengeCategories: ChallengeCategory[];
  challenges: Challenge[];
  currentuserPartipations: ChallengeParticipation[];
}

export interface ChallengeCategory {
  title: string;
  category_id: string;
  icon: string;
  description: string;
}

export interface Challenge {
  challenge_id: string;
  title: string;
  category_id: string;
  summary: string;
  description: string;
  total_points: number;
  hints: Hint[];
}

export interface Hint {
  text: string;
  cost: number;
}

export interface ChallengeParticipation {
    participation_id: string;
    challenge_id: string;
    user_id: string;
    progress: number;
    status: string;
    rating: number;
    used_hints: number[];
}
