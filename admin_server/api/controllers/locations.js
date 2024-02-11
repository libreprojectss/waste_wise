import Joi from "joi";
import centroid_locations from "../../models/centroid_locations.js";
import location_validator from "../validators/location_validator.js";


class LocationController{
    constructor(){
        this.model=centroid_locations
        this.validator=new location_validator()
    }

    getAll=async(req,res)=>{
        console.log("Fetching locations")
        const locations=await this.model.find()
        return res.apiSuccess("Locations fetched sucessfully",locations,200)
    }

    create=async(req,res)=>{
        const body_data=req.body
        try{
        try{
            console.log(body_data)
            await this.validator.validate(body_data)
        }
        catch(err){
            return res.apiError(err.message,400)
        }
        const locations=await this.model.create(body_data)
        return res.apiSuccess("Location created sucessful",locations)
    }
        catch(err){
            return res.apiError("Something went wrong",500)
        }
    }
}

export default LocationController