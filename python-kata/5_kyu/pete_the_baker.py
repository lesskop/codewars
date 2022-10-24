# https://www.codewars.com/kata/525c65e51bf619685c000059

def pete_has_needed_ingredients(recipe: dict, pete_has: dict) -> bool:
    for ingredient in recipe.keys():
        if ingredient not in pete_has.keys():
            return False

    return True


def cakes(recipe: dict, pete_has: dict) -> int:
    cakes_num = 100500  # bad implementation, but I don't think that Pete wants to make 100500+ cakes :)

    if not pete_has_needed_ingredients(recipe, pete_has):
        return 0

    for pete_ingredient, pete_quantity in pete_has.items():
        for recipe_ingredient, recipe_quantity in recipe.items():
            if pete_ingredient == recipe_ingredient:
                temp_cakes_num = pete_quantity // recipe_quantity
                if temp_cakes_num < cakes_num:
                    cakes_num = temp_cakes_num

    return cakes_num


print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1},
            {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))

print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100},
            {'sugar': 500, 'flour': 2000, 'milk': 2000}))


# It was so easy :(
# def cakes(recipe, available):
#     return min(available.get(k, 0) / recipe[k] for k in recipe)
