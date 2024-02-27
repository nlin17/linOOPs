class A:
    def method(self):
        print("In A")

class B(A):
    def method(self):
        print("In B")

class C(A):
    def method(self):
        print("In C")

class D(B, C):
    pass

d = D()
d.method()