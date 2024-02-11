import { useState } from "react";
import { MapContainer, Marker, TileLayer } from "react-leaflet";
import L, { MarkerCluster } from "leaflet";
import MarkerClusterGroup from "react-leaflet-cluster";
import logo from "@/assets/location.svg";
import "@/App.css";
import "leaflet/dist/leaflet.css";

const customIcon = new L.Icon({
  iconUrl: logo,
  iconSize: new L.Point(40, 47),
});

// NOTE: iconCreateFunction is running by leaflet, which is not support ES6 arrow func syntax
// eslint-disable-next-line
const createClusterCustomIcon = function (cluster: MarkerCluster) {
  return L.divIcon({
    html: `<span>${cluster.getChildCount()}</span>`,
    className: "custom-marker-cluster",
    iconSize: L.point(33, 33, true),
  });
};

function MapComponent() {
  const [dynamicPosition, setPosition] = useState<L.LatLngExpression>([
    28.051687, 83.987261,
  ]);
  return (
    <>
      <MapContainer
        className="leaflet-container"
        center={[28.2613485, 83.9721112]}
        zoom={4}
        scrollWheelZoom={true}
      >
        <TileLayer
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <MarkerClusterGroup
          onClick={(e) => console.log("onClick", e)}
          iconCreateFunction={createClusterCustomIcon}
          maxClusterRadius={150}
          spiderfyOnMaxZoom={true}
          polygonOptions={{
            fillColor: "#ffffff",
            color: "#f00800",
            weight: 5,
            opacity: 1,
            fillOpacity: 0.8,
          }}
          showCoverageOnHover={true}
        >
          <Marker position={[28.668754, 83.104185]} icon={customIcon} />
          <Marker position={[29.587613, 83.944535]} icon={customIcon} />
          <Marker position={[28.614681, 83.121517]} icon={customIcon} />
          <Marker position={[29.357641, 83.328708]} icon={customIcon} />
          <Marker
            position={dynamicPosition}
            title="a title  as asd2"
            icon={customIcon}
          />
          <Marker position={[28.931841, 83.876713]} icon={customIcon} />
        </MarkerClusterGroup>
      </MapContainer>
    </>
  );
}

export default MapComponent;
