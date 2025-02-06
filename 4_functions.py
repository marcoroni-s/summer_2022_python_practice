#!/usr/bin/env python
# coding: utf-8

# In[1]:


def display_vowel_info(input):
    if len(input) == 0:
        x = print("The string must not be empty")
        return x
    else:
        y = print("The sentance", '"'+input+'"', "has", len(input), "characters, and there are:")
        return y
    
    initial_a = 0
    initial_e = 0
    initial_i = 0
    initial_o = 0
    initial_u = 0

    for character in input:

        lowercase_character = character.lower()
        if lowercase_character == 'a':
            initial_a = initial_a + 1
        elif lowercase_character == 'e':
            initial_e = initial_e + 1
        elif lowercase_character == 'i':
            initial_i = initial_i + 1
        elif lowercase_character == 'o':
            initial_o = initial_o + 1
        elif lowercase_character == 'u':
            initial_u = initial_u + 1
            
    print(initial_a, "a's")
    print(initial_e, "e's")
    print(initial_i, "i's")
    print(initial_o, "o's")
    print(initial_u, "u's")


# In[2]:


display_vowel_info("mama")


# In[3]:


def display_vowel_info(input):
    if len(input) == 0:
        print("The string must not be empty")
    else:
        print("The sentence", '"'+input+'"', "has", len(input), "characters, and there are:")

        initial_a = 0
        initial_e = 0
        initial_i = 0
        initial_o = 0
        initial_u = 0

        for character in input:
            lowercase_character = character.lower()
            if lowercase_character == 'a':
                initial_a = initial_a + 1
            elif lowercase_character == 'e':
                initial_e = initial_e + 1
            elif lowercase_character == 'i':
                initial_i = initial_i + 1
            elif lowercase_character == 'o':
                initial_o = initial_o + 1
            elif lowercase_character == 'u':
                initial_u = initial_u + 1

        print(initial_a, "a's")
        print(initial_e, "e's")
        print(initial_i, "i's")
        print(initial_o, "o's")
        print(initial_u, "u's")


# In[4]:


def print_rectangle(base, height, character):
    if int(base) <= 0 or int(height) <= 0:
        print("Sides must be positive integers")
    else:
        for vertical in range(height):
            for horizontal in range(base):
                print(str(character), end = "")
            print()


# In[5]:


x = input("What shoudl the character be")
print_rectangle(3,4,x)


# In[6]:


def num_negatives(theList):
    if len(theList) == 0:
        print("List must be greater than zero")

    for x in theList:
        start = 0
        if x < 0:
            start = start + 1
            
        return start 


# In[7]:


list = [-3, -4, 0, 1]


# In[8]:


num_negatives(list)


# In[9]:


def num_negatives(theList):
    if len(theList) == 0:
        print("List must be greater than 0")

    start = 0  

    for x in theList:
        if x < 0:
            start = start + 1

    return start



# In[ ]:





# In[14]:


def negatives(theList):
    if len(theList) == 0:
        print("List must be greater than 0")
    
    negative_list = []

    for num in theList:
        if num < 0:
            negative_list.append(num)

    return negative_list


# In[18]:


list = [-3, -4, -5]
negatives(list)
num_negatives(list)


# In[ ]:





# In[19]:


def negatives(theList):
    if len(theList) == 0:
        print("List must be greater than 0")
    
    negative_list = []

    for num in theList:
        if num < 0:
            negative_list.append(num)

    return negative_list

# Example usage
my_list = [-3, -4, -5]
print(negatives(my_list))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[22]:


#**************************************************************************
# * Name: Marco Soto                                                
# * Date: 07/01/2022                                                   
# *************************************************************************
# * Problem Statement and Specifications: 
# * complete 4 different functions that are under the name methods.py which will be imported by 
# * methods_test.py 
# * Input:  
# * Inputs listed below already 
# *
# * Output: 
# *
# * Outputs listed below already 
# *************************************************************************


# ****** COMPLETE THE FOLLOWING METHODS BELOW ******

# @param input a string   
# Precondition: input must be a non-empty string 
# Postcondition: display the input string, the number of characters in the input string, 
# as well as the counts for all vowel types in the input string. 

def display_vowel_info(input):
	
    if len(input) == 0:
        print("The string must not be empty")
    else:
        print("The sentence", '"'+input+'"', "has", len(input), "characters, and there are:")

        initial_a = 0
        initial_e = 0
        initial_i = 0
        initial_o = 0
        initial_u = 0

        for character in input:
            lowercase_character = character.lower()
            if lowercase_character == 'a':
                initial_a = initial_a + 1
            elif lowercase_character == 'e':
                initial_e = initial_e + 1
            elif lowercase_character == 'i':
                initial_i = initial_i + 1
            elif lowercase_character == 'o':
                initial_o = initial_o + 1
            elif lowercase_character == 'u':
                initial_u = initial_u + 1

        print(initial_a, "a's")
        print(initial_e, "e's")
        print(initial_i, "i's")
        print(initial_o, "o's")
        print(initial_u, "u's")



	
	
	
	
	

# @params base the base length of the rectangle as a positive integer
#		  height the height of the rectangle as a positive integer
#         character the character used to print the rectangle  
# Precondition: base and height must be positive integers, character must be a valid
#				keyboard character
# Postcondition: prints the rectangle with dimensions base x height using the
# 				 specified character

def print_rectangle(base, height, character):
	
    if int(base) <= 0 or int(height) <= 0:
        print("Sides must be positive integers")
    else:
        for vertical in range(height):
            for horizontal in range(base):
                print(str(character), end = "")
            print()	
	
	
	
	
    
    
    
      
      
# @params theList a list of numerical values
# @return the number of negative numbers in the list           
# Precondition: theList is non-empty 
# Postcondition: returns number of negatives
def num_negatives(theList):

    if len(theList) == 0:
        print("List must be greater than 0")

    start = 0  

    for x in theList:
        if x < 0:
            start = start + 1

    return start	
	
	
	
	
		
	



	
# @params theList a list of numerical values
# @return a list containing only the negative numbers in the list           
# Precondition: theList is non-empty 
# Postcondition: returns a list of all negative numbers in the list
def negatives(theList):

			
    if len(theList) == 0:
        print("List must be greater than 0")
    
    negative_list = []

    for num in theList:
        if num < 0:
            negative_list.append(num)

    return negative_list					        

 







# import methods

infoString = ('This program asks the user for a sentence,\n'
         'searches the sentence for all vowels,\n'
         'and displays the number of times each vowel appears in the sentence.\n')

print(infoString)
       
# prompt for input    
sentence = input('Enter a sentence: ')

display_vowel_info(sentence)

# prompt for input
base = int(input('Enter a positive integer for the base of the rectangle: ')) 
height = int(input('Enter a positive integer for the height of the rectangle: '))
character = (input('Enter a character used to print the rectangle: '))
print()

# print the rectangle by calling the printRectangle function
print_rectangle(base, height, character)
print()

# prompt the user to enter a list of numbers and store them in a list
list = [float(x) for x in input('Enter some numbers separated by whitespace ').split()]

print()    

# output the number of negatives    
print('The number of negatives in the list is', num_negatives(list))

# output the list of negatives numbers    
print('The negatives in the list are ', end = '') 
    
for items in negatives(list):
    print(items, ' ', sep = '', end = '') 
    
print('\n')


 


# In[ ]:




