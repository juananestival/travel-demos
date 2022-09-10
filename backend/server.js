import express from "express";
import dotenv from "dotenv";
import productRoutes from './routes/productRoutes.js'
import webhookEmulator from './routes/webHookEmulator.js'
import colors from "colors";
import bodyParser from "body-parser";


//config
dotenv.config();
const PORT = process.env.PORT || 8000;
const app = express();

app.use(bodyParser.urlencoded({
    extended: true
  }));
app.use(bodyParser.json());
//routes
app.get("/", (req, res) => {
    res.send("API is runing");
});

app.use('/api/products', productRoutes)
app.use('/api/wh', webhookEmulator)




//execute
app.listen(
    PORT,
    console.log(
      `server runing in ${process.env.NODE_ENV}mode on port ${PORT}.`.yellow.bold
    )
);

console.log('Server...')
