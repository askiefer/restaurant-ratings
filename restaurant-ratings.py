import sys

filename = sys.argv[1]

from random import choice

def print_restaurant_ratings(filename):
    """This prints restaurant ratings from a file."""

    with open(filename) as in_file:
        # asks user for their name
        user_name = raw_input("Hello! What is your name? ")

        #initializes a list and asks user to add a restaurant and score to it
        restaurants = {}
        #restaurant_name = raw_input("What restaurant would you like to review? ")
        #restaurant_score = raw_input("What score do you give this restaurant? ")
        #restaurants.append((restaurant_name, int(restaurant_score)))

        # iterates through each line and splits at colon then inputs it into dict
        for line in in_file:
            # gets rid of newline character at end of line
            line = line.rstrip()
            # makes a list from file line: ["Restaurant Name", score]
            restaurant_and_rating = line.split(":")
            # adds a tuple of name and rating to a list of all restaurants
            restaurants[restaurant_and_rating[0]] = restaurant_and_rating[1]
        
        # chooses a random restaurant and unpacks name and score from tuple
        # random_restaurant = choice(restaurants)
        # rand_rest_name = random_restaurant[0]
        # rand_rest_score = random_restaurant[1]

        # # tells user current rating and asks for a new one
        # print "Hello, %s! %s has a rating of %s." %(user_name, rand_rest_name, rand_rest_score)
        # new_score = int(raw_input("What rating would you give %s?" %(rand_rest_name)))

        # # updates restaurant rating
        # for item in restaurants:
        #     # Item[0] is restaurant tuple, item[0][0] is restaurant name, item[0][1] is score
        #     if item[0] == rand_rest_name:
        #         del restaurants[restaurants.index(item)]

        # restaurants.append((rand_rest_name, new_score))

        # sorts list alphabetically
        rest_list = sorted(restaurants)
        # prints each tuple of name and rating on a new line
        for key in rest_list:
            print key, "has a rating of:", restaurants[key]



print_restaurant_ratings(filename)

