my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    },
      "dad": {
      "name": "Larry",
      "age": 65
    },
      "brother": {
      "name": "Brian",
      "age": 25
    }
}

for family_member, member_details in my_family.items():
    print(f'{member_details["name"]} is my {family_member} and is {member_details["age"]}')
