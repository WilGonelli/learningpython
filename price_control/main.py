import json
from pathlib import Path
from datetime import date

dados = []
FILE = Path("items.json")

def open_file(file):
    if not file.exists():
        return {}
    
    if file.stat().st_size == 0:
        return {}
    
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def get_items(dados):
    item = input("digite o item: ").lower()
    value = float(input("digite o valor: "))
    hoje = date.today().isoformat()
    
    if item not in dados:
        dados[item] = []
    
    dados[item].append({
        "data":hoje,
        "value": value
    })
    
    price_compare(dados, item)
    

def save_items(dados):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def price_compare(dados, item):
    item_list = dados[item]
    if len(item_list) == 1:       
        print(f"primeiro registro do item {item} com valor de R${item_list[0]["value"]:.2f}")
        return
    
    last_value = item_list[-2]["value"]
    new_value = item_list[-1]["value"]
    
    dif = (((new_value - last_value) / last_value) * 100)
    if dif < 0:
        print(f"o produto {item} teve uma diminuição de {dif:.2f}% em relação a ultima vez comprada")
    else:    
        print(f"o produto {item} teve um aumento de {dif:.2f}% em relação a ultima vez comprada")
    
def control():
    dados = open_file(FILE)    
    get_items(dados)
    save_items(dados)
    

if __name__ == "__main__":
    control()