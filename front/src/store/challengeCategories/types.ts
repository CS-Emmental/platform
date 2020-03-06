export interface ChallengeCategoriesState {
  challengeCategories: ChallengeCategory[];
}

export interface ChallengeCategory {
  title: string;
  title_slug: string;
  category_id: string;
  icon: string;
  description: string;
}
