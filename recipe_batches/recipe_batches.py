#!/usr/bin/python

import math

# loop over both dictionaries
# compare values for each between the two
# find out how many times the left goes into the right for each value
# get the smallest amount of possible combinations for one ingredient out of all of them


def recipe_batches(recipe, ingredients):
    if set(recipe) == set(ingredients):
        amounts = []
        for key in recipe:
            amounts.append(ingredients[key] // recipe[key])
            print("amounts", amounts)
        return min(amounts)
    else:
        return 0


# if __name__ == "__main__":
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {"milk": 100, "butter": 50, "flour": 5}
#     ingredients = {"milk": 132, "butter": 48, "flour": 51}
#     print(
#         "{batches} batches can be made from the available ingredients: {ingredients}.".format(
#             batches=recipe_batches(recipe, ingredients), ingredients=ingredients
#         )
#     )
