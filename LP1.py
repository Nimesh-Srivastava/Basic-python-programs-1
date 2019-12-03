#x = int(input("Input x : "))
#y = int(input("Input y : "))
#print("\nSum = " + str(x+y))
#if(x>y) :
#    print("\nDifference is = " + str(x-y))
#else :
#    print("\nDifference is = " + str(y-x))
#print("\nMultiplication is = " + str(x*y))
#print("\nDivision x/y is = " + str(x/y))
#print("\nDivision y/x is = " + str(y/x) +"\n\n")


#a = input("Write a true sentence(T) : ")
#b = input("Write a false sentence(F) : ")
#a = True
#b = False
#print("T and F : " + str(a and b))
#print("T or F : " + str(a or b))
#print("not T : " + str(not a))



#x = int(input("Input the number of items : "))
#i = 0
#b = 0
#a = 0
#while (i < x) :
#    a = int(input("Enter element " + str(i+1) + " : "))
#    b = b + a
#    i = i+1
#print("Average = " + str(b/x))
 


x = int(input("Input the number of items : "))
a = []
for i in range(0,x) : 
    y = int(input("\nEnter element " + str(i+1) + " : "))
    a.append(y)
i = 0
for i in range(0,x-1) :
    if(a[i+1]<a[i]):
        j = i
        while(j>=0):
            if(a[j+1]<a[j]):
                b = a[j]
                a[j] = a[j+1]
                a[j+1] = b
            j=j-1
i = 0
print("\nList = " + str(a))
if(x%2!=0):
    print("\nMedian = " + str(a[x//2]))
else:
    x=x+1
    print("\nMedian = " + str(a[x//2]))