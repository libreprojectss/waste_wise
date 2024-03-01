import { number } from "yup";

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

export interface Ilocation {
  lat: number;
  lng: number;
}
