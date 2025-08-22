import app

# Withdraw Amount function
def withdraw(user_name):
    app.lg.debug("User in Withdraw page")
    amount = app.users_table[user_name][2]
    withdraw_amount = int(input("Please enter withdraw amount: "))
    if amount >= withdraw_amount:
        app.users_table[user_name][2] -= withdraw_amount
        app.lg.info(f"{withdraw_amount} withdraw successful and current balance is {app.users_table[user_name][2]}")
        print(f"{withdraw_amount} withdraw successful and current balance is {app.users_table[user_name][2]}")