import math
print("Choose either 'investment' or 'bond' from the menu below to proceed")
print("")
print("investment   - to calculate the amount of interest you'll earn on investment")
print("bond         - to calculate the amount you'll have to pay on a home loan")
print("")
print("Type 'investment or bond'")
selection = input()
selection = selection.lower()   # Converting any uppercase letters to lowercase so BOND, Bond, bond, INVESTMENT, Investment and investment is handled the same way
print("")
print(selection + " selected")
print("")

if selection == "investment":   # The following statement will only execute when investment is entered
    
    inv_amount = float(input("Enter the amount of money for deposit: "))
    inv_rate = float(input("Enter the interest rate(percentage, without the % sign): "))
    inv_years = int(input("Enter the amount of years you wish to invest for: "))
    interest = input("Enter the type of interest you want to use (simple or compound): ")

    if interest == "simple":    # The following statement will only execute if the interest type selected is simple
        print("")
        print("Amount deposited: R" + str(inv_amount))
        print("Interest rate: " + str(inv_rate))
        print("Years invested for: " + str(inv_years))
        print("Type of interest: " + interest)
        print("")
        
        a = inv_amount*((1+inv_rate/100)*inv_years)     # Simple interest formulae
        a = round(a,2)
        print("Total with interest: R" + str(a))

    elif interest == "compound":    # The following statement will only execute if the interest type selected is compound
        print("")
        print("Amount deposited: R" + str(inv_amount))
        print("Interest rate: " + str(inv_rate))
        print("Years invested for: " + str(inv_years))
        print("Type of interest: " + interest)
        print("")
        
        a = inv_amount* math.pow((1+inv_rate/100),inv_years)    # Compound interest formulae
        a = round(a,2)
        print("Total with interest: R" + str(a))

    else:   # This statement executes if the user has not selected between simple or compound interest
        print("Error, you have not chosen simple OR compound. Please try again")

elif selection == "bond":   #This statement will execute if the selection type is bond

    print("")
    b_amount = float(input("Enter the present value of house: "))
    b_interest = float(input("Enter the annual interest: "))
    b_months = float(input("Enter the number of months over which the bond will be repaid: "))
    print("")
    print("Present value: R" + str(b_amount))
    print("Annual interest: " + str(b_interest) + "%")
    print("Monthly interest: " + str(round((b_interest/12),2)) + "%")   # Monthly interest calculated by deviding annual interest by 12
    print("Repayment months: " + str(b_months))
    print("")
    
    x = (((b_interest/100)/12)*b_amount)/(1-((1+((b_interest/100)))**(-1*b_months))) # Bond repayment formulae

                                          
    print("Total repayment per month: R" + str(round(x,2)))

else:   # This statement executes if the user has not typed bond or investment correctly
    print("You have not made a valid selection")





                                          
