export interface ChallengesState {
  challengeCategories: ChallengeCategory[];
  challenges: Challenge[];
}

export interface ChallengeCategory {
  title: string;
  kebab: string;
  category_id: string;
  icon: string;
  description: string;
}

export interface Challenge {
  title: string;
  kebab: string;
  category_id: string;
  icon: string;
  description: string;
  challengesCount: number;
}
