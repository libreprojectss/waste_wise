import mongoose from "mongoose";

const connectDB= async()=>{
    const mongo_url=process.env.MONGO_URL
    try{
        await mongoose.connect(mongo_url).then((res)=>{
            console.log("Db connected",res.connection.host);
        })
        .catch((err)=>{
            console.log("Error to connect to db",err)
        })
    }
    catch(err){
        console.log("Database connection error",err)
    }

}
export default connectDB