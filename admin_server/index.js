import express from "express"
import dotenv from "dotenv"
import cors from "cors"
// import cookieParser from "cookie-parser"
import { formatResponse } from "./middlewares/parsers/parseResponse.js"
const app = express()
app.use(
	session({
	  secret:"BluestoneSecretKey",
	  resave: false,
	  saveUninitialized: true,
	})
  );
app.use(
	cors({
		origin: [
			"http://127.0.0.1:3000",
			"http://localhost:3000",
		],
		credentials: true,
	})
)

app.use(express.static('public'));


app.use(express.json({ limit: "10mb" }))
app.use(express.urlencoded({ extended: true }))

dotenv.config()


app.use(formatResponse)
// app.use("", Routes) 

app.listen(process.env.PORT, () => {
	console.log("Server is running on port :", process.env.PORT)
})

export default app
