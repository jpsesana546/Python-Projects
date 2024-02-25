import menu
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_resources_availability(coffee_choice):
    ingredients_required = menu.MENU[coffee_choice]["ingredients"]
    available_resources = menu.resources["ingredients"]

    for ingredient, required_amount in ingredients_required.items():
        if required_amount > available_resources[ingredient]:
            print(f"Sorry, not enough {ingredient}.")
            return False

    return True


def process_payment(coffee_choice):
    total = 0
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickels: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01

    if total < menu.MENU[coffee_choice]["cost"]:
        print("Insufficient Funds")
        return False
    else:
        menu.resources["money"] += menu.MENU[coffee_choice]["cost"]
        change = round(total - menu.MENU[coffee_choice]["cost"], 2)
        print(f"Your change is ${change}")
        return True


def prepare_coffee(coffee_choice):
    ingredients_required = menu.MENU[coffee_choice]["ingredients"]
    available_resources = menu.resources["ingredients"]

    for ingredient, required_amount in ingredients_required.items():
        available_resources[ingredient] -= required_amount

    return print(f"Here is your {coffee_choice}. Enjoy!")


def main():
    machine_on = True

    while machine_on:
        coffee_choice = input(
            "What would you like? (espresso/latte/cappuccino) ")

        if coffee_choice == "off":
            machine_on = False
            print("Turning off...")
            break

        if coffee_choice == "report":
            return print(menu.resources)

        if not check_resources_availability(coffee_choice):
            return

        if not process_payment(coffee_choice):
            return
        else:
            prepare_coffee(coffee_choice)


if __name__ == "__main__":
    clear_screen()
    main()

