export interface ChallengesState {
  challengeCategories: ChallengeCategory[];
  challenges: Challenge[];
}

export interface ChallengeCategory {
  title: string;
  slug: string;
  category_id: string;
  icon: string;
  description: string;
}

export interface Challenge {
  challenge_id: string;
  title: string;
  slug: string;
  category_id: string;
  icon: string;
  summary: string;
  description: string;
  total_points: number;
}
