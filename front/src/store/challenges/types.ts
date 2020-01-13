export interface ChallengesState {
  challengeCategories: ChallengeCategory[];
}

export interface ChallengeCategory {
  title: string;
  kebab: string;
  category_id: string;
  icon: string;
  description: string;
  challengesCount: number;
}
