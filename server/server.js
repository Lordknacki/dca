import express from "express";
import cors from "cors";
import { WebSocketServer } from "ws";
import { SYMBOLS, CHECK_INTERVAL } from "./config.js";
import { fetchPrice } from "./priceService.js";
import { updateHistory, checkAlert } from "./alertEngine.js";

const app = express();
app.use(cors());

const server = app.listen(3000, () =>
  console.log("Server running on port 3000")
);

const wss = new WebSocketServer({ server });

wss.on("connection", ws => {
  console.log("Client connected");
});

async function monitor() {
  for (const asset of SYMBOLS) {
    try {
      const price = await fetchPrice(asset.symbol);

      updateHistory(asset.symbol, price);

      const alert = checkAlert(asset.symbol);

      if (alert) {
        wss.clients.forEach(client => {
          client.send(JSON.stringify(alert));
        });
      }

    } catch (error) {
      console.error("Error fetching", asset.symbol);
    }
  }
}

setInterval(monitor, CHECK_INTERVAL);
