class Addition:
  no1=10
  no2=20
  def arithmetic(self):
      print("Result = "+str(self.no1+self.no2))

class Substraction(Addition):
  def arithmetic(self):
      print("Result = "+str(self.no1-self.no2))

a1=Addition()
a1.arithmetic()

b1=Substraction()
b1.arithmetic()
