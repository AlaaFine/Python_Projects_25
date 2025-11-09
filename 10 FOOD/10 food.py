    
    #Task 10 :
# Project about Food
print("Welcome to Healthy food for thirty-one days")

name = input("What is your name Sir or Madaam: ")
goal = input("Gain weight OR Lose weight: ").lower()

print(f"Hello {name}, you selected: {goal}")

day_number = int(input("What is the number of the day you want (1-31): "))

# Gain Weight Plan (31 days complete)
Gain_weight = {
    1: ["Breakfast: 2 eggs + 1 loaf of local bread + a cup of yogurt",
        "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
        "Dinner: 1 loaf of local bread + tahini or beans + salad",
        "Snack: 1 cup of yogurt + a banana"],

    2: ["Breakfast: Beans 1 cup + 1 loaf of bread + a cup of yogurt",
        "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
        "Dinner: 2 eggs + a loaf of bread + vegetables",
        "Snack: Yogurt + a spoonful of tahini + bread"],

    3: ["Breakfast: A cup of yogurt + 2 small loaves of bread + fava beans",
        "Lunch: Rice + lentils + a spoonful of oil or tahini + salad",
        "Dinner: A loaf of bread + boiled or lightly fried potatoes + an egg",
        "Snack: A cup of yogurt + dates (3-4)"],

    4: ["Breakfast: Beans + Loaf + Yogurt",
        "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
        "Dinner: 1 loaf of local bread + tahini or beans + salad",
        "Snack: 1 cup of yogurt + a banana"],

    5: ["Breakfast: 2 eggs + 1 loaf of local bread + a cup of yogurt",
        "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
        "Dinner: 1 loaf of local bread + tahini or beans + salad",
        "Snack: 1 cup of yogurt + a banana"],

    6: ["Breakfast: Beans (1 cup) + 1 loaf of bread + a cup of yogurt",
        "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
        "Dinner: 2 eggs + a loaf of bread + vegetables",
        "Snack: Yogurt + a spoonful of tahini + bread"],

    7: ["Breakfast: A cup of yogurt + 2 small loaves of bread + fava beans",
        "Lunch: Rice + lentils + a spoonful of oil or tahini + salad",
        "Dinner: A loaf of bread + boiled potatoes + an egg",
        "Snack: A cup of yogurt + dates (3-4)"],

    8: ["Breakfast: Beans 1 cup + 1 loaf of bread + a cup of yogurt",
        "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
        "Dinner: 2 eggs + a loaf of bread + vegetables",
        "Snack: Yogurt + a spoonful of tahini + bread"],

    9: ["Breakfast: Beans + Loaf + Yogurt",
        "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
        "Dinner: 1 loaf of local bread + tahini or beans + salad",
        "Snack: 1 cup of yogurt + a banana"],

    10: ["Breakfast: 2 eggs + 1 loaf of local bread + a cup of yogurt",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"],

    11: ["Breakfast: Beans + Loaf + Yogurt",
         "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
         "Dinner: 2 eggs + a loaf of bread + vegetables",
         "Snack: Yogurt + a spoonful of tahini + bread"],

    12: ["Breakfast: Beans 1 cup + 1 loaf of bread + a cup of yogurt",
         "Lunch: Rice + lentils + a spoonful of oil or tahini + salad",
         "Dinner: A loaf of bread + boiled potatoes + an egg",
         "Snack: A cup of yogurt + dates (3-4)"],

    13: ["Breakfast: A cup of yogurt + 2 small loaves of bread + fava beans",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"],

    14: ["Breakfast: Beans + Loaf + Yogurt",
         "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
         "Dinner: 2 eggs + a loaf of bread + vegetables",
         "Snack: Yogurt + a spoonful of tahini + bread"],

    15: ["Breakfast: 2 eggs + 1 loaf of local bread + a cup of yogurt",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"],

    16: ["Breakfast: Beans 1 cup + 1 loaf of bread + a cup of yogurt",
         "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
         "Dinner: 2 eggs + a loaf of bread + vegetables",
         "Snack: Yogurt + a spoonful of tahini + bread"],

    17: ["Breakfast: Beans + Loaf + Yogurt",
         "Lunch: Rice + lentils + a spoonful of oil or tahini + salad",
         "Dinner: A loaf of bread + boiled potatoes + an egg",
         "Snack: A cup of yogurt + dates (3-4)"],

    18: ["Breakfast: 2 eggs + 1 loaf of local bread + a cup of yogurt",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"],

    19: ["Breakfast: A cup of yogurt + 2 small loaves of bread + fava beans",
         "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
         "Dinner: 2 eggs + a loaf of bread + vegetables",
         "Snack: Yogurt + a spoonful of tahini + bread"],

    20: ["Breakfast: Beans + Loaf + Yogurt",
         "Lunch: Rice + lentils + a spoonful of oil or tahini + salad",
         "Dinner: A loaf of bread + boiled potatoes + an egg",
         "Snack: A cup of yogurt + dates (3-4)"],

    21: ["Breakfast: 2 eggs + 1 loaf of local bread + a cup of yogurt",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"],

    22: ["Breakfast: Beans (1 cup) + 1 loaf of bread + a cup of yogurt",
         "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
         "Dinner: 2 eggs + a loaf of bread + vegetables",
         "Snack: Yogurt + a spoonful of tahini + bread"],

    23: ["Breakfast: A cup of yogurt + 2 small loaves of bread + fava beans",
         "Lunch: Rice + lentils + a spoonful of oil or tahini + salad",
         "Dinner: A loaf of bread + boiled potatoes + an egg",
         "Snack: A cup of yogurt + dates (3-4)"],

    24: ["Breakfast: Beans (1 cup) + 1 loaf of bread + a cup of yogurt",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"],

    25: ["Breakfast: 2 eggs + a loaf of bread + a cup of yogurt",
         "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
         "Dinner: 2 eggs + a loaf of bread + vegetables",
         "Snack: Yogurt + a spoonful of tahini + bread"],

    26: ["Breakfast: A cup of yogurt + 2 small loaves of bread + fava beans",
         "Lunch: Rice + lentils + a spoonful of oil or tahini + salad",
         "Dinner: A loaf of bread + boiled potatoes + an egg",
         "Snack: A cup of yogurt + dates (3-4)"],

    27: ["Breakfast: 2 eggs + 1 loaf of local bread + a cup of yogurt",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"],

    28: ["Breakfast: Beans + Loaf + Yogurt",
         "Lunch: Rice (1.5 cups) + 1/4 chicken or liver + salad",
         "Dinner: 2 eggs + a loaf of bread + vegetables",
         "Snack: Yogurt + a spoonful of tahini + bread"],

    29: ["Breakfast: Beans (1 cup) + 1 loaf of bread + a cup of yogurt",
         "Lunch: Rice + lentils + a spoonful of oil or tahini + salad",
         "Dinner: A loaf of bread + boiled potatoes + an egg",
         "Snack: A cup of yogurt + dates (3-4)"],

    30: ["Breakfast: A cup of yogurt + 2 small loaves of bread + fava beans",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"],

    31: ["Breakfast: 2 eggs + 1 loaf of local bread + a cup of yogurt",
         "Lunch: 1 1/2 cups of rice + vegetables + a cup of beans or lentils",
         "Dinner: 1 loaf of local bread + tahini or beans + salad",
         "Snack: 1 cup of yogurt + a banana"]
}

# Lose Weight Plan (31 days complete)
Lose_weight = {
    1: ["Breakfast: Boiled egg + 1/4 loaf of baladi bread + cucumber or tomato",
        "Lunch: 1/2 cup rice or 1/4 loaf of bread + 1 cup cooked vegetables + 1/2 cup lentils or fava beans",
        "Dinner: Large salad (cucumber, tomato, and carrot) + a small yogurt"],

    2: ["Breakfast: Half a cup of fava beans with lemon + a quarter loaf of bread + cucumber",
        "Lunch: One cup of yellow lentil soup + half a loaf of baladi bread + a plate of salad",
        "Dinner: Two boiled eggs + a small plate of cooked vegetables"],

    3: ["Breakfast: One egg + a quarter loaf of bread + cucumber/lettuce",
        "Lunch: Lentil soup + a salad + half a loaf of bread",
        "Dinner: Yogurt + a piece of fruit"],

    4: ["Breakfast: Boiled egg + 1/4 loaf of baladi bread + cucumber or tomato",
        "Lunch: 1/2 cup rice or 1/4 loaf of bread + 1 cup cooked vegetables + 1/2 cup lentils or fava beans",
        "Dinner: Large salad (cucumber, tomato, and carrot) + a small yogurt"],

    5: ["Breakfast: Half a cup of fava beans with lemon + a quarter loaf of bread + cucumber",
        "Lunch: One cup of yellow lentil soup + half a loaf of baladi bread + a plate of salad",
        "Dinner: Two boiled eggs + a small plate of cooked vegetables"],

    6: ["Breakfast: Yogurt + a piece of fruit (orange or guava)",
        "Lunch: Half a cup of rice + vegetables + a piece of liver or a quarter of a small chicken",
        "Dinner: Fava beans (half a cup) + salad"],

    7: ["Breakfast: One egg + a quarter loaf of bread + cucumber/lettuce",
        "Lunch: Lentil soup + a salad + half a loaf of bread",
        "Dinner: Yogurt + a piece of fruit"],

    8: ["Breakfast: Boiled egg + 1/4 loaf of baladi bread + cucumber or tomato",
        "Lunch: 1/2 cup rice or 1/4 loaf of bread + 1 cup cooked vegetables + 1/2 cup lentils or fava beans",
        "Dinner: Large salad (cucumber, tomato, and carrot) + a small yogurt"],

    9: ["Breakfast: Half a cup of fava beans with lemon + a quarter loaf of bread + cucumber",
        "Lunch: One cup of yellow lentil soup + half a loaf of baladi bread + a plate of salad",
        "Dinner: Two boiled eggs + a small plate of cooked vegetables"],

    10: ["Breakfast: Beans + Salad + 1/4 Loaf of Bread",
         "Lunch: Half a Cup of Rice + Vegetables + Egg or Lentils",
         "Dinner: Large Salad + Yogurt"],

    11: ["Breakfast: One egg + a quarter loaf of bread + cucumber/lettuce",
         "Lunch: Lentil soup + a salad + half a loaf of bread",
         "Dinner: Yogurt + a piece of fruit"],

    12: ["Breakfast: Yogurt + a piece of fruit (orange or guava)",
         "Lunch: Half a cup of rice + vegetables + a piece of liver or a quarter of a small chicken",
         "Dinner: Fava beans (half a cup) + salad"],

    13: ["Breakfast: Beans + Salad + 1/4 Loaf of Bread",
         "Lunch: Half a Cup of Rice + Vegetables + Egg or Lentils",
         "Dinner: Large Salad + Yogurt"],

    14: ["Breakfast: Yogurt + a piece of fruit (orange or guava)",
         "Lunch: Half a cup of rice + vegetables + a piece of liver or a quarter of a small chicken",
         "Dinner: Fava beans (half a cup) + salad"],

    15: ["Breakfast: Boiled egg + 1/4 loaf of baladi bread + cucumber or tomato",
         "Lunch: 1/2 cup rice or 1/4 loaf of bread + 1 cup cooked vegetables + 1/2 cup lentils or fava beans",
         "Dinner: Large salad (cucumber, tomato, and carrot) + a small yogurt"],

    16: ["Breakfast: Half a cup of fava beans with lemon + a quarter loaf of bread + cucumber",
         "Lunch: One cup of yellow lentil soup + half a loaf of baladi bread + a plate of salad",
         "Dinner: Two boiled eggs + a small plate of cooked vegetables"],

    17: ["Breakfast: One egg + a quarter loaf of bread + cucumber/lettuce",
         "Lunch: Lentil soup + a salad + half a loaf of bread",
         "Dinner: Yogurt + a piece of fruit"],

    18: ["Breakfast: Yogurt + a piece of fruit (orange or guava)",
         "Lunch: Half a cup of rice + vegetables + a piece of liver or a quarter of a small chicken",
         "Dinner: Fava beans (half a cup) + salad"],

    19: ["Breakfast: Half a cup of fava beans with lemon + a quarter loaf of bread + cucumber",
         "Lunch: One cup of yellow lentil soup + half a loaf of baladi bread + a plate of salad",
         "Dinner: Two boiled eggs + a small plate of cooked vegetables"],

    20: ["Breakfast: Yogurt + a piece of fruit (orange or guava)",
         "Lunch: Half a cup of rice + vegetables + a piece of liver or a quarter of a small chicken",
         "Dinner: Fava beans (half a cup) + salad"],

    21: ["Breakfast: One egg + a quarter loaf of bread + cucumber/lettuce",
         "Lunch: Lentil soup + a salad + half a loaf of bread",
         "Dinner: Yogurt + a piece of fruit"],

    22: ["Breakfast: Boiled egg + 1/4 loaf of baladi bread + cucumber or tomato",
         "Lunch: 1/2 cup rice or 1/4 loaf of bread + 1 cup cooked vegetables + 1/2 cup lentils or fava beans",
         "Dinner: Large salad (cucumber, tomato, and carrot) + a small yogurt"],

    23: ["Breakfast: Half a cup of fava beans with lemon + a quarter loaf of bread + cucumber",
         "Lunch: One cup of yellow lentil soup + half a loaf of baladi bread + a plate of salad",
         "Dinner: Two boiled eggs + a small plate of cooked vegetables"],

    24: ["Breakfast: Yogurt + a piece of fruit (orange or guava)",
         "Lunch: Half a cup of rice + vegetables + a piece of liver or a quarter of a small chicken",
         "Dinner: Fava beans (half a cup) + salad"],

    25: ["Breakfast: One egg + a quarter loaf of bread + cucumber/lettuce",
         "Lunch: Lentil soup + a salad + half a loaf of bread",
         "Dinner: Yogurt + a piece of fruit"],

    26: ["Breakfast: Beans + Salad + 1/4 Loaf of Bread",
         "Lunch: Half a Cup of Rice + Vegetables + Egg or Lentils",
         "Dinner: Large Salad + Yogurt"],

    27: ["Breakfast: One egg + a quarter loaf of bread + cucumber/lettuce",
         "Lunch: Lentil soup + a salad + half a loaf of bread",
         "Dinner: Yogurt + a piece of fruit"],

    28: ["Breakfast: Yogurt + a piece of fruit (orange or guava)",
         "Lunch: Half a cup of rice + vegetables + a piece of liver or a quarter of a small chicken",
         "Dinner: Fava beans (half a cup) + salad"],

    29: ["Breakfast: Boiled egg + 1/4 loaf of baladi bread + cucumber or tomato",
         "Lunch: 1/2 cup rice or 1/4 loaf of bread + 1 cup cooked vegetables + 1/2 cup lentils or fava beans",
         "Dinner: Large salad (cucumber, tomato, and carrot) + a small yogurt"],

    30: ["Breakfast: Half a cup of fava beans with lemon + a quarter loaf of bread + cucumber",
         "Lunch: One cup of yellow lentil soup + half a loaf of baladi bread + a plate of salad",
         "Dinner: Two boiled eggs + a small plate of cooked vegetables"],

    31: ["Breakfast: Boiled egg + 1/4 loaf of baladi bread + cucumber or tomato",
         "Lunch: 1/2 cup rice or 1/4 loaf of bread + 1 cup cooked vegetables + 1/2 cup lentils or fava beans",
         "Dinner: Large salad (cucumber, tomato, and carrot) + a small yogurt"]
}
