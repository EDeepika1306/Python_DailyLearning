"""
Read 10 number find the sum and average
"""
sum=0
num=[]
for i in range(10):
    num=int(input("Enter the number"))
    sum=sum+num
    avg=sum/10
print(sum)
print(avg)
