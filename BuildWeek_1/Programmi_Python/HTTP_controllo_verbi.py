import requests
from datetime import datetime
from zoneinfo import ZoneInfo

def check_http_verbs(url, path):
    full_url = url.rstrip("/") + path
    verbs = ["GET", "POST", "PUT", "DELETE", 
             "OPTIONS", "HEAD", "PATCH", "TRACE"]

    print(f"\n{'=' * 55}")
    print(f"  TEST HTTP VERBS")
    print(f"  URL: {full_url}")
    print(f"  Data: {datetime.now(ZoneInfo('Europe/Rome')).strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'=' * 55}")

    abilitati = []
    disabilitati = []

    for verb in verbs:
        try:
            r = requests.request(verb, full_url,
                               timeout=3,
                               allow_redirects=False)
            if r.status_code < 400:
                print(f"  ✅ {verb:10} → {r.status_code} ABILITATO")
                abilitati.append(verb)
            else:
                print(f"  ❌ {verb:10} → {r.status_code} DISABILITATO")
                disabilitati.append(verb)
        except requests.exceptions.ConnectionError:
            print(f"  ⚠️  {verb:10} → CONNESSIONE RIFIUTATA")
        except requests.exceptions.Timeout:
            print(f"  ⚠️  {verb:10} → TIMEOUT")
        except Exception as e:
            print(f"  ⚠️  {verb:10} → ERRORE: {e}")

    print(f"\n{'=' * 55}")
    print(f"  RIEPILOGO:")
    print(f"  Verbi abilitati:    {abilitati}")
    print(f"  Verbi disabilitati: {disabilitati}")
    print(f"{'=' * 55}\n")

if __name__ == "__main__":
    url  = input("URL base (es. http://172.16.0.2/): ").strip()
    path = input("Path (es. /phpmyadmin/ ): ").strip()
    check_http_verbs(url, path) 
