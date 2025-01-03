class Person():

    def __init__(self,first_name,last_name):
      self.first_name = first_name
      self.last_name = last_name

    def hello(self):
        print("hello!")

    def report(self):
       print(f'I am {self.first_name} {self.last_name}')


class agent(Person):
   
   def reveal (self,passcode):
      if passcode == 123:
         print("I am a agent")

      else:
         self.report()

x= agent("john", "smith")
x.reveal(123)
