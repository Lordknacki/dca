<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <title>Cours Xiaomi 1810.HK</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background: #000;
      color: #f5f5f5;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .card {
      background: #000;
      border-radius: 16px;
      border: 1px solid #333;
      padding: 10px;
      width: 100%;
      max-width: 420px;
    }

    .title {
      font-size: 16px;
      text-align: center;
      margin-bottom: 6px;
      opacity: 0.8;
    }

    .ticker {
      font-size: 20px;
      text-align: center;
      margin-bottom: 8px;
      letter-spacing: 2px;
    }

    /* Le conteneur TradingView doit juste prendre toute la largeur */
    .tv-wrap {
      width: 100%;
      height: 260px; /* tu peux ajuster selon ton écran */
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="title">Cours en direct</div>
    <div class="ticker">XIAOMI • 1810.HK</div>

    <div class="tv-wrap">
      <!-- Widget TradingView mini overview -->
      <div class="tradingview-widget-container">
        <div class="tradingview-widget-container__widget"></div>
        <script type="text/javascript"
          src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
{
  "symbol": "HKEX:1810",
  "width": "100%",
  "height": "100%",
  "locale": "fr",
  "dateRange": "1D",
  "colorTheme": "dark",
  "isTransparent": true,
  "autosize": true,
  "hideDateRanges": true,
  "hideMarketStatus": false,
  "hideSymbolLogo": false,
  "scalePosition": "right",
  "scaleMode": "Normal",
  "fontFamily": "Trebuchet MS, sans-serif",
  "fontSize": "12",
  "noTimeScale": false,
  "chartType": "candlesticks",
  "lineWidth": 2,
  "timeFrames": [],
  "upColor": "#26a69a",
  "downColor": "#ef5350",
  "borderUpColor": "#26a69a",
  "borderDownColor": "#ef5350",
  "wickUpColor": "#26a69a",
  "wickDownColor": "#ef5350"
}
        </script>
      </div>
    </div>
  </div>
</body>
</html>
