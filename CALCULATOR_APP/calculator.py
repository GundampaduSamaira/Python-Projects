# importing modules
import addition,subtraction,multiplication,division,modulusDivision


operations = (
    "1. Addition \n",
    "2. Subtraction \n",
    "3. Multiplication \n",
    "4. Division \n",
    "5. Modulus Division \n",
    "6. Exit \n"

)

# main function
if __name__ == "__main__":
    print("-----Calculator-----")
    while True:
        print(*operations)
        choice = int(input("Select Operation between 1 and 5: "))
    

        if choice == 1:
            a, b = map(int,input("Please enter two values with space: ").split())
            res = addition.add(a,b)
            print(f"Addition of given two values is: {res}")
        elif choice == 2:
            a, b = map(int,input("Please enter two values with space: ").split())
            res = subtraction.subtract(a,b)
            print(f"Subtraction of given two values is: {res}")
        elif choice == 3:
            a, b = map(int,input("Please enter two values with space: ").split())
            res = multiplication.multiply(a,b)
            print(f"Multiplication of given two values is: {res}")
        elif choice == 4:
            a,b = map(int,input("Please enter two values with space: ").split())
            res = division.divide(a,b)
            print(f"Division of given two values is: {res}")
        elif choice == 5:
            a,b = map(int,input("Please enter two values with space: ").split())
            res = modulusDivision.modDivision(a,b)
            print(f"Modulus Division of given two values is: {res}")
        else:
            print("-----End-----")
            exit()
    




