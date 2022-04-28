from math import ceil
from sys import float_info, maxsize
import json

from Ingredients import ingredients, Ingredient
from RecipeLoader import SandwichRecipe


def calculate_best_packet_size(num_sandwiches: int, ingredient_name: str, ingredient_quantity_per_sandwich: int):
    total_ingredient_quantity = ingredient_quantity_per_sandwich * num_sandwiches

    best_packet_index = 0
    best_packet_cost = float_info.max
    i = 0
    for ingredient in ingredients[ingredient_name]:
        required_packs = ceil(total_ingredient_quantity / ingredient.quantity_per_pack)
        total_cost = required_packs * ingredient.cost
        if total_cost < best_packet_cost:
            best_packet_cost = total_cost
            best_packet_index = i
        i += 1

    return best_packet_index, best_packet_cost


def calculate_optimum_sandwich_counts(min_sandwiches: int,
                                      max_sandwiches: int,
                                      desired_sandwiches: set[SandwichRecipe]):
    cost_per_sandwich = {}
    for sandwich in desired_sandwiches:
        for sandwich_count in range(min_sandwiches, max_sandwiches + 1):

            total_cost = 0

            for (sandwich_component, quantity_required) in sandwich.components.items():
                index, cost = calculate_best_packet_size(sandwich_count, sandwich_component, quantity_required)
                total_cost += cost

            cost_per_sandwich[sandwich_count] = total_cost / sandwich_count

        print("Optimum sandwich quantities for %s are:" % sandwich.name)
        last_minimum = maxsize
        for i in range(min_sandwiches, max_sandwiches):
            cost_a = cost_per_sandwich[i]
            cost_b = cost_per_sandwich[i + 1]

            if (cost_b > cost_a) and (cost_a < last_minimum):
                last_minimum = cost_a
                print("\t%.2i = £%.2f per sandwich" % (i, cost_a / 100.0))

        print()


def main():
    chicken_sweetcorn = SandwichRecipe(
        "Chicken and Sweetcorn",
        {
            "White Bread": 2,
            "Chicken Breast": 56,
            "Sweetcorn": 35,
            "Mayonnaise": 23,
        }
    )

    smoked_ham_and_cheddar = SandwichRecipe(
        "Smoked Ham and Cheddar",
        {
            "Wholemeal Bread": 2,
            "Smoked Ham": 44,
            "Medium Cheddar": 30,
            "Mayonnaise": 23
        }
    )

    tuna_mayo = SandwichRecipe(
        "Tuna Mayo",
        {
            "Wholemeal Bread": 2,
            "Tuna": 41,
            "Mayonnaise": 29
        }
    )

    beef_and_horseradish = SandwichRecipe(
        "Beef and Horseradish",
        {
            "White Bread": 2,
            "Beef": 50,
            "Horseradish Mayonnaise": 29,
            "Rocket Salad": 24
        }
    )

    brie_bacon_chilli = SandwichRecipe(
        "Brie, Bacon and Chilli Chutney",
        {
            "Wholemeal Bread": 2,
            "Brie": 45,
            "Chilli Chutney": 25,
            "Smoked Bacon": 22,
            "Spinach": 29,
            "Mayonnaise": 23,
        }
    )

    bacon_and_egg = SandwichRecipe(
        "Bacon & Egg",
        {
            "Wholemeal Bread": 2,
            "Smoked Bacon": 64,
            "Egg": 25,
            "Mayonnaise": 16
        }
    )

    cheese = SandwichRecipe(
        "Cheese",
        {
            "White Bread": 2,
            "Medium Cheddar": 45,
            "Butter": 6
        }
    )

    min_sandwiches = 1
    max_sandwiches = 1000
    desired_sandwiches = {
        cheese
    }

    print(json.dumps(cheese))

    calculate_optimum_sandwich_counts(min_sandwiches, max_sandwiches, desired_sandwiches)


if __name__ == "__main__":
    main()
