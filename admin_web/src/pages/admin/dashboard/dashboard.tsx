import { useSelector } from "react-redux";

import MapComponent from "@/components/map-layout/Layout";
import useGetLocationQuery from "@/services/location/use-get-location-query";
import MapLayout from "@/components/map-layout/Layout";

function Dashboard() {
  const { user } = useSelector((state: any) => state.user);
  // const { data: locationData, isLoading } = useGetLocationQuery();
  // console.log("response", locationData);

  return (
    <>
      <div className="p-4">
        <h1 className="text-xl font-bold">
          Welcome,{user?.fullname || "Tilak"}{" "}
        </h1>
      </div>

      <div className="my-12 px-4 md:px-8 xl:px-12 py-4">
        <MapLayout>
          <div>hell</div>
        </MapLayout>
      </div>
    </>
  );
}

export default Dashboard;
