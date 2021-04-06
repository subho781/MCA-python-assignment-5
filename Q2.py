'''Write a function that takes a sentence as an input 
parameter and displays the number of words in the 
sentence'''

test_string = "This is Python Programming assignment"
print ("The original string is : " + test_string)
res = len(test_string.split())
print ("The number of words : " + str(res))
