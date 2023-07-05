"""
CSSE1001 Assignment 1
Semester 1, 2023
"""

# Fill these in with your details
__author__ = "Shae Schlusser"
__email__ = "shaeschlusser@uqconnect.edu.au"
__date__ = "20/03/2023"

from constants import *

#Hours worked on assignment
def num_hours() -> float:
    return 20

def get_recipe_name(recipe: tuple[str, str]) -> str:
    '''
    Returns the name of a recipe from a tuple containing the recipe name, ingredients and amounts

            Parameters:
                    recipe (tuple): first object string is the name, second object string is the list of ingredients

            Returns:
                    recipe_name (str): string of the recipe name
    '''   
    
    #Row 0 is the name of the recipe
    recipe_name = recipe[0]

    return recipe_name

def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    '''
    Returns a tuple of every component of one ingredient in a recipe where each object of the tuple corresponds to the amount, measurement and name

            Parameters:
                    raw_ingredient_detail (str): string of all ingredients in a recipe including the name, amount and measurement where new ingredients are separated by a comma

            Returns:
                    ingredients (tuple): tuple containing the amount, measurement and name of the ingredient
    '''

    #split ingredient details 3 times - for amount, measurment and item
    list_of_raw_ingredients = raw_ingredient_detail.split(" ", 2)
    amount_ingredient = float(list_of_raw_ingredients[0])
    
    #Remove amount from list
    list_of_raw_ingredients = list_of_raw_ingredients[1:]

    #add amount back as float and convert to tuple
    ingredients = (amount_ingredient, ) + tuple(list_of_raw_ingredients)

    return ingredients

def create_recipe() -> tuple[str, str]:
    '''
    Returns a tuple of a recipe created by the user, including the name of the recipe and all ingredients including their amounts, measurement and names in one string

            Parameters:
                    name_of_recipe (str): string entered by the user corresponding to the name of the recipe

                    ingredient (str): string entered by the user corresponding to the amount, measurement and name of the ingredient in the recipe, separated by spaces
            Returns:
                    recipe (tuple): tuple containing the name of the recipe and a single string of every ingredient in the recipe
    '''

    recipe = []
    ingredient_list = ""
    name_of_recipe = input("Please enter the recipe name: ")
    recipe += [name_of_recipe]

    while True:
        ingredient = input("Please enter an ingredient: ")
        #Check if user has not entered anything
        if len(ingredient) == 0:
            break

        #Break up separate ingredients with comma
        ingredient_list += ingredient + ','

    #Remove the last comma from the list and append the final ingredient list to the recipe list    
    ingredient_list = ingredient_list.rstrip(',')
    recipe.append(ingredient_list)
    recipe = tuple(recipe)

    return recipe

def recipe_ingredients(recipe: tuple[str, str]) -> tuple[tuple[float, str, str]]:
    '''
    Returns a 2-dimensional tuple containing every ingredient in a recipe, and each ingredient is a tuple containing the amount, measurement and name

            Parameters:
                    recipe (tuple): tuple containing the name of the recipe and a single string of every ingredient separated by commas

            Returns:
                    recipe_ingredients (tuple): tuple containing the amount, measurement and name of every ingredient in the recipe in its own tuple
    '''

    #Unpack tuple but only the ingredient part
    recipe_name, ingredients = recipe
    #List of all ingredients in the recipe
    recipe_ingredients  = []
    #Split ingredients into their own string, separated by a comma
    split_ingredients = ingredients.split(",")
    
    #Parse all ingredients from a single string into separate elements 
    for i in split_ingredients:
        recipe_ingredients += (parse_ingredient(i), )

    recipe_ingredients = tuple(recipe_ingredients)
    
    return recipe_ingredients

def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]) -> None:
    '''
    Adds a recipe into the recipes list

            Parameters:
                    new_recipe (tuple): tuple containing the name of the recipe and a single string of every ingredient separated by commas

            Returns:

    '''

    #Convert the recipe into a tuple and add it to the existing recipes
    recipe = tuple(new_recipe)
    recipes.append(recipe)

    return 

