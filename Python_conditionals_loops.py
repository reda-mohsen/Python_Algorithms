# If Statements
print('Checking if conditon')
# x = int(input('Enter an integer x: '))
# y = int(input('Enter an integer y: '))
# z = int(input('Enter an integer z: '))
x = 3
y = 5
z = 4

# Check if x is the least
if x<y and x<z:
    print('x is the least')
# then x>y or x>z
elif y<z:
    print('y is the least')
# then y>z
else:
    print('z is the least')
print('Done with conditional')

# While Statements
print('Checking while loop')
n = 0
while n < 6:
    print (n) # n = 5
    n = n+1
print(n)# n = 6

# For Statements
print('Checking for loop')
mysum = 0
for i in range(3,13,4): # 3->start, (13-1)->end, 4->step, i is from 3 to 12 step 3(3,6,9,12)
    mysum += i # mysum = 3, mysum = 6, mysum = 4+11=15
    if mysum == 15: # false, false
        print (mysum) # print 15
        break
    else:
        mysum = i-3 # mysum = 0, mysum = 4
    print(i) # print 3, print 7
    print(mysum) # print 0, print 4
print (mysum+5) # print 20

# For with Strings
print('Check for with strings')
s = "abcdefg"
for index in range(len(s)):
    print(index)
for char in s:
    print(char)
    
