import { Marker, Popup } from "react-leaflet";
import { LatLngExpression } from "leaflet";

interface LocationMarkerProps {
  position: LatLngExpression;
}

const LocationMarker: React.FC<LocationMarkerProps> = ({ position }) => {
  return (
    <Marker position={position || [28.25, 81.95]}>
      <Popup>
        <p>Location:{position?.toString()}</p>
      </Popup>
    </Marker>
  );
};

export default LocationMarker;
