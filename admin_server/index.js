import express from "express";
import dotenv from "dotenv";
import cors from "cors";
import bodyParser from "body-parser";
// import cookieParser from "cookie-parser"
import { formatResponse } from "./api/middlewares/parse_response.js";
import router from "./api/routes/all_routes.js";
import connectDB from "./config/mongo.js";
const app = express();

app.use(
  cors({
    origin: [
      "http://127.0.0.1:3000",
      "http://localhost:3000",
      "http://localhost:5173",
    ],
    credentials: true,
  })
);

app.use(express.static("public"));

app.use(bodyParser.json());
app.use(express.urlencoded({ extended: true }));

dotenv.config();

app.use(formatResponse);
connectDB();
// app.use("", Routes)

app.use("", router);

app.listen(8000, () => {
  console.log("Server is running on ", 8000);
});

export default app;
