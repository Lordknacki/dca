import os
import json
import requests
from datetime import datetime, timezone

ALLTICK_TOKEN = os.getenv("ALLTICK_TOKEN")
ALLTICK_URL = "https://quote.alltick.io/quote-stock-b-api/trade-tick"
FX_URL = "https://api.frankfurter.app/latest?from=HKD&to=EUR"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json",
}

def get_xiaomi_hkd():
    if not ALLTICK_TOKEN:
        raise RuntimeError("ALLTICK_TOKEN manquant (secret GitHub non défini).")

    # D’après leur doc, on envoie un JSON dans query=...
    query = {
        "data": {
            "code": "01810.HK"  # Code HKEX de Xiaomi chez eux
        }
    }

    params = {
        "token": ALLTICK_TOKEN,
        "query": json.dumps(query, separators=(",", ":"))
    }

    r = requests.get(ALLTICK_URL, params=params, headers=HEADERS, timeout=15)
    print("AllTick status:", r.status_code)
    print("AllTick body preview:", r.text[:300].replace("\n", " "))

    data = r.json()

    # La structure exacte peut varier un peu, mais en général :
    # {
    #   "code":0,
    #   "msg":"success",
    #   "data":[{"code":"01810.HK","last_price":..., "last_time": ...}, ...]
    # }
    if data.get("code") != 0 or "data" not in data or not data["data"]:
        raise RuntimeError(f"Données AllTick introuvables ou erreur : {data}")

    tick = data["data"][0]
    price_hkd = tick.get("last_price")
    last_time = tick.get("last_time")  # souvent timestamp en ms ou s

    if price_hkd is None:
        raise RuntimeError(f"Prix HKD introuvable : {tick}")

    # On normalise l’heure si possible, sinon on la laisse brute
    if isinstance(last_time, (int, float)):
        # supposons un timestamp en secondes ou ms
        if last_time > 10_000_000_000:  # heuristique ms vs s
            last_dt = datetime.fromtimestamp(last_time / 1000, tz=timezone.utc)
        else:
            last_dt = datetime.fromtimestamp(last_time, tz=timezone.utc)
        last_iso = last_dt.isoformat()
    else:
        last_iso = str(last_time) if last_time is not None else None

    # On n’a pas forcément le change HKD ni le % dans la même réponse, donc on laisse None
    change_hkd = tick.get("change")  # si présent
    change_pct = tick.get("change_ratio")  # si présent en %

    return float(price_hkd), change_hkd, change_pct, last_iso

def get_hkd_to_eur():
    r = requests.get(FX_URL, headers=HEADERS, timeout=15)
    print("FX status:", r.status_code)
    print("FX body preview:", r.text[:200].replace("\n", " "))
    data = r.json()
    return float(data["rates"]["EUR"])

def main():
    price_hkd, change_hkd, change_pct, last_time = get_xiaomi_hkd()
    rate_hkd_eur = get_hkd_to_eur()
    price_eur = price_hkd * rate_hkd_eur

    payload = {
        "symbol": "01810.HK",
        "price_hkd": price_hkd,
        "price_eur": price_eur,
        "change_hkd": change_hkd,
        "change_percent": change_pct,
        "last_trading_time": last_time,
        "rate_hkd_eur": rate_hkd_eur,
        "generated_at_utc": datetime.now(timezone.utc).isoformat()
    }

    with open("xiaomi.json", "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print("xiaomi.json mis à jour :", payload)

if __name__ == "__main__":
    main()
