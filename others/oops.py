
#operator overloading
class Student:

    def __init__(self , m1, m2):
        self.m1 = m1
        self.m2 = m2

    #alternative for method/function overloading in python
    def sum (self, a=None, b=None, c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s =  a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s=a
        return s

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        s1 = self.m1 + self.m2
        s2 = other.m1 + other.m2
        if s1>s2:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.m1} {self.m2}'

         
s1 = Student(50,69)
s2 = Student(56, 64)

s3 = s1+s2      #student.__add__(s1,s2)
print (s3.m1 , s3.m2)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")

print(s1)  # == print(s1.__str__()) , will print address if not overloaded
print(s2)  # == print(s2.__str__()) , after overloading it prints value

print(f'SUM : {s1.sum(2, 4)}')