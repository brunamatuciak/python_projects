# Número de produtos por página
PAGE_SIZE = 20

# URL base do GraphQL da VTEX
BASE_URL = "https://www.darksidebooks.com.br/_v/segment/graphql/v1"

# Headers obrigatórios para GraphQL
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Origin": "https://www.darksidebooks.com.br",
    "Referer": "https://www.darksidebooks.com.br/livros",
    "x-requested-with": "XMLHttpRequest"
}
