variable="af23@3Gb2209mf3&)h"
print(len(variable))
character=count=special_characters=0
for c in variable:
    if c.isalpha():
        character+=1
    elif c.isdigit():
        count+=1
    else:
        special_characters+=1
print("list of characters   ",character)
print("list of digits  ",count)
print("list of special characters   ",special_characters)