def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
    '''
    Searches through all recipes in the recipe list and returns the ingredients of a recipe that matches a given recipe name

    If no recipe matches the given recipe name, return None

            Parameters:
                    recipe_name (str): string of the recipe name

            Returns:
                    found_recipe (tuple): tuple containing the name of the recipe and the amount, measurement and name of every ingredient in the recipe in one tuple
    '''
    
    count = 0
    found_recipe = []

    #Compare the recipe name to all recipe names in recipes, if they match, return the name of the recipe
    for i in recipes:
        if recipe_name == get_recipe_name(i):
            found_recipe = i
            count += 1
            break

    #If no recipe name matches any in the recipe list, return None
    if count == 0:
        return None

    return found_recipe

def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    '''
    Removes a recipe from the list of recipes given the name of the recipe

    If no recipe matches the name of the recipe, nothing happens

            Parameters:
                    name (str): string of the recipe name

                    recipes (list): list of recipes

            Returns:

    '''

    #Compare the recipe name to all recipe names in recipes and remove one instance that matches if any are found
    for i in recipes:
        if name == get_recipe_name(i):
            recipes.remove(i)

    return 

def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float,str] | None:
    '''
    Checks if the given ingredient is in the recipe and returns the amount and measurment of the ingredient as a tuple

    If the ingredient does not exist in the recipe

            Parameters:
                    ingredient (str): string of the ingredient name

                    recipe (tuple): tuple of the recipe the ingredient is in

            Returns:
                    ingredient_amount (tuple): tuple containing the name of the recipe and the amount, measurement and name of every ingredient in the recipe in one tuple
    '''

    i = 0
    ingredients = recipe_ingredients(recipe)

    #Check if the ingredient exists in the recipe
    if ingredient in recipe[1]:
        #Get the amount and measurement for all ingredients in the recipe
        while i < len(ingredients):
            if ingredients[i][2] == ingredient:
                amount, measurement, item = ingredients[i]
            i+= 1

        ingredient_amount = [amount] + [measurement]
        ingredient_amount = tuple(ingredient_amount)

        return ingredient_amount
    #Return None if the ingredient is not in the recipe
    else:
        return None

def  add_to_shopping_list(ingredient_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str] | None]) -> None:
    '''
    Adds an ingredient to the shopping list

    If the ingredient is already in the list, the item amount is added onto the existing amount

            Parameters:
                    ingredient_details (tuple): tuple of ingredient details including the amount, measurement and name

                    shopping_list (list): list of all ingredients 

            Returns:

    '''

    i = 0
    in_the_list = False

    while i < len(shopping_list):
        #If ingredient is already in the shopping list
        if shopping_list[i][2] == ingredient_details[2]:

            #Get name, amount and measurement of the ingredient currently in the shopping list
            amount_in_shopping_list, measurement, name = shopping_list[i]

            #Remove first instance of the ingredient
            shopping_list.remove(shopping_list[i])

            #Add the new ingredient amount to current ingredient amount
            amount_to_be_added = ingredient_details[0]
            new_amount = amount_in_shopping_list + amount_to_be_added

            new_ingredient_amount = [new_amount] + [measurement] + [name]
            new_ingredient_amount = tuple(new_ingredient_amount)

            #Add the ingredient back with updated amount
            shopping_list.append(new_ingredient_amount)
            in_the_list = True
            break
        i+= 1
    
    #If ingredient is not in shopping list
    if in_the_list == False:
        shopping_list.append(ingredient_details)

    return

