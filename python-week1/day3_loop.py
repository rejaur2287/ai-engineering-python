menu = {
    "দুধ চা": 20,
    "রং চা": 10,
    "মালাই চা": 30,
    "আদা চা": 15,
    "লেবু চা": 15,
    "মসলা চা": 20,
    "কফি": 30,
    "সিঙ্গারা": 10,
    "সমুচা": 10,
    "আলুর চপ": 10,
    "কেক": 20,
    "বনরুটি ও কলা": 15,
}

def total_price(item, quantity):
    price = menu[item]
    total = price * quantity
    return total

orders = [
    ("দুধ চা", 25),
    ("রং চা", 15),
    ("সিঙ্গারা", 20),
]

grand_total = 0
for item, qty in orders:
    line_total = total_price(item, qty)
    print(item, qty, line_total)
    grand_total = grand_total + line_total

print("মোট:", grand_total)
