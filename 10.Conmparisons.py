#المقارنات في بايثون
#def max(num1 , num2, num3):
    #if num1 >= num2 and num1 >= num3:
      #  return 
    #elif num2 >= num1 and num2 >= num3:   return num2
    #else:
       # return num3
#print(max(10,20,30))
def match_string(str1 , str2):
     if str1 == str2:#لمطابقة التساوي بين النصوص
     #if str1 != str2: #لمطابقة عدم التساوي بين النصوص
        print("The strings do match")
     else:
        print("The Strings dont match")
match_string("Ali" , "Hamza")