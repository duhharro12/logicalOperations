'''
Created on Feb 15, 2020

@author: ITAUser
'''
#1)
# )Broken: Change the code so it returns True
# )4 !== 4 and 3 == 3
# )Correct:
(4==4) and (3==3)
#2
# )Broken: Change the code so it returns True
# )3**2 == 3+2 or 1+2 <= 3 and !True
# )Correct:
not(3**2==3+2) or (1+2<=3)
#3)
# )Broken: Change it so it returns False
# )(True and False) or (True or false)
# )Correct:
not(True and False) or not(True or False)

#4)
# )Broken: Make the code return True
# )((5==5) and 4<3) and not(True and 8**2 >= 64)
# )Correct:
((5==5) and not(4<3)) and (True and (8**2>=64))
#5)
# )Broken:Make the code return False
# )a = True
# )b = False
# )((a or b) and a) or (a or b)
# )Correct:
(not(a) or (b)) or (not(a) or (b))
#6)
# )Broken: make the code return True
# )a = True
# )b = False
# )not(a or b) and a
# )Correct:
(not(not(a) or (b)) and (a)
