import axios from "axios";

export async function fetchPrice(symbol) {
  const url = `https://api.binance.com/api/v3/ticker/price?symbol=${symbol}`;
  const response = await axios.get(url);
  return parseFloat(response.data.price);
}
