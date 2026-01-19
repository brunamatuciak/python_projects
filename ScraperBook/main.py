from services.vtex_client import graphql_request
from utils.logger import info
from utils.saver import save_json

def main():
    info("Scraper iniciado")
    data = {"status": "estrutura ok"}
    save_json(data)
    info("Scraper finalizado")

if __name__ == "__main__":
    main()
