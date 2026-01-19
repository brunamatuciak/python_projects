import json
from pathlib import Path

def save_json(data, filename="data/products.json"):
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Arquivo salvo em {path}")
