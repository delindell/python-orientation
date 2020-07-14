def chicken_monkey():
    for num in range(1, 101):
      if num % 5 == 0 and num % 7 == 0:
        print('ChickenMonkey', num) 
      elif num % 5 == 0:
        print('Chicken', num)
      elif num % 7 == 0:
        print('Monkey', num)

chicken_monkey()

def run(*kids):
    for child in kids:
        print(f'{child} ran like a fool!')

run('Pam', 'Sam', 'Andrea', 'Will')

def swing(*kids):
    for child in kids:
        print(f'{child} swung like a maniac!')

swing('Marybeth', 'Ariel', 'Kevin', 'Courtney')

def slide(*kids):
    for child in kids:
        print(f'{child} slid down that slide like a mug!')

slide('Mike', 'Jack', 'Jennifer', 'Earl')

def hide_and_seek(*kids):
    for child in kids:
        print(f'{child} is terrible at hide and seek!')

hide_and_seek('Henry', 'Heather', 'Hayley', 'Hugh')
