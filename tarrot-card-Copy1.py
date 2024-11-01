#!/usr/bin/env python
# coding: utf-8

# In[8]:


from constraint import Problem

# Ask the user for their horoscope
horoscope = input("What is your Horoscope? ")

# Define the names of the horoscopes and character traits
horoscope_names = ['Aries', 'Sagittarius', 'Leo', 'Cancer', 'Pisces', 'Aquarius', 'Capricorn']
good_character_traits = ['Happy', 'Sad', 'Feeling Doechi']
bad_character_traits = ['Angry', 'Mad', 'Loving']
character_traits = good_character_traits + bad_character_traits

# Create a constraint problem
problem = Problem()

# Add variables and their possible values to the problem
for name in horoscope_names:
    problem.addVariable(name, character_traits)

# Define a single custom constraint function
def myConstraint(sagittarius, aries):
    if sagittarius != aries:
        return True
    return False

# Add the custom constraint to the problem
problem.addConstraint(myConstraint, ["Sagittarius", "Aries"])

# Get solutions that satisfy the constraints
solutions = problem.getSolutions()

# Print the solutions
for solution in solutions:
    print(solution)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




