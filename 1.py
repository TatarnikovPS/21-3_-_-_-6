try:
    a=int(input("Введите длину массива: "))
except ValueError:
    print("Вы допустили ошибку при вводе данных, попробуйте снова")
    a=int(input("Введите длину массива: "))
ARRAY=[0]*a
for i in range (a):
    try:
        ARRAY[i]=float(input("Введите число массива: "))
    except ValueError:
        print("Вы допустили ошибку при вводе данных, попробуйте снова")
        ARRAY[i]=float(input("Введите число массива: "))
    if(i==0):
        minB=ARRAY[i]
    elif minB>ARRAY[i]:
        minB=ARRAY[i]
try:
    DELTA=int(input("Введите дельту: "))
except ValueError:
    print("Вы допустили ошибку при вводе данных, попробуйте снова")
    DELTA=int(input("Введите дельту: "))
print("Вывод: ",ARRAY.count(minB+DELTA))
