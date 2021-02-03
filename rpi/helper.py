def drinkZuordnung(value):
    switcher = {
        0: "Sex on the Beach",
        1: "Gin Tonic",
        2: "Blue Lagoon",
        3: "Flying Hirsch",
        4: "Vodka E",
        5: "HemingWay",
        6: "Blue Gin Tonic",
        7: "Strong Red",
        8: "No Sex on the Beach",
        9: "Blue Lagoon alkfree",
    }
    return switcher.get(value, print("Invalid value! Has to be int 0-9!"))

def zahlZuordnung(stringvalue):
      switcher = {
        "Sex on the Beach": 0,
        "Gin Tonic": 1,
        "Blue Lagoon": 2,
        "Flying Hirsch": 3,
        "Vodka E": 4,
        "HemingWay": 5,
        "Blue Gin Tonic": 6,
        "Strong Red": 7,
        "No Sex on the Beach": 8,
        "Blue Lagoon alkfree": 9,
    }
    return switcher.get(stringvalue, print("Invalid value! Has to be a string!"))