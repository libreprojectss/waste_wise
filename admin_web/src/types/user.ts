export interface IUser {
  id: number;
  createdAt: string;
  updatedAt: string;
  name: string;
  isVerified: boolean;
  email: string;
}

export interface IUserState {
  user: IUser | null;
  loginStatus: boolean;
}
