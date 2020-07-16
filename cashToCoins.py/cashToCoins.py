import math

def cash_to_coins():
    dollar_amount = 8.69

    piggy_bank = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }

    piggy_bank["quarters"] = math.floor(dollar_amount / .25)
    dollar_amount = dollar_amount % .25
    piggy_bank["dimes"] = math.floor(dollar_amount / .10)
    dollar_amount = dollar_amount % .10
    piggy_bank["nickels"] = math.floor(dollar_amount / .05)
    dollar_amount = dollar_amount % .05
    piggy_bank["pennies"] = math.floor(dollar_amount / .01)
    dollar_amount = dollar_amount % .01

    print(piggy_bank)

cash_to_coins()
