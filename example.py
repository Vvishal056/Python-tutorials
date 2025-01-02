class circle():
  pi = 3.14
  def __init__(self,radius=1):
    self.radius = radius

  def multiply_radius(self,number):
    self.radius = self.radius*number
    print(f'Radius has been change to{self.radius}')



mycircle = circle(radius=4)
mycircle.multiply_radius(20)
print(mycircle.radius)