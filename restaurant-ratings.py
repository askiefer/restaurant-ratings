import sys

filename = sys.argv[1]

def print_restaurant_ratings(filename):
    """This prints restaurant ratings from a file."""

    with open(filename) as in_file:

        restaurants = []

        # iterates through each line and splits at colon then inputs it into dict
        
        for line in in_file: 
            # ["Restaurant Name", score]
            restaurant_and_rating = line.split(":")
            restaurants.append( (restaurant_and_rating[0], restaurant_and_rating[1][0]) )
        
        restaurants = sorted(restaurants)
        
        for item in restaurants:
            print item[0], "has a rating of:", item[1]



print_restaurant_ratings(filename)

