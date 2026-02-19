import { DROP_THRESHOLD } from "./config.js";

const history = {};

export function updateHistory(symbol, price) {
  if (!history[symbol]) history[symbol] = [];

  history[symbol].push({
    price,
    time: Date.now()
  });

  // garder seulement 15 minutes
  history[symbol] = history[symbol].filter(
    entry => Date.now() - entry.time <= 15 * 60 * 1000
  );
}

export function checkAlert(symbol) {
  const data = history[symbol];
  if (!data || data.length < 2) return null;

  const firstPrice = data[0].price;
  const lastPrice = data[data.length - 1].price;

  const changePercent = ((lastPrice - firstPrice) / firstPrice) * 100;

  if (changePercent <= DROP_THRESHOLD) {
    return {
      symbol,
      change: changePercent.toFixed(2),
      currentPrice: lastPrice
    };
  }

  return null;
}
