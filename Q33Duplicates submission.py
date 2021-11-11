from typing import Counter


# Duplicates submission_type: Duplicates


num_list = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
new_list=[]
for num in num_list:
    if num not in new_list:
        new_list.append (num)
print("after removing duplicates the list is:",new_list)


# print (set(n))



