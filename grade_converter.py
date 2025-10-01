# FILE NAME - grade_converter.py

# NAME: 
# DATE: 
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

print('===== Grade Converter =====')

percent = int(input('Enter a numerical grade (1-100): '))

#print(list(range(80,90)))

if percent > 100:
    print('A+')
#elif percent in range(90, 100):
elif percent >= 90:
    print('A')
elif percent >= 80:
    print('B')
elif percent >= 70:
    print('C')
elif percent >= 65:
    print('D')
else:
    print('F')

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?

There is a difference between if-if-else and if-elif-else!
Make sure you write statements in your correct order to solve the problem you have in front of you.






'''
