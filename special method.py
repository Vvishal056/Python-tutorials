class Book():
  
  def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages

  def __str__(self):
    return f"{self.title} written by {self.author}" 

  def __len__(self):
    return  self.pages
  
  

mybook = Book("pyhton!!","vishal",230)
print(mybook)
print(len(mybook))
