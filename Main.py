print('Welcome to Recipe Generator')

ingredients = []

while True:
    ingredient = input("Enter ingredient: ")

    if ingredient == '0':
        break
    ingredients.append(ingredient)

print(ingredients)