import cn from "classnames";

import { useState } from "react";
import { LatLngExpression } from "leaflet";
import { useMapEvents } from "react-leaflet";

import LocationMarker from "@/components/ui/location-marker";
import MapLayout from "@/components/map-layout/Layout";

import useAddLocationMutation from "@/services/location/use-location-mutation";

const MapEvents = ({
  setLocation,
}: {
  setLocation: (location: LatLngExpression) => void;
}) => {
  const [markerPosition, setMarkerPosition] = useState<LatLngExpression>();

  useMapEvents({
    click(e) {
      const { lat, lng } = e.latlng;
      setMarkerPosition([lat, lng]);
      setLocation(e.latlng);
    },
  });

  return markerPosition ? <LocationMarker position={markerPosition} /> : null;
};

function AddUserForm({
  className,
  toggleModal,
}: {
  className?: string;
  toggleModal: () => void;
}) {
  const [location, setLocation] = useState<LatLngExpression>();
  const [locationName, setLocationName] = useState<string>();

  const { mutate: addLocation, isPending } = useAddLocationMutation({
    toggleModal,
  });

  const handleSubmit = (e: any) => {
    e.preventDefault();

    const data: any = { location_name: locationName, ...location };
    addLocation(data);
    console.log("data", data);
  };
  return (
    <form onSubmit={handleSubmit} className={cn(className)}>
      <fieldset>
        <label className="label" htmlFor="categoryName">
          Full Name (required)
        </label>
        <input
          onChange={(e) => setLocationName(e.target.value)}
          className="input"
          type="text"
          placeholder="Enter location name"
        />
      </fieldset>
      <fieldset className="mt-4">
        <MapLayout>
          <MapEvents setLocation={setLocation} />
        </MapLayout>
      </fieldset>
      <button disabled={isPending} className="mt-4 primary-btn title-body">
        Add user {isPending && "..."}
      </button>
    </form>
  );
}

export default AddUserForm;
