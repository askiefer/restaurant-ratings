import sys

filename = sys.argv[1]

def print_restaurant_ratings(filename):
    """This prints restaurant ratings from a file."""

    with open(filename) as in_file:

        restaurants = []

        # iterates through each line and splits at colon then inputs it into dict
        
        for line in in_file: 
            # gets rid of newline character at end of line
            line = line.rstrip()
            # makes a list from file line: ["Restaurant Name", score]
            restaurant_and_rating = line.split(":")
            # adds a tuple of name and rating to a list of all restaurants
            restaurants.append((restaurant_and_rating[0], restaurant_and_rating[1]))
        
        # sorts list alphabetically
        restaurants = sorted(restaurants)
        # prints each tuple of name and rating on a new line
        for item in restaurants:
            print item[0], "has a rating of:", item[1]



print_restaurant_ratings(filename)

