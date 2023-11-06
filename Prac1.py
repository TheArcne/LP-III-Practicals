#Practical 1

#Non-Recursive-----------
import time

def non_recursive(n):
    a=0
    b=1
    if n<0:
            print("incorrect value")
    elif n==0:
            return 0
    elif n==1:
            return 1
    else:
            for i in range(2,n+1):
                c=a+b
                a=b
                b=c
            return c

n=int(input("enter value:"))

start_time=time.time()

print("non recursive:",non_recursive(n))
end_time=time.time()
print(f"time required by non recursive is {end_time-start_time}")

#Recursive---------
def recursive(n):
    if n<0:
        print("invalid input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recursive(n-1) + recursive(n-2)

start_time=time.time()
print("recursive",recursive(n))

end_time=time.time()
print(f"time required by recursive is {end_time-start_time}")
