import vine from "@vinejs/vine";
import Base_Validator from "./base_validator.js";

class LocationValidator extends Base_Validator {
  constructor() {
    super();

    this.schema = vine.object({
      location_name: vine.string(),
      lat: vine.number(),
      long: vine.number(),
    });
  }
}

export default LocationValidator;
