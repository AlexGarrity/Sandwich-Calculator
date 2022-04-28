class Ingredient:
    def __init__(self, name: str, cost: float, quantity_per_pack: float):
        self.name = name
        self.cost = cost
        self.quantity_per_pack = quantity_per_pack


ingredients: dict[str, list[Ingredient]] = {
    # Breads
    "White Bread": [
        Ingredient("Sainsbury's Soft Medium Sliced White Bread 800g", 55, 18)
    ],
    "Wholemeal Bread": [
        Ingredient("Sainsbury's Medium Sliced Wholemeal Bread 800g", 55, 18)
    ],

    # Meats
    "Chicken Breast": [
        Ingredient("J.James & Family Cooked British Chicken Breast Slices 240g", 199, 240)
    ],
    "Smoked Bacon": [
        Ingredient("Sainsbury's British Smoked cooked crispy Bacon rashers 100g", 200, 100)
    ],
    "Smoked Ham": [
        Ingredient("Sainsbury's British Smoked Cooked Ham Slices x7 120g", 190, 120)
    ],
    "Tuna": [
        Ingredient("Sainsbury's Tuna Chunks In Water 160g", 105, 120),
        Ingredient("Sainsbury's Tuna Chunks in Spring Water 3x80g (3x60g*)", 200, 180),
        Ingredient("Sainsbury's Tuna in Spring Water 340g (240g*)", 210, 240),
        Ingredient("Sainsbury's Tuna Chunks In Spring Water 4x160g (480g*)", 400, 480)

    ],
    "Beef": [
        Ingredient("Sainsbury's British Cooked Roast Beef Slices x3 85g", 190, 85)
    ],

    # Cheese
    "Medium Cheddar": [
        Ingredient("Sainsbury's Mature British Cheddar 220g", 160, 220),
        Ingredient("Sainsbury's British Mature Cheddar Cheese 400g", 210, 400),
        Ingredient("Mary Ann's Dairy Mature Cheddar Cheese 600g", 266, 600),
        Ingredient("Mary Ann's Dairy Mature Cheddar Cheese 900g", 399, 900)
    ],
    "Brie": [
        Ingredient("Sainsbury's French Mild Brie Cheese 200g", 110, 200)
    ],

    # ???
    "Egg": [
        Ingredient("Sainsbury's Woodland Free Range Medium Eggs x6", 100, 348),
        Ingredient("Sainsbury's Woodland Free Range Large Eggs x6", 125, 408),
        Ingredient("Sainsbury's Woodland Free Range Very Large Eggs x6", 150, 450),
        Ingredient("Sainsbury's Woodland Free Range Medium Eggs x12", 180, 696),
        Ingredient("Sainsbury's Woodland Free Range Large Eggs x12", 215, 816),
        Ingredient("Sainsbury's Free Range British Eggs Medium x15", 210, 870)
    ],

    # Vegetables
    "Sweetcorn": [
        Ingredient("The Greengrocer Sweetcorn 950g", 89, 950)
    ],
    "Rocket Salad": [
        Ingredient("Sainsbury's Rocket Salad, SO Organic 60g", 160, 60)
    ],
    "Spinach": [
        Ingredient("Sainsbury's Baby Whole Leaf Spinach 1kg", 150, 1000)
    ],

    # Sauces
    "Mayonnaise": [
        Ingredient("Hubbard's Foodstore Mayonnaise 500ml", 60, 549)
    ],
    "Horseradish Mayonnaise": [
        Ingredient("Sainsbury's Creamed Horseradish Sauce 160ml", 60, 176)
    ],
    "Chilli Chutney": [
        Ingredient("Sainsbury's Taste the Difference Chilli Jam Spicy & Sweet 200g", 160, 200)
    ],
    "Butter": [
        Ingredient("Sainsbury's British Butter, Unsalted 250g", 148, 250)
    ]
}
