import app 

# Checking User Balance function
def balance(user_name:int):
    app.lg.debug("User in Balance page")
    if user_name in app.users_table:
        amount = app.users_table[user_name][2]
        app.lg.info(f"{user_name} user current balance is {amount}")
        print(f"{user_name} user current balance is {amount}")
    else:
        app.lg.warning("User not found")
        print("user not found")
