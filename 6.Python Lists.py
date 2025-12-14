 # 1القوائم
Frende =[1 ,2,3,4,5,"Ahmed","Ali","Mohamed"]
#print(Frende)
print(Frende[0])#الوصول الى عنصر في القائمة
print(Frende[-1])#الوصول الى اخر عنصر في القائمة
print(Frende[1:4])#الوصول الى مجموعة عناصر في القائمة
Frende[0]="Sayed"#تغيير عنصر في القائمة
# 2القوائم
Hamza =["Hamza","Sayed","Ali"]
tutorial =["Python","Java","C++"]
Hamza.append("Omar")#اضافة عنصر في نهاية القائمة
Hamza.insert(1,"Khaled")#اضافة عنصر في موقع معين في القائمة
Hamza.remove("Ali")#حذف عنصر من القائمة
Hamza.pop()#حذف اخر عنصر من القائمة
Hamza.sort()#ترتيب القائمة
Hamza.reverse()#عكس ترتيب القائمة
print(len(Hamza))#طول القائمة
print(Hamza.index("Sayed"))#موقع عنصر في القائمة
#Hamza += tutorial#دمج قائمتين
print(Hamza)