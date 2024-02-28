import express from 'express'
import LocationController from "../controllers/locations.js";

const router=express.Router()

const locationControllerObj=new LocationController()
router.get("/api/v1/locations",locationControllerObj.getAll)
router.post("/api/v1/locations/add",locationControllerObj.create)


export default router