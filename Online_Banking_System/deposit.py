import app

# Deposit Amount function
def deposit(user_name):
    app.lg.info("User in deposit page")
    deposit_amount = int(input("Please enter amount: "))
    if user_name in app.users_table:
        app.users_table[user_name][2] += deposit_amount
        app.lg.info(f"{deposit_amount} deposit successful and current balance is {app.users_table[user_name][2]}")
        print(f"{deposit_amount} deposit successful and current balance is {app.users_table[user_name][2]}")
