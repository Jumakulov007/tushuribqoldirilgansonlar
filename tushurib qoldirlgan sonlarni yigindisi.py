import os
os.system("cls")
ls=[]
sch=0
sch1=0
n=int(input("Nechta son kiritasiz?: "))
for x in range(n):
    x=int(input(f"x[{sch}]="))
    sch+=1
    ls.append(x)
a=(max(ls))
b=(min(ls))
for x in range(b,a,1):
    if x not in ls:
        sch1+=x
print("Tushib qolgan sonlarni yigindisi: ",sch1)