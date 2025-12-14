# الادوات الشرطية في بايثون
is_hungry = False
wants_to_eat = True
#تغير القيمه من صح الى خطا او العكس
#تتغير المخرجات حسب القيمه
#if is_hungry or wants_to_eat:#لو هناك شرط
if is_hungry and wants_to_eat:#لو هناك شرط
    print("I'm Hungry")
elif is_hungry and not wants_to_eat: #لو كان هناك شرط اخر
    print("I'm Hungry But I don't want to eat")
elif not is_hungry and wants_to_eat:
    print("I'm Not Hungry But I want to eat")
else:#لو لم يكن هناك شرط
    print("I'm Not Hungry")
    