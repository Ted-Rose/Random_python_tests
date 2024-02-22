""" Test how format method performs."""
item = {"amount": ""}

for k, v in item.items():
    if k == "amount":
        amount = item["amount"]
        amount = str('{:.2f}'.format(float(amount)))
        if amount != "":
            print("Here amount is an empty string")