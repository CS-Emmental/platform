export interface ChallengeParticipationsState {
  currentuserPartipations: ChallengeParticipation[];
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
