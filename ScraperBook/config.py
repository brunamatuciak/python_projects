BASE_URL = "https://www.darksidebooks.com.br"
GRAPHQL_URL = f"{BASE_URL}/_v/segment/graphql/v1"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "pt-BR,pt;q=0.9",
}

PAGE_SIZE = 12
REQUEST_DELAY_MIN = 1
REQUEST_DELAY_MAX = 3
