import { Dispatch, SetStateAction } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";

import toast from "react-hot-toast";

import http from "@/lib/http";
import { LocationConfig } from "@/services/api.config";

const addLocationApi = async ({ data }: { data: FormData }) => {
  try {
    const url = LocationConfig.ADD_LOCATION();
    const response = await http.post(url, data);
    console.log("reponse", response);
    return response.data;

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
  } catch (e: any) {
    toast.error(e?.response?.data?.message || "Something went wrong");
    return;
  }
};

const useAddLocationMutation = ({
  reset,
  toggleModal,
}: {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  reset: any;
  toggleModal: () => void;
  setImage: Dispatch<SetStateAction<File | null>>;
}) => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: addLocationApi,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ["location"] });
      reset();
      toggleModal();
      toast.success(data?.message || "Location successfully added");
    },
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    onError: (e: any) => {
      toast.error(e?.response?.data?.message || "Something went wrong");
    },
  });
};

export default useAddLocationMutation;
