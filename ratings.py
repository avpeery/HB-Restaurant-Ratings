"""Restaurant rating lister."""

def creates_dictionary(filename):
    restaurant_dictionary = {}
    given_file = open(filename)
    for line in given_file:
        line = line.rstrip()
        words = line.split(":")
        restaurant_dictionary[words[0]] = words[1]
    return restaurant_dictionary


def prints_ratings_alphabetically(given_dictionary):
    restaurants = sorted(given_dictionary)
    for restaurant in restaurants:
        print(f"{restaurant} is rated at {given_dictionary[restaurant]}.")

prints_ratings_alphabetically(creates_dictionary("scores.txt"))