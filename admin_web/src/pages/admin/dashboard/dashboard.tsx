import MapComponent from "@/components/map/Map";
import { useSelector } from "react-redux";

function Dashboard() {
  const { user } = useSelector((state: any) => state.user);
  return (
    <>
      <div className="p-4">
        <h1 className="text-xl font-bold">
          Welcome,{user?.fullname || "Tilak"}{" "}
        </h1>
      </div>

      <div className="my-12 px-4 md:px-8 xl:px-12 py-4">
        <MapComponent />
      </div>
    </>
  );
}

export default Dashboard;
