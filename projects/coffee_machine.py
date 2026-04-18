
print('''
         _____        __  __              ___  ___           _     _            
        /  __ \      / _|/ _|             |  \/  |          | |   (_)           
        | /  \/ ___ | |_| |_ ___  ___     | .  . | __ _  ___| |__  _ _ __   ___ 
        | |    / _ \|  _|  _/ _ \/ _ \    | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
        | \__/\ (_) | | | ||  __/  __/    | |  | | (_| | (__| | | | | | | |  __/
        \____/\___/|_| |_| \___|\___|     \_|  |_/\__,_|\___|_| |_|_|_| |_|\___|
                                                                        
        ''' )

# Initial machine resources and menu data
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

profit = 0
is_on = True

while is_on:
    # 1. Prompt user for their choice 
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # 2. Turn off the machine 
    if choice == "off":
        is_on = False
    
    # 3. Print report [cite: 9, 10]
    elif choice == "report":
        print(f"Water: {resources["water"]}ml") 
        print(f"Milk: {resources["milk"]}ml") 
        print(f"Coffee: {resources["coffee"]}g") 
        print(f"Money: ${profit}") 

    elif choice in MENU:
        drink = MENU[choice]
        
        # 4. Check resources 
        enough_resources = True
        for item, amount in drink["ingredients"].items(): # item stores the key , amount stores the value , .items() does this
            if amount > resources[item]:
                print(f"Sorry there is not enough {item}.") 
                enough_resources = False
        
        if enough_resources:
            # 5. Process coins 
            print("Please insert coins.")
            quarters = int(input("how many quarters?: ")) * 0.25 
            dimes = int(input("how many dimes?: ")) * 0.10 
            nickles = int(input("how many nickles?: ")) * 0.05 
            pennies = int(input("how many pennies?: ")) * 0.01 
            total_received = quarters + dimes + nickles + pennies 

            # 6. Check transaction 
            if total_received < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.") 
            else:
                # Calculate change and round to 2 decimal places 
                change = round(total_received - drink["cost"], 2)
                if change > 0:
                    print(f"Here is ${change:.2f} dollars in change.") 
                
                profit += drink["cost"] 
                
                # 7. Make Coffee: Deduct resources [cite: 35, 36]
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item] 
                
                print(f"Here is your {choice}. Enjoy!")