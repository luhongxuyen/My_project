from sys import exc_info
from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    on_mode = True

    menu = Menu()
    cf_maker = CoffeeMaker()
    m_machine = MoneyMachine()

    while on_mode:
        try:
            user_input = input(f"What would you like? ({menu.get_items()}): ").lower()

            if user_input == "report":
                cf_maker.report()
                m_machine.report()
            
            elif user_input in ["off", "end", "shutdown"]:
                print('Goodbye.')
                on_mode = False

            else:
                drink = menu.find_drink(user_input)
                
                if drink:
                    if m_machine.make_payment(cost= drink.cost):
                        if cf_maker.is_resource_sufficient(drink):
                            cf_maker.make_coffee(drink)

        except ValueError:
            exc_type, exc_value, exc_traceback = exc_info()
            print(f'Type of error: {exc_type.__name__}')
        

if __name__ == "__main__":
    main()