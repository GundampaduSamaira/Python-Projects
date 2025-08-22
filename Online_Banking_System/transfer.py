import app

# Transfer Amount function
def transfer(user_name):
    app.lg.debug("User in transfer page")
    receiver_account = int(input("Enter Receiver account number: "))
    amount = int(input("Enter amount: "))
    app.lg.info(f"receiver account is {receiver_account} and amount is {amount}")
    current_amount = app.users_table[user_name][2]
    if receiver_account in app.users_table:
        if current_amount >= amount:
            # amount updation in users table
            app.users_table[user_name][2] -= amount
            app.users_table[receiver_account][2] += amount
            app.lg.info(f"{amount} transfer successful and current balance is {app.users_table[user_name][2]}")
            print(f"{amount} transfer successful and current balance is {app.users_table[user_name][2]}")
        else:
            app.lg.warning("Insufficient amount")
            print("Insufficient amount")
    else:
        app.lg.warning(f"{receiver_account} not found")
        print(f"{receiver_account} not found")