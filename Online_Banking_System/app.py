import logging as lg
import balance,deposit,transfer,withdraw,history,exit
lg.basicConfig(
    filename = "app.log",
    level = lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s] - %(message)s"
)

# total operations
operations = (
    "1. Balance\n"
    "2. Withdraw\n"
    "3. Deposit\n"
    "4. Transfer\n"
    "5. History\n"
    "6. Exit\n"
)

# Account Table
account_table = {
    12345:6789,
    54321:9876
}

# Users Table
users_table = {
    12345:['GSamaira','samairag456@gmail.com',10000],
    54321:['GKundana','gkundana1025@gmail.com',50000]
}

# Checking Valid User
def valid_user(user_name:int,password:int):
    lg.debug("User in login page")
    if user_name in account_table:
        if account_table[user_name] == password:
            lg.info("User successfullt loggined")
            print("User successfullly loggined")
            return True
        else:
            lg.warning("Please check your login credentials")
            print("Please check your login credentials")
            return False
    else:
        lg.warning("Please check your login credentials")
        print("Please check your login credentials")
        return False

# Choose_operation function definition
def choose_operation(account_no, choice):
    lg.info(f"Selected Operation is {operations[choice-1]}")
    val = False
    if choice == 1:
        balance.balance(user_name=account_no)
    elif choice == 2:
        withdraw.withdraw(user_name=account_no)
    elif choice == 3:
        deposit.deposit(user_name=account_no)
    elif choice == 4:
        transfer.transfer(user_name=account_no)
    elif choice == 5:
        history.history(user_name=account_no)
    elif choice == 6:
        val = exit.exit_fun()
    else:
        print("Enter choice between (1-6)")
    if val:
        return val
    
if __name__ == "__main__":
    print("Welcome to the Online Codegnan Banking")
    lg.info("Welcome to the Online Codegnan Banking")
    user_name = int(input("Please, Enter account number: "))
    password = int(input("Please, Enter pin number: "))
    lg.info(f"User credentials are {user_name} and {password}")
    while True:
        if valid_user(user_name,password):
            print(*operations)
            lg.info(operations)
            choice = int(input("Please select operation (1-6): "))
            exit_fun_val = choose_operation(account_no = user_name ,choice = choice)
            if exit_fun_val:
                break
        
        else:
            lg.warning("User not found, Please check with your login credentials")
            print("User not found, Please check with your login credentials")


    