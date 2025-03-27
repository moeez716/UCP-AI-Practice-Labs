#Exercise 1.1
a=250
print("a part type is ",type(a))
b=28%5
print("b part type is ",type(b))
c=2.5e2
print("c part type is ",type(c))
d=3e5
print("d part type is ",type(d))
e=3 * 10**5
print("e part type is ",type(e))
f=20 + 35 * 2  #follow BDMAS Rule to evalute expression
print("f part type is ",type(f))  
g=2 / 3 * 3
print("g part type is ",type(g))

h = 2 // 3 * 3  #It is different from 2 / 3 * 3 because it divde and round off in floor
print("h part type is ",type(h))
i=25 - 5 * 2 - 9
#Is this different from ((25 - 5) * 2) - 9 and/or 25 - ((5 * 2) - 9)? Why?
#Answere can be chnaged because it follow BDMAS Rule and bracket arrangement are different

print("i part type is ",type(i))


#Exercise 1.2
def sundaes(flavors,sauces):
    count =0
    for flavor in flavors:
        for sauce in sauces:
            print(flavor + " ice cream sundae with " + sauce + " sauce")
            count=count+1
    return count                

flavors = ["vanilla", "chocolate", "strawberry", "pistacchio"]
sauces = ["caramel", "butterscotch", "chocolate"]
print(sundaes(flavors,sauces))


#Exersize 1.3
def triangle():
 
 value=1
 row = 1
 while row <=10:
   column = 1
   while column <=row:
      if column != row:
        print(value, ' ', sep = '', end = '')
      else:
        print(value)
      value = value + 1
      column = column + 1
   row = row + 1

triangle()


#Exercise 1.4 
#part 1
#cube
def cube(n):
   print(n*n*n)

cube(5)  
#factorial
def factorial(n):
   fac=1
   if n==0:
      return 1
   else:
      for x in range(1,n+1):
         fac=fac*x
   return fac
print(factorial(0))      
#count pattern
def count_pattern(pattern, lst):
   n=len(lst)
   
   k=-1
   count=0
   x=0
   i=0
   j=0
   for s in range(0,len(lst)*len(pattern)-1):
      k=k+1
      if i==len(lst):
         break
      if pattern[k]==lst[i]:
         x=x+1
      if k==len(pattern)-1:
         k=-1
         j=j+1
      if x==len(pattern):
         x=0
         count=count+1
      if k==-1:
         i=j
      else:
         i=i+1         
   return count     
print(count_pattern(('a', 'b'), ('a','b', 'c', 'e', 'b', 'a', 'b', 'f')))

  # develop table
a=int(input("Enter number"))
n=int(input("Enter size"))
i=1
while i<=n:
    print(a, " * ", i, " = ",a*i)
    i=i+1

#Simple calculator
def simpleCalculator(a,b,opt):
   if opt=='+':
      return a+b
   elif opt=='-':
      return a-b
   elif opt=='*':
      return a*b
   elif opt=='/':
      return a/b
   
a=int(input("Enter First number \n"))
b=int(input("Enter Second number \n"))
c=input("Enter operator \n")         
print(simpleCalculator(a,b,c))

#sort the sentence in alphabetical order
str="i am from pakistan"
a=str.split(" ")
a.sort()
str=" ".join(a)
print(str)
#part 2
class integertoroman:
 def __init__(self,number):
    self.number=number
 def printroman(a):   
    
    num = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
     
    while a.number:
        div = a.number // num[i]
        a.number %= num[i]
 
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
number = 3849
print("Roman value is:", end = " ")
om=integertoroman(number)
om.printroman()
#part 3
print()
print("pair element")
class pairElement:
   def __init__(self,target,arr):
      self.target=target
      self.arr=arr
      self.n=len(arr)
   def pair(self):
      
      for i in range(0,self.n):
         a=self.arr[i]
         for j in range(i,self.n):
            if a+self.arr[j]==self.target:
               print(i+1,", ",j+1)
            
numbers= [10,20,10,40,50,60,70]
a=pairElement(70,numbers)
a.pair()

#part4
class threeElement:
   def __init__(self,arr):
      self.arr=arr
   def find(obj):
      
      m=[]
      n=len(obj.arr)
      for i in range(0,n):
         
         for j in range(i,n):
            for k in range(j,n):
               count=0
               l=[]
               if obj.arr[i]+obj.arr[j]+obj.arr[k]==0:
                  l.append(obj.arr[i])
                  l.append(obj.arr[j])
                  l.append(obj.arr[k])
                  count=count+1
               if count==1:
                  m.append(l)
      return m
arr=[-25, -10, -7, -3, 2, 4, 8, 10,20,5]
g=threeElement(arr)
print(g.find())      

 
#part 5
class reverse:
   def __init__(self,str):
      self.str=str
   def rev(a):
      l=a.str.split()
      l.reverse()
      s=" ".join(l)
      print(s)
r=reverse("hello .py")
r.rev()

#part6
#(a)
str=input(" Enter the string ")
#(b)
a=len(str)
#(C)
print(a)


#part 7
mat1=[
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
mat2=[
   [3,2,1],
   [6,5,7],
   [4,2,1]
]
mat3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(mat1)):
   for j in range(0,len(mat2)):
      mat3[i][j]=mat1[i][j]+mat2[i][j]

print(mat3)

#part 8
mat1=[
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
mat2=[
   [3,2,1],
   [6,5,7],
   [4,2,1]
]
mat3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(mat1)):
   for j in range(0,len(mat2)):
      mat3[i][j]=mat1[i][j]*mat2[i][j]

print(mat3)

#task9
def calculator(a,b,op="+",format="float"):
   
   if op=="+":
      c= a+b
   elif op=="-":
      c=a-b
   elif op=="*":
      c=a*b
   elif op=="/":
      if b==0:
         return "error! number2 should not be zero"
      else:
         c=a/b
   if format=="integer":
      return round(c)
   else:
      return c
print(calculator(10,0,"/","integer"))

#Part 10

class Number:
   multiplier=2
   def __init__(self,x,y):
      self.x=x
      self.y=y
   def add(obj):
      return obj.x+obj.y
   def multiply(obj,a):
      return obj.multiplier*a
   def subtract(b,c):
      return b-c
   def value(self):
      return self.x, self.y
   def setValue(obj,x,y):
      obj.x=x
      obj.y=y
   def delValue(obj,x,y):
      del obj.x
      del obj.y

s=Number(3,5)
print(s.add())
print(s.multiply(5))
print(Number.subtract(3,1))
print(s.value())   