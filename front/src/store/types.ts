export interface RootState {
  version: string;
  currentUser?: User;
  isAuthenticated: boolean;
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
