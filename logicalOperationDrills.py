'''
Created on Feb 15, 2020

@author: ITAUser
'''
#1) 4 == 5 and 5 == 5
False
#2) 5 == 5 or 5 == 4
True
#3) not 3 == 3
False
#4) a = 2
# ) not a == 2
False
#5) a = 3
# ) b = 2
# ) a == b and b == 4
False
#6) a = 4
# ) b = 4
# ) a == b or b == 4
True
#7) a = 6
# ) b = (12/2)
# ) a == b and b == (24/4)
True
#8) a = (3/3)
# ) b = (13/13)
# ) a == b or b == 1
True
#9) a = 3
# ) b = math.sqrt(9)
# ) c = 2
# ) a == b and b == c
False
#10) a = "word"
#  ) b = "Word"
#  ) c = "Word"
#  ) a == b or b == c
True
#11) (10/5) == (12/6) and math.sqrt(9) == 3
True
#12) (14/7) == (15/5) or math.sqrt(9) == 3
True
#13) a = 10
#  ) b = 5
#  ) (a/b) == 2 and 2 == 1
False
#14) a = 10
#  ) b = 5
#  ) (a/b) == (12/6)
True
#15) a = 10
#  ) b = 5
#  ) c = 12
#  ) d = 6
#  ) (a/b) == (12/6) and (c/2) == d
True
#16) a = "something"
#  ) b = "some thing"
#  ) a == b and b == 2
False
#17) a = "word"
#  ) b = "word"
#  ) word = "incorrect"
#  ) a == b and b == word
True
#18) a = True
#  ) a == True and not True == False
True
#19) a = True
#  ) b = False
#  ) a == b or not a == b
True
#20) a = True
#  ) A = False
#  ) b = False
#  ) A == b or a == b
True
