from itertools import accumulate

##### What does the term first-class function mean?

#### First-Class Functions: First-class functions refer to the ability of a programming language to treat functions as first-class citizens.

#### This means functions can be assigned to variables, 
#### passed as arguments to other functions, 
#### and returned as values from functions.

# First-Class Citizens: In programming languages, first-class citizens are entities that can be manipulated in the same way as other entities, 

# such as variables, literals, and data structures. 
# They have the ability to be assigned to variables, 
# passed as arguments, 
# and returned as values. 



###### This is how we are used to seing functions


def square_it(num):
    return num * num

# print(square_it(5))


## How do we use it?










###### What happens if we try to execute the following code?

squared = square_it
# print(squared(5))











####### It says that squared is some function square_it.. at some address..

#
##
###
####
#####
######    What will this return?

# number_squared = square_it(3)
# print(number_squared)














######################################

## What do we think will happen if we run this code?

# print(squared(9))






#######




# print(squared(squared(3)))














def quartered(num):
    return squared(squared(num))

# print(quartered(3))





#############################
# A Higher Order Function

## Accepts a function ##
##         OR         ##
## Returns a function ##


#############################



# Lets make our own higher order function.

def my_map(my_func, my_list):
    result = []
    for thing in my_list:
        result.append(my_func(thing))
    return result

some_list = [1, 2, 3, 4, 5]
some_func = squared

# print(my_map(some_func, some_list))

########
built_in = list(map(some_func, some_list))

# print(built_in)



def cube(x):
    return x ** 3

cubed_list = list(map(cube, some_list))
# print(cubed_list)


### Filter

### Lets think of a simple way we can apply filter in python

input_list = [44, 35, 7, 8, 99, 105, 140, 460, 999, 3, 44, 32, 5, 4, 3]




###### What are some ways we could filter this?




#### numbers from our list that are less than 10?


### We can make a function that will return a number only if its less than 10
def less_than_ten(num):
    if num < 10:
        return num
    

### Our filter is going to return an iterator, which needs an iterable to be used
## This is why we have list(filter(func, iterable))
    
our_first_filter = list(filter(less_than_ten, input_list))

# print(our_first_filter)


###### Some things to remember
#### Filter uses a function, and an iterable
#### The Function needs to return a Boolean
#### The result of Filter needs to be in an iterable


#### There are some equivalent ways to filter that you will see in the wild

####  They will still need a condition that produces a Boolean
#### And an iterable thing that is being filtered

### Another way to produce our filter from before would be:

##### Note that our loop and condition are still enclosed within a list []
nums_less_than_ten = [num for num in input_list if num < 10]
# print(nums_less_than_ten)


#### Another equivalent you may see in the wild

lambda_nums = list(filter(lambda num: num < 10, input_list))
# print(lambda_nums)

##############################
# You could think of this being similar to a arrow function (anonymous function) in javascript
#const my_list = [1 , 2, 3, 4, 33, 44, 55]
# const doubled_list = my_list.filter((num)=> num < 10)



#################### Reduce

#### In python need to import functools to use
from functools import reduce

##### You can read about functools and reduce in the python documentation.

##### What do we remember about Reduce?

##### Reduce is a higher order function that is going to let us 'reduce' an iterable to just one element

##### The value of the element returned by reduce will depend on the function we pass to reduce

##### If not specified the default operation is going to be adding

### We need a function that has the arguments accumulator, current_value, and optionally initializer

boring_list = [1, 2, 3, 4, 5]

testing_sum = [1, 2, 3, 4, 5]

def the_function(acc, curr):
    return acc + curr

# basic_example = reduce(the_function, boring_list)
# print(basic_example)




subtract_list = [30, 3, 2, 4, 1, 5, 3, 2]

def the_subtract(acc, curr):
    return acc - curr

subtracting = reduce(the_subtract, subtract_list)
# print(subtracting)




### To get a better idea of whats going on, lets take a look at the set-up to using a prefix-sum algorithm.

prefix_example = [1, 4, 0, 5, 3, -2, 5, 10, 4, 2]

prefix = [prefix_example[0]]

for i in range(1, len(prefix_example)):
    prefix.append(prefix_example[i] + prefix[-1])

# print(prefix)



what_is_this_thing = list(accumulate([1, 4, 0, 5, 3, -2, 5, 10, 4, 2]))
# print(what_is_this_thing)


## Lets first take our boring list

accumulator = [boring_list[0]]

for current_value in boring_list[1:]:
    accumulator.append(current_value + accumulator[-1])

# print(accumulator)


#### So we can think of an accumulator as a variable that keeps track of the cumulative result as we iterate through a sequence

#### Current value is the element currently being processed in the sequence, and we notice reduce is giving us the last current value accumulated



#### Ok, what about this thing I saw in the docs about an optional INITIALIZER??


## So far we have used reduce by default (addition), and we have also shown we can also do subtraction

### When we call reduce by default reduce(acc, curr) for a simple list like

## We end up calculating something like 
# 
#  [ 1, 2, 3, 4, 5]
# 
# ((((1 + 2) + 3) + 4) + 5)

##### If we were to write something like:

init_reducer = reduce(lambda acc, val: acc + val, boring_list, 5)


# print(init_reducer)


#### By passing an initializer, we told reduce to start with 5

#### So now we begin calculating something like (((((5+ 1)+2)+3)+4)+5)











sample_strings = ['I wonder what', 'would make it so that', 'we may want to include something. Like a initializer', 'with our reducer', 'Do we have enough text yet???']


char_count = reduce(lambda acc, val: acc + len(val), sample_strings, 20)
# print(char_count)

multiply_list = [-4, 5, 3, 2, 5, 4]
divide_list = [1000, 5, 10, 4, 2]


multiply_reduce = reduce(lambda acc, val: acc * val, multiply_list)
# print(multiply_reduce)

divide_reduce = reduce(lambda acc, val: acc / val, divide_list)
# print(divide_reduce)





###### Okay a small practice problem. Lets see if we can return a string in the format of Code Platon Is Asking For Help..
input_string = "Code Platoon! is ? asking for ! help.. We neEd to fiX th1e senTence to Only hAv3e th3e W0OrdZ from this string"

























# words_string = input_string.split(" ")
# letters_string = list(filter(lambda letter: letter.isalpha(), words_string))
# for i in range(len(letters_string)):
#     letters_string[i] = letters_string[i][0].upper() + letters_string[i][1:].lower()
# print("".join(letters_string))


