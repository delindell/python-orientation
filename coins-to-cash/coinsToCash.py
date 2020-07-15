def calc_dollars(**coins):
    for (deliniation, amount) in coins.items():
        if deliniation == 'pennies':
           dollar_amount = amount * .01
        elif deliniation == 'nickels':
            dollar_amount += amount * .05
        elif deliniation == 'dimes':
            dollar_amount += amount * .1
        elif deliniation == 'quarters':
            dollar_amount += amount * .25
    print(dollar_amount)

calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)
