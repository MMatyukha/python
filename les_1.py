#----------------------------1--------------------------------------------------------
x=int(input("at the end of the time period"))
y="everything goes back to the original point"
print(y,x)

#---------------2---------------------------------------------------------------------
s=int(input('sec='))
hour = (s * 0.00027)
min = (s - hour * 3600) / 60
sec = s - hour * 3600 - min * 60
print(round(hour,2),':',round(min,2),':',round(sec,2))

#---------------------------------------------3-------------------------------------------
n = int(input("number n: "))
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
c = n + int(t1) + int(t2)
print("resalt :", c)
#-----------------------------------------4-----------------------------------------------
n = int(input("number:"))
m = n%10
n = n//10
while n > 0:
    if n%10 > m:
        m = n%10
    n = n//10
print(m)
#------------------5-------------------
n = float(input("profit margin:"))
m = float(input("costs:"))
r=n-m
if r>0:
    print ('compliment',' benefit=')
    print('yield :',r/n)
    per=int(input("persional:"))
    print("salary =",r/per)
elif r<0:
    print("You must do better")
else:
     print("zero  - it  is Ok")
#6--------------------------------------------------------
x = float(input('Start :'))
y = float(input('Finish :'))
d = 1
while y - x > 0:
    x = x + (x * 0.1)
    d += 1
print('Finish  result=',d, 'day')