def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list:list) -> None:
    '''
    Removes an ingredient from the shopping list

    If the remaning amount of the ingredient is <= 0 then the item is removed from the list

            Parameters:
                    ingredient_name (str): string of the name of ingredient

                    amount (float): float amount of the item to be removed

                    shopping_list (list): list of all ingredients 

            Returns:

    '''   
    
    i = 0
    while i < len(shopping_list):
        #Check if ingredient added is already in the shopping list
        if shopping_list[i][2] == ingredient_name:

            #Get name, amount and measurement of the ingredient currently in the shopping list 
            amount_in_shopping_list, measurement, name = shopping_list[i]

            #Remove first instance of the ingredient in the shopping list
            shopping_list.remove(shopping_list[i])
            new_amount = amount_in_shopping_list - amount

            #If the new ingredient amount is less than 0, break the loop, which removes the ingredient entirely
            if new_amount <= 0:
                break
            else:
                new_ingredient_amount = [new_amount] + [measurement] + [name]
                new_ingredient_amount = tuple(new_ingredient_amount)
                shopping_list.append(new_ingredient_amount)
            break
        i+= 1

def generate_shopping_list(recipes: list[tuple[str, str]]) -> list[tuple[float, str, str]]:
    '''
    Returns a list of ingredients given a list of recipes

    Ingredient details include amount, measurement and ingredient name

            Parameters:
                    recipes (list): list of tuples of recipes including the recipe name and a single string of ingredients


            Returns:
                    shopping_list (list): list of tuples containing the amount, measurement and name of every ingredient in each recipe
    '''

    shopping_list_of_recipes = []
    shopping_list = []

    #Combine all recipe ingredients into one list
    for i in range(len(recipes)):
        shopping_list_of_recipes.append(recipe_ingredients(recipes[i]))

    #Flatten shopping list into 1 dimensional list
    flat_shopping_list = [k for i in shopping_list_of_recipes for k in i]

    #Add all ingredients to the shopping list
    for i in range(len(flat_shopping_list)):
        add_to_shopping_list(flat_shopping_list[i], shopping_list)

    return shopping_list

