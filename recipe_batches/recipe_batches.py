#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  if len(recipe) > len(ingredients):
    return 0
  for key in recipe:
    if ingredients[key] < recipe[key]:
      return 0
    else:
      placeholder = ingredients[key] // recipe[key]
      batches.append(placeholder)
  
  return min(batches) 

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))