import { useQuery } from "@tanstack/react-query";

import toast from "react-hot-toast";

import http from "@/lib/http";
import { LocationConfig } from "@/services/api.config";

const getLocationApi = async () => {
  try {
    const url = LocationConfig.GET_ALL();
    const response = await http(url);
    return response.data.categories;

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
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
