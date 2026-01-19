from services.vtex_client import fetch_all_books
from utils.saver import save_json

def main():
    print("Iniciando scraping da listagem de livros...")
    books = fetch_all_books()
    save_json(books)
    print(f"Total de livros salvos: {len(books)}")

if __name__ == "__main__":
    main()
