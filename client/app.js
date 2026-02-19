const socket = new WebSocket("ws://localhost:3000");

socket.onmessage = function(event) {
  const data = JSON.parse(event.data);

  const alertDiv = document.createElement("div");
  alertDiv.className = "alert";

  alertDiv.innerHTML = `
    ⚠️ ${data.symbol} dropped ${data.change}% <br>
    Current price: ${data.currentPrice}
  `;

  document.getElementById("alerts").appendChild(alertDiv);

  // Son alerte
  const audio = new Audio("https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg");
  audio.play();
};
