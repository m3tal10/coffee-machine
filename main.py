MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}


def mutate_resources(resources, ordered):
    for key in ordered['ingredients']:
        resources[key]-=ordered['ingredients'][key]
    resources["money"]+=ordered["cost"]


def check_money(cost):
    print("Please insert coins. ")
    quarters=int(input('How many quarters?: '))*0.25
    dimes=int(input('How many dimes?: '))*0.10
    nickels=int(input('How many nickels?: '))*0.05
    pennies=int(input('How many pennies?: '))*0.01

    total_money= quarters+dimes+nickels+pennies
    if(total_money>cost):
        return total_money-cost
    else:
        return False

def check_resources(choice_ingreds,resources):
    for key in choice_ingreds:
        if(choice_ingreds[key]>resources[key]):
            return f"Sorry, there is not enough {key}"
    return True


def print_report():
    for key in resources:
        if(key=='water' or key=='milk'):
            print(f"{key}: {resources[key]}ml")
        elif(key=='coffee'):
            print(f"{key}: {resources[key]}g")
        else:
            print(f"{key}: ${resources[key]}")


def make_coffee(choice):
    resource_available= check_resources(MENU[choice]['ingredients'],resources)
    if(resource_available!=True):
        return resource_available
    money_available= check_money(MENU[choice]['cost'])
    if(money_available==False):
        return "Sorry that's not enough money. Money refunded."
    mutate_resources(resources, MENU[choice])
    return [choice,round(money_available,2)]


def coffee_machine():
    is_on= True
    while is_on:
        choice= input('What would you like? (espresso/latte/cappuccino): ').lower()
        if choice== 'off':
            print('Machine turned off...')
            is_on=False
            break
        elif choice== 'report':
            print_report()
        else:
            can_make= make_coffee(choice)
            if len(can_make)==2:
                print(f"Here's your {can_make[1]} change.")
                print(f"Here's your {can_make[0]}, enjoy!.")
            else:
                print(can_make)
coffee_machine()
