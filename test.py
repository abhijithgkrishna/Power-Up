# number = int(input("Enter number "))

# if number > 5:
#     if number > 10:
#         print("big number")
#     else :
#         print("Not so big number")
# else :
#     print("Small number")


#  nested loops

# for i in range(10): # 0 1 2 3 4 5 6 7 8 9
#     for j in range(3): # 0 1 2
#         print(i+j, end=" ")
#     print("")
    

# 0 1 2 
# 1 2 3 
# 2 3 4
# 3 4 5
# 4 5 6
# 5 6 7
# 6 7 8
# 7 8 9
# 8 9 10
# 9 10 11


# Pattern Printing

#       0
# *     1
# **    2
# ***   3
# ****  4

num = int(input("Enter a number"))
for i in range(num): # 0 1 2 3 4
    for j in range(i+1):
        print("*", end="") 
    print()

# Demonstration with example input
# Enter a number 5
# *
# **
# ***
# ****
# *****
