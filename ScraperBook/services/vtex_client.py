# services/vtex_scraper.py

from playwright.sync_api import sync_playwright

def fetch_all_books(base_url="https://www.darksidebooks.com.br/livros"):
    """
    Faz scraping de todos os livros da listagem da DarkSideBooks usando Playwright.
    Retorna uma lista de dicionários com: nome, título, link e imagem.
    """

    books = []

    with sync_playwright() as p:
        # Abre o navegador Chromium em headless (sem abrir janela)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Vai para a página principal de livros
        page.goto(base_url)
        page.wait_for_selector("div.vtex-product-summary-2-x-container")  # Espera produtos carregarem

        # Scroll infinito para garantir que todos os produtos carreguem
        last_height = page.evaluate("() => document.body.scrollHeight")
        while True:
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1000)  # espera carregar mais produtos
            new_height = page.evaluate("() => document.body.scrollHeight")
            if new_height == last_height:
                break  # chegou ao fim da página
            last_height = new_height

        # Seleciona todos os cards de produtos
        product_elements = page.query_selector_all("div.vtex-product-summary-2-x-container")

        for el in product_elements:
            # Pega dados de cada produto
            name = el.query_selector("span.vtex-product-summary-2-x-productBrand").inner_text() if el.query_selector("span.vtex-product-summary-2-x-productBrand") else ""
            title = el.query_selector("span.vtex-product-summary-2-x-productBrand + span").inner_text() if el.query_selector("span.vtex-product-summary-2-x-productBrand + span") else ""
            image = el.query_selector("img").get_attribute("src") if el.query_selector("img") else ""
            link = el.query_selector("a.vtex-product-summary-2-x-clearLink").get_attribute("href") if el.query_selector("a.vtex-product-summary-2-x-clearLink") else ""

            books.append({
                "name": name.strip(),
                "title": title.strip(),
                "image": image,
                "link": f"https://www.darksidebooks.com.br{link}" if link else ""
            })

        browser.close()

    return books
