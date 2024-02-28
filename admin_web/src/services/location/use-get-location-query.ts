import { useQuery } from "@tanstack/react-query";

import toast from "react-hot-toast";

import http from "@/lib/http";
import { LocationConfig } from "@/services/api.config";

const getLocationApi = async (): Promise<any> => {
  try {
    const url = LocationConfig.GET_ALL();
    const response = await http(url);
    return response.data;
  } catch (e: any) {
    toast.error(e?.response?.data?.message || "Something went wrong");
    return;
  }
};

const useGetLocationQuery = () => {
  return useQuery({
    queryKey: ["location"],
    queryFn: getLocationApi,
  });
};

export default useGetLocationQuery;
