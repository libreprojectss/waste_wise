import { Dispatch, SetStateAction } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";

import toast from "react-hot-toast";

import http from "@/lib/http";
import { LocationConfig } from "@/services/api.config";

const addLocationApi = async (data: any) => {
  try {
    // console.log(data);
    const url = LocationConfig.ADD_LOCATION();
    const response = await http.post(url, data);
    console.log("reponse", response);
    return response.data;
  } catch (e: any) {
    toast.error(e?.response?.data?.message || "Something went wrong");
    return;
  }
};

const useAddLocationMutation = ({
  toggleModal,
}: {
  toggleModal: () => void;
}) => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: addLocationApi,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ["location"] });
      toast.success(data?.message || "Location created successful");
      toggleModal();
    },

    onError: (e: any) => {
      toast.error(e?.response?.data?.message || "Something went wrong");
    },
  });
};

export default useAddLocationMutation;
