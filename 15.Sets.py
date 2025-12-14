numbers =(1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10)
name ="liisslaam"
unique_numbers = set(numbers)#تحويل القائمة الى مجموعة
unique_name = set(name)#تحويل النص الى مجموعة
print(unique_numbers)
unique_numbers.add(11)#اضافة عنصر الى المجموعة
unique_numbers.remove(5)#حذف عنصر من المجموعة
print(len(unique_numbers))#طول المجموعة
print(unique_numbers.union({12, 13, 14}))#دمج مجموعتين
print(unique_numbers.intersection({5, 6, 7, 8}))#العناصر المشتركة بين مجموعتين
print(unique_numbers.difference({5, 6, 7, 8}))#العناصر المختلفة بين مجموعتين
print(unique_numbers.symmetric_difference({5, 6, 7, 8}))#العناصر المختلفة بين مجموعتين فقط
print(unique_name)
#المجموعات في بايثون