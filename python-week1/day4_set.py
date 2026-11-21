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
    return menu[item] * quantity

orders = [
    ("দুধ চা", 25),
    ("রং চা", 15),
    ("সিঙ্গারা", 20),
    ("দুধ চা", 10),
    ("রং চা", 5),
]

items_sold = set()
for item, qty in orders:
    items_sold.add(item)

print("আজ বিক্রি হয়েছে:", items_sold)
print("মোট item ধরন:", len(items_sold))

totals = {}
for item, qty in orders:
    if item in totals:
        totals[item] = totals[item] + total_price(item, qty)
    else:
        totals[item] = total_price(item, qty)

for item, taka in totals.items():
    print(item, taka)

print("সর্বমোট:", sum(totals.values()))
