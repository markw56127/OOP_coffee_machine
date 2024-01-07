from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu_ = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def coffee_machine():
    on = True
    while on:
        choice = input(f"What would you like? {menu_.get_items()}: ")
        drink = menu_.find_drink(choice)
        if choice == "off":
            return
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif drink is None:
            print("Please enter a valid drink")
            break
        else:
            if not coffee_maker.is_resource_sufficient(drink):
                break
            else:
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                    on = False

    cont = input("Would you like another drink? Type 'yes' or 'no': ")
    if cont == 'yes':
        coffee_machine()


coffee_machine()
