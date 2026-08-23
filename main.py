def user_startup():
    global budget_days
    budget_days = int(input(
        "Welcome to Alex's Budget Manager. "
        "How many days would you like to budget for?\n"
    ))
    money_in()


def user_income():
    global income
    user_income = input("Do you get paid weekly or monthly? (w/m)\n").lower()
    income_digit = float(input("List the amount of money you make\n"))
    if user_income == "w":
        income = round(income_digit * (budget_days/7), 2)
    elif user_income == "m":
        income = round(income_digit * (budget_days/30), 2)
    print("Income Successfully Changed!")
    return income

def add_gift():
    global gift_check
    global gift_name
    gift_check = {}
    gift_name = gift_name = input("What is the name of the gift(s) payment? Type STOP when done adding.\n").strip()
    print("Gift added sucessfully!")
    while gift_name != "STOP":
        gift_check[gift_name] = None
        gift_name = gift_name = input("What is the name of the gift payment? Type STOP when done adding.\n").strip()
        print("Gift added sucessfully!")
    print("All gift names added successfully!", gift_check)
    return gift_check

def manage_gift(gift_check):
    for name in gift_check:
        gift_amount = float(input(f"List the amount for {name}.\n"))
        gift_check[name] = gift_amount
    print("Your final gift name and amount are shown: ",gift_check)
    print("If any are wrong, reset ALL values with ---> 2. Manage gift income")
    return gift_check

def gift_money():
    print("GIFT MONEY SETTINGS")
    print("Note: Please add at least 1 gift income before attempting to manage income!!")
    print("1. Add gift income.")
    print("2. Manage gift income.")
    print("3. Save and continue.")
    menu_option = int(input())
    while menu_option != 3:
        if menu_option == 1:
            add_gift()
        if menu_option == 2:
            manage_gift(gift_check)
        gift_money()
        menu_option = int(input())
    money_in()

def cost_list():
    global cost_check
    global cost_name
    cost_check = {}
    cost_name = cost_name = input("What is the name of the cost(s) payment? Type STOP when done adding.\n").strip()
    print("Cost added sucessfully!")
    while cost_name != "STOP":
        cost_check[cost_name] = None
        cost_name = cost_name = input("What is the name of the cost payment? Type STOP when done adding.\n").strip()
        print("Cost added sucessfully!")
    print("All cost names added successfully!", cost_check)
    return cost_check

def manage_cost(cost_check):
    for name in cost_check:
        payment_plan = input(f"Is {name} a payment plan? (y/n)\n").lower()
        if payment_plan == "y":
            payment_timing = input(
                "Does the following payment occur weekly, monthly, yearly, or custom interval? (w,m,y,c)\n"
            ).lower()
            if payment_timing == "w":
                cost_amount = float(input(f"List the amount for {name}.\n"))
                cost_check[name] = round(cost_amount * (budget_days/7), 2)
            elif payment_timing == "m":
                cost_amount = float(input(f"List the amount for {name}.\n"))
                cost_check[name] = round(cost_amount * (budget_days / 30), 2)
            elif payment_timing == "y":
                cost_amount = float(input(f"List the amount for {name}.\n"))
                cost_check[name] = round(cost_amount * (budget_days / 365), 2)
            elif payment_timing == "c":
                custom_interval = int(input("What do you want the custom interval to be? [List the number in days]/n"))
                cost_amount = float(input(f"List the amount for ${name}.\n"))
                cost_check[name] = round(cost_amount * (budget_days / custom_interval), 2)
            else:
                print("Not a valid option")
                manage_cost(cost_check)
        elif payment_plan == "n":
            cost_amount = float(input(f"List the amount for {name}.\n"))
            cost_check[name] = cost_amount
        else:
            print("Not a valid option")
            manage_cost(cost_check)
    print("Your final cost name and amount are shown: ", cost_check)
    print("If any are wrong, reset ALL values with ---> 2. Manage cost income")
    print("")
    return cost_check

def money_out():
    print("--SECTION 2: Money Out--")
    print("NOTE: Add at least one cost before attempting to manage!")
    print("1. Add a cost(s)" )
    print("2. Manage cost(s)")
    print("3. Save and calculate!!")
    menu_option = int(input())
    while menu_option != 3:
        if menu_option == 1:
            cost_list()
        elif menu_option == 2:
            manage_cost(cost_check)
        else:
            print("Invalid option")
        money_out()
        menu_option = int(input())
    end_process()


def end_process():
    print("Thank you for using Alex's Budget Manager.")
    print("")
    print("--- RECEIPT ---")
    print("Breakdown: Income ")

    has_income = 'income' in globals()
    has_gift = 'gift_check' in globals()
    has_cost = 'cost_check' in globals()

    if has_income:
        print("+ $", income)

    gift_total = 0
    if has_gift:
        for i in gift_check:
            print(i, ": $", gift_check[i])
            gift_total += gift_check[i]

    print("------")
    print("Breakdown: Charges")
    cost_total = 0
    if has_cost:
        for i in cost_check:
            print(i, ": -$", cost_check[i])
            cost_total += cost_check[i]
    else:
        print("No charges were added! :)")
    print("------")


    if has_income and has_gift and has_cost:
        sum_total = (income + gift_total) - cost_total
    elif has_income and has_gift and not has_cost:
        sum_total = income + gift_total
    elif has_income and not has_gift and has_cost:
        sum_total = income - cost_total
    elif has_income and not has_gift and not has_cost:
        sum_total = income
    elif not has_income and has_gift and has_cost:
        sum_total = gift_total - cost_total
    elif not has_income and has_gift and not has_cost:
        sum_total = gift_total
    elif not has_income and not has_gift and has_cost:
        sum_total = 0 - cost_total
    else:
        sum_total = 0

    if sum_total < 0:
        print(" Your total is - $", sum_total)
    else:
        print(" Your total is $", sum_total)
    print("------")
    if sum_total < 0:
        print("Looks like your underbudget! Start saving!")
    else:
        print("Looks like your in green! :)")


def money_in():
    print("--SECTION 1: Money In--")
    print("1. Manage income.")
    print("2. Manage gift money.")
    print("3. Save and continue.")
    menu_option = int(input())
    while menu_option != 3:
        if menu_option == 1:
            user_income()
        elif menu_option == 2:
            gift_money()
        else:
            print("Invalid option")
        money_in()
        menu_option = int(input())
    money_out()


def main():
    user_startup()


main()