def display_ingredients(shopping_list: list[tuple[float, str, str]]) -> None:
    '''
    Print the current shopping list in alphabetical order

            Parameters:
                    shopping_list (list): list of tuples containing the amount, measurement and name of every ingredient in each recipe


            Returns:

    '''

    max_amount_length = 0
    max_measurement_length = 0
    max_item_length = 0
    ingredient = []
    item_list_with_space = []
    new_shopping_list = []

    #Get largest number length from ingredient
    for i in range(len(shopping_list)):
        if len(str(shopping_list[i][0])) > len(str(max_amount_length)):
            max_amount_length = shopping_list[i][0]
    max_amount_length = len(str(max_amount_length))

    #Get biggest word length from measurement
    for i in range(len(shopping_list)):
        if len(str(shopping_list[i][1])) > len(str(max_measurement_length)):
            max_measurement_length = shopping_list[i][1]
    max_measurement_length = len(str(max_measurement_length))

    #Get biggest word length from item
    for i in range(len(shopping_list)):
        if len(str(shopping_list[i][2])) > len(str(max_item_length)):
            max_item_length = shopping_list[i][2]
    max_item_length = len(max_item_length)

    size_of_measurement_column = max_measurement_length + 3
    
    #Sort list alphabetically
    shopping_list.sort(key= lambda x: x[2])

    #Get measurements and put into a list
    for i in range(len(shopping_list)):
        item_list_with_space.append(shopping_list[i][1])

    #Check which measurement strings are even, and distribute whitespace evenly on both sides so that the total character length equals size_of_measurement_column
    for i in range(len(item_list_with_space)):
        if len(item_list_with_space[i]) % 2 != 0:
            number_spaces = (size_of_measurement_column - len(item_list_with_space[i])) // 2
            item_list_with_space[i] = " "*number_spaces + item_list_with_space[i] + " "*(number_spaces - 1)

        #For odd strings, get the number of whitespaces on the left and right side of the string so that the total character length equals size_of_measurement_column
        left_spaces = (size_of_measurement_column - len(item_list_with_space[i])) // 2
        right_spaces = ((size_of_measurement_column - len(item_list_with_space[i])) // 2)
        #Skew whitespaces to the right
        item_list_with_space[i] = " "*left_spaces + item_list_with_space[i] + " "*(right_spaces + 1)

    #Create a tuple of all ingredients in the shopping list
    for i in range(len(shopping_list)):
        amount, measurement, name = shopping_list[i]
        measurement = item_list_with_space[i]
        ingredient = [amount] + [measurement] + [name]
        ingredient = tuple(ingredient)
        new_shopping_list.append(ingredient)

    #Display list with "|" separators
    for item in new_shopping_list:
        print("|" + " "*((max_amount_length-len(str(item[0])))), item[0], "|" + item[1]+ "|",item[2], " "*(max_item_length-len(item[2])),  "|")

    return

def sanitise_command(command: str, remove_num: bool) -> str:
    '''
    Returns a user's command with no whitespace and all lowercase

    If remove_num is True, remove all numbers in the command too

            Parameters:
                    command (tuple): tuple containing the name of the recipe and a single string of every ingredient separated by commas

                    remove_num (bool): bool where True removes all numbers in the command and False does not

            Returns:
                    new_command (str): string of new command with whitespace or numbers removed, and all lower case
    '''
    
    #Remove numbers in the string if True
    if remove_num == True:
        new_command = ''.join((x for x in command if not x.isdigit()))

    #Remove whitespace and convert all uppercase letters to lowercase
    new_command = "".join(new_command.rstrip().lstrip())
    new_command = new_command.lower()
    
    return new_command

def main():
    '''
    Create a collection of pre-made recipes

    Prompts user for a command and responds accordingly

    '''
    loop = True
    shopping_list = []
    collection = []

    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]
    while loop == True:
        user_input = input("Please enter a command: ")
        
        ### Dynamic Inputs ###

        #Remove ingredient from shopping list
        if "rm -i" in user_input:
            ingredient = []
            amount = ""
            name = ""
            #Clean user input by removing "rm -i", leaving only the ingredient name and amount
            user_input = user_input.replace("rm -i", "")

            #separate amount from name and place them in separate strings
            for i in user_input:
                if (i.isdigit()):
                    amount += i
                else:
                    name += i
            
            #Remove whitespace from the name string
            name = "".join(name.rstrip().lstrip())
            amount = float(amount)
            #Add them back into a single list where name is a string and amount is a float
            ingredient = [name] + [amount]
            remove_from_shopping_list(ingredient[0], ingredient[1], shopping_list)
            
        #Add a recipe to the collection
        if "add" in user_input:
            user_input = user_input.replace("add", "")
            user_input = sanitise_command(user_input, True)

            #If the recipe name matches one in the recipe book, add it to the collection
            if find_recipe(user_input, recipe_collection) != None:
                add_recipe(find_recipe(user_input, recipe_collection), collection)
            else:
                print("")
                print("Recipe does not exist in the cook book. ")
                print("Use the mkrec command to create a new recipe.")
                print("")

        #Remove recipe from the collection
        if "rm" in user_input:
            user_input = user_input.replace("rm", "")
            user_input = sanitise_command(user_input, True)
            remove_recipe(user_input, collection)

        ### Static Inputs ###

        #Remove whitespace, numbers and capital letters in preparation for all static input commands
        user_input = sanitise_command(user_input, True)

        #Display help
        if user_input == "h":
            print(HELP_TEXT)
        
        #Create a recipe and add it to the cook book DONE
        if user_input == 'mkrec':
            recipe_collection += [create_recipe()]

        #List all items in shopping list DONE
        if user_input == "ls":

            #Check if there are recipes in the collection and print any that are in there
            if len(collection) == 0:
                print("No recipe in meal plan yet.")
            else:
                print(collection)

        #List all avaibable recipes in the cook book
        if user_input == "ls -a":
            for i in recipe_collection:
                print(get_recipe_name(i))

        #Display shopping list
        if user_input == "ls -s":
            display_ingredients(shopping_list)
        
        #Generate shopping list from collection
        if user_input == "g":

            #Generate a shopping list and display it if there are recipes in the collection
            if len(collection) >  0:
                shopping_list = generate_shopping_list(collection)
                display_ingredients(shopping_list)

        #Quit the program
        elif user_input == "q":
            return

        ### Static Inputs ###

if __name__ == "__main__":
    main()