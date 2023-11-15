#Create a Python file named lab_7-2.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Create a function called find_sum()
def find_sum(num1,num2):
#Add the parameters num1 and num2 to the definition of find_sum()
#Add statements to the function that adds the arguments passed to num1 and num2 and stores them in a new variable num_sum
    num_sum = num1 + num2
#Finish the function with a statement that returns num_sum
    return num_sum
#Create a statement that calls the function to find the sum of 111 and 222. Set it equal to the variable my_sum
my_sum = find_sum(111,222)
#Add another print statement after the previous statement that prints my_sum
print(my_sum)
#What happens when you run the program?
    #It prints 333 the sum of 111 and 222