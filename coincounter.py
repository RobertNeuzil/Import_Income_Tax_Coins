import math

print ("""Only Enter Numerical Values

	""")


def runprogram():
    x = 1
    try:
        pennies = int(input("Enter amount of pennies: "))

        nickels = int(input("Enter amount of nickels: "))

        dimes = int(input("Enter amount of dimes: "))

        quarters = int(input("Enter amount of quarters: "))
    except ValueError:
        print ("""

                Invalid Character. Please a start over

        
                                                                            """)
        if True:
            runprogram()
        return False

    
    pennies = pennies * 0.01
    nickels = nickels * 0.05
    dimes = dimes * 0.10
    quarters = quarters * 0.25

    rawtotal = pennies + nickels + dimes + quarters
    rawtotal = round(rawtotal, 2)

    print ("""
                             """ + "You have " + "$" + str(rawtotal) + " dollars")

    


runprogram()

    



