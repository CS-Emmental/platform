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
  value: string;
  reward: number;
  text: string;
}

export interface Port {
  name: string;
  port: number;
}

export interface ChallengeParticipation {
    participation_id: string;
    challenge_id: string;
    user_id: string;
    status: string;
    rating: number;
    found_flags: number[];
    used_hints: number[];
    port: number;
}
