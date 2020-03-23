export interface ChallengesState {
  challenges: Challenge[];
}

export interface Challenge {
  challenge_id: string;
  title: string;
  title_slug: string;
  category_id: string;
  summary: string;
  description: string;
  total_points: number;
  flags: Flag[];
  hints: Hint[];
  containers: object;
  challenge_type: string;
  created_at: number;
  updated_at: number;
}

export interface Hint {
  text: string;
  cost: number;
}

export interface Flag {
  secret: string;
  reward: number;
  text: string;
}

export interface Port {
  name: string;
  port: number;
}
