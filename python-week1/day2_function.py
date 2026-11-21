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

print(total_price("দুধ চা", 3))
print(total_price("সিঙ্গারা", 5))
print(total_price("মালাই চা", 2))
