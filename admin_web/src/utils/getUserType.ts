import { RootState } from "@/redux/store";
import { useSelector } from "react-redux";

export const getUserType = () => {
  // const role = useSelector<RootState>((state) => state.user?.loginStatus);
  return "ADMIN";
};
