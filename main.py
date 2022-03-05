#Joe Mama's Pizza

toppings = "\t\t\t\tT O P P I N G S\nOlives, Mushrooms, Onions, Bellpeppers, Jalpeños, Sausage, Pineapple, Extra Cheese, Extra Sauce"

drinkmenu = "\t\t\t\t\tD R I N K S\nCoca-Cola, Sprite, Fanta, Pepsi, Mountain Dew, Lemonade, Orange Juice, Sparkling Water, Water"

foodmenu = "\t\t\t\t\tM E N U\nCheese Pizza, Pepperoni Pizza, Combo Pizza, Keto Pizza, Meat Lovers Pizza, Vegetarian Pizza"

foodorder = input("Welcome to Joe Mama's Pizza! What would you like to order?\n\n" + foodmenu + "\n\n\t")

toppingorder = input("\nWould you like any other toppings with your " + foodorder + "?\n\n" + toppings + "\n\n\t")

drinkorder = input("\nWould you like a drink with your meal?\n\n" + drinkmenu + "\n\n\t")

print("Your " + foodorder + " with " + toppingorder + " and your " + drinkorder + " will be ready in 20 - 30 minutes. Thank you for eating with Joe Mama's Pizza")

