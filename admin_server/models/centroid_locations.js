import mongoose from "mongoose";

const LocationSchema = new mongoose.Schema({
  location_name: {
    type: String,
    required: true,
  },
  lat: {
    type: Number,
    required: true,
  },
  lng: {
    type: Number,
    required: true,
  },
});

export default mongoose.model("Locations", LocationSchema);
