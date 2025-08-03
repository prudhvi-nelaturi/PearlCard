FARE_RULES = {
    (1, 1): 40,
    (1, 2): 55, (2, 1): 55,
    (1, 3): 65, (3, 1): 65,
    (2, 2): 35,
    (2, 3): 45, (3, 2): 45,
    (3, 3): 30,
}

def calculate_fare(from_zone, to_zone):
    return FARE_RULES.get((from_zone, to_zone), 0)
