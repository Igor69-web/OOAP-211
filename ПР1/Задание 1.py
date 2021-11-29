class First:
	color = "red"
	def out(self):
		print(self.color + "!")
obj1 = First()
obj2= First()
print(obj1.color)
print(obj2.color)
obj1.out()
obj2.out()

class Second:
	color = "red"
	form = "circle"
	def changecolor(self,newcolor):
		self.color = newcolor
	def changeform(self,newform):
		self.form = newform
obj1= Second()
obj2= Second()
print(obj1.color,obj2.form)
print(obj1.color,obj2.form)
obj1.changecolor("green")
obj2.changecolor("blue")
obj2.changeform("oval")
print(obj1.color,obj1.form)
print(obj1.color,obj2.form)
obj3 = Second()
obj3.changecolor("triangle")
obj3.changecolor("yellow")
print(obj3.color,obj3.form)