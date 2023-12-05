m=0
x=int(input('enter 1st: '))
y1=int(input('enter 2nd: '))
z=str(input('enter ope: '))

if z=='+':
    m=x+y1
    print(m)

elif z=='-':
    m=x-y1
    print(m)

elif z=='*':
    m=x*y1
    print(m)

elif z=='/':
    m=x//y1
    print(m)

else:
    print("Enter +,-,/,* operators only")

n=str(input("Do you want 2 continu or not yes/no :")).lower()

v=True

if n=='yes':
    while v:
        y2 = int(input('enter number: '))
        z2 = str(input('enter operator: '))
        if z2 == '+':
            m += y2
            print(m)

        elif z2 == '-':
            m -= y2
            print(m)

        elif z2 == '*':
            m *= y2
            print(m)

        elif z2 == '/':
            m //= y2
            print(m)

        else:
            print("Enter +,-,/,* operators only")
        f=str(input("Do you want to continue or not yes/no :")).lower()
        if f=='yes':
            continue
        elif f=='no':
            print('final result is: ',m)
            v=False
        else:
            print("Enter yes/no only")

else:
    print(m)