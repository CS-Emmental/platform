export interface ChallengesState {
  challenges: Challenge[];
}

export interface Challenge {
  challenge_id: string;
  title: string;
  category_id: string;
  summary: string;
  description: string;
  total_points: number;
  flags: Flag[];
  hints: Hint[];
  image: string;
  ports: Port[];
  challenge_type: string;
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
