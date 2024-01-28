class Demo1:
  def method1(self):
      print("Class A method")

class Demo2(Demo1):
  def method1(self):
      print("Class B method")

a1=Demo1()
a1.method1()

b1=Demo2()
b1.method1()
