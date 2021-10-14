#Author: Lucas Johnston-Flanagan
#date: 2021-10-13
#filename: functions.py
#Description: An example program floatroducing functions

#One way to think of a function is as a 'mini program' within a program. 
#It is only run when it is "called".

#We have actually used functions before! any time we use something like:
    #input()
    #print()
    #round()
    #random.randrange()
#Notice a theme? 
#Functions always appear in the form:
    #function_name(parameters) 
    #Where function_name is the name of the function
    #And the parameters are variables or literals that the function operates on. 
#Not all functions have parameters (like .lower() or .upper() )
#Usally we define all functions at the top of our code (before our "main" code)

#Though there are many (many) built in functions in Python, we can acutally create our own!
#here is the basic format of how to create a function in pyhton
def sample_display(parameter1, parameter2): #note that you can have more or less parameters, as needed.
    #not the identation level! (just like with if statements and loops)
    print(f"{parameter1:10}{parameter2:10}")


#Let's look at a more complex example: An addition calculator 
def add_calculator (num_1, num_2):
    total = float(num_1) + float(num_2)
    return total #what is a return?
    #A return statement "returns" the literal or variable that appears after it back to where we left it in the main code.

#We can have functions that include loops and if statements with-in them as well!
def avd_calculator(num_1, num_2, operator):
    #notice how I can use the same variable names in this function as I did in another.
    #That is because the "scope" of these variables is contained within  just this function.
    if operator == "+":
        total = float(num_1) + float(num_2)
    elif operator == "-":
        total = float(num_1) - float(num_2)
    elif operator == "/":
        total = float(num_1) / float(num_2)
    elif operator == "*":
        total = float(num_1) * float(num_2)
    elif operator == "**":
        total = float(num_1) ** float(num_2)
    return total
#"Main code"
sample_display("Example", "Table")    #notice how "Example" and "Table" are printed even though we didn't directly print them!

print (add_calculator (4 , 10)) #This will add 4 and 10, then print it (as our function is called)

#We can use variables instead of literals for our function 
userinput1 = input("Enter your first number: ")
userinput2 = input("Enter your second number: ")
total = add_calculator(userinput1, userinput2)
print("The total is: " + str(total))

#And we can even do this all in one line (if we don't need to save the user input)
print("Your numbers added together are: " + str(add_calculator(input("Enter your first number: "),input("Enter your second number: "))))

#Let's look at a more complex function 
user_op = input("What kind of math do you want to do? (+, -, /, *, **)")
user_num1 = input("Enter your first number: ")
user_num2 = input("Enter your second number: ")

print(user_num1 + " " + user_op + " " + user_num2 + " = " + str(avd_calculator(user_num1, user_num2, user_op)))

#Practice Program: Functions
    #Create a program that includes the use of at least 2 custom functions.
        #at least one of the functions should have parameters
        #at least one of the functions should have conditionals (if statements) within it
        # at least one of the funcitons should have reprition (loops) within it.  