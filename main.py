n = input ('Количесвто лет ')
if int(n)%10>=5 and int(n)%10<10:
    print ('Вам '+ n + ' лет')
elif int(n)%10<=4 and int(n)%10>1:
    print ('Вам '+ n + ' года')
else:
    print ('Вам '+ n + ' год')
