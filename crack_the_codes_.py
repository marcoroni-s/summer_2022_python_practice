#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome. What is your name? ")
user_name = input("")


# In[2]:


print("Hello,", user_name + ".", "Are you ready to crack the code?")
user_response = input("")


# In[9]:


if user_response.lower() != "yes":
    print("Goodbye.")
else:
    print()
    print("Please enter a number:")
    first_number = int(input(""))
    
    if first_number != 3:
        print("Sorry, that was incorrect.")
        print("Better luck next time!")
    else:
        print("Correct!")
        print()
        print("Please enter a number:")
        second_number = int(input(""))
        
        if second_number == 1 or 33 <= second_number <= 100:
            print("Correct!")
            print()
            print("Please enter a number:")
            third_number = int(input(""))
            
            if third_number < 0:
                print("Sorry, that was incorrect.")
                print("Better luck next time!")
            else:
                if third_number % 3 == 0 or third_number % 7 == 0:
                    print("Correct!")
                    print("You have cracked the code!")
                else:
                    print("Sorry, that was incorrect.")
                    print("Better luck next time!")
        else:
            print("Sorry, that was incorrect.")
            print("Better luck next time!")
            
            


# In[ ]:




