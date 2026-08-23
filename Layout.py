#Requirements/Planning

#Money_In
#-----------------------
#Income - Weekly, Monthly
#Gift_Money - Custom Amount per Month
#Current Balance

#Money_Out
#---------------------------------
#Rent/Housing
#Food
#Transportation
#Entertainment
#Subscription
#Misc (Custom)


#Calc
#Total Spent
#Money Remaining
#Spending per category
#Over/under budget


#Pseudocode

#Central Code

#Greet user and ask how many days the user wants to budget for
    #The following will be saved to budget_days

#Ask if user wants to create a budget or already has budget

#If user already has a budget
    # if there is any updates needed for Money_In or Money_Out
          # if so, ask which one and run that process again
    # After run the end process
#Else, create a new budget running functions money in and money_out
     # After run the end process


#Function: Money_In()
#Purpose: Quantify the deposable income

# Ask the number of their current balance
# Ask if they have income or gift_money
# Run the following function which would define income/gift_money variable

#Function Name: Income()
#Purpose: Track income

# Ask user if they make weekly or monthly income
   # If weekly, take their weekly income and multiply it by (budget_days/7)
   # If monthly, take their weekly income and multiply it by (budget_days/30)

#Function: Gift_Money()
#Purpose: Factor in additional one time payments
  #LOOP: START
    # Ask them to enter an additional one-time payment
    # Ask the name they'd like to name it
    # Ask if they want another additional payment or want it to end
  #END


#Function: Money_Out()
#Purpose: Quantify the damage
# Create a menu that allows to edit each function
    #--- MONEY OUT---#
    #Rent/Housing -----> Housing()
    #Food -----> Food()
    #Transportation ------> Transportation()
    #Entertainment -----> Entertainment()
    #Subscription -----> Subscription()
    #Misc (Custom) -----> Misc()
    # Calculate Budget! ----> end_process()


#Function: Housing()
# Ask user if they have monthly or yearly lease
   # If monthly, take cost and multiply it by (budget_days/30)
            # Save into Housing_Weekly_Payment
# If yearly, take the cost and multiply it by (budget_days/30)
            # Save into Housing_Weekly_Payment

#Function: Food()
# Ask user if they make weekly, monthly, or daily payments
   # If weekly, take their weekly payments and multiply it by (budget_days/7)
        #Save into Food_Weekly_Payment
   # If monthly, take their weekly payments and multiply it by (budget_days/30)
        #Save into Food_Monthly_Payment
   # If daily, take their payment and multiply it by budget_days
        # Save into Food_Daily_Payment

#Function: Transportation()
# Ask user if they make weekly, monthly, or daily payments
   # If weekly, take their weekly payments and multiply it by (budget_days/7)
        #Save into Transportation_Weekly_Payment
   # If monthly, take their weekly payments and multiply it by (budget_days/30)
        #Save into Transportation_Monthly_Payment
   # If daily, take their payment and multiply it by budget_days
        # Save into Transportation_Daily_Payment

#Function: Entertainment
# Ask user if they make weekly, monthly, or daily payments
   # If weekly, take their weekly payments and multiply it by (budget_days/7)
        #Save into Entertainment_Weekly_Payment
   # If monthly, take their weekly payments and multiply it by (budget_days/30)
        #Save into Entertainment_Monthly_Payment
   # If daily, take their payment and multiply it by budget_days
        # Save into Entertainment_Daily_Payment

#Function: Subscription
# Ask user if they make weekly, monthly, or daily payments
   # If weekly, take their weekly payments and multiply it by (budget_days/7)
        #Save into Subscription_Weekly_Payment
   # If monthly, take their weekly payments and multiply it by (budget_days/30)
        #Save into Subscription_Monthly_Payment
   # If daily, take their payment and multiply it by budget_days
        # Save into Subscription_Daily_Payment

#Function Misc (Custom)
  #LOOP: START
    # Ask them to enter an additional one-time payment
    # Ask the name they'd like to name it
# Ask user if make it weekly, monthly, daily or yearly payments
   # If weekly, take their weekly payments and multiply it by (budget_days/7)
        #Save into name_Weekly_Payment
   # If monthly, take their weekly payments and multiply it by (budget_days/30)
        #Save into name_Monthly_Payment
   # If daily, take their payment and multiply it by budget_days
        # Save into name_Daily_Payment
    # If yearly, take the cost and multiply it by (budget_days/30)
       # Save into name_Yearly_Payment
# Ask if they want another additional payment or want it to end
  #END



#Function: end_process()
# Receipt
# print every variable from money in
# print every variable from money out
# add every variable from money in together
# add every variable from money out
# subject money_in_sum - money_in_sum
# If total_sum > positive 
    #Print total_sum
# Else
    #Print You are underbudget!, print total_sum







