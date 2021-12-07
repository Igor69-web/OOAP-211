class First:
	color = "red"
	def out(self):
		print(self.color + "!")
obj1= First()
obj2 = First()
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
obj2 = Second()
obj3 = Second()
print(obj1.color,obj1.form,obj3.form)
print(obj2.color,obj2.form)
obj1.changecolor("green")
obj2.changecolor("blue")
obj2.changeform("oval")
obj3.changeform("treangel")
print(obj1.color,obj1.form,obj3.form)
print(obj2.color,obj2.form)


class Building:
	def __init__(self,w,c,n=0):
		self.what = w
		self.color = c
		self.numbers = n
		self.mwhere(n)
	def mwhere(self,n):
		if n<=0:
			self.where = "отсутсвуют"
		elif 0<n<100:
			self.where = "малый склад"
		else:
			self.where = "основной склад"
	def plus(self,p):
		self.number = self.numbers + p
		self.mwhere(self.numbers)
	def minus(self,m):
		self.numbers = self.numbers - m
		self.mwhere(self.numbers)
m1 = Building("доски","белые",50)
m2 = Building("доски","коричиневые",300)
m3 = Building("кирпичи","белые")
print(m1.what,m1.color,m1.where)
print(m2.what,m2.color,m2.where)
print(m3.what,m3.color,m3.where)
m1.plus(500)
print(m1.numbers,m1.where)


class Person:
	def __init__(self,h,br,n,i):
		self.name = n
		self.hp = h
		self.brony = br
		self.intlekt = i
	def br(self):
		return self.brony
	def intelkt(self):
		return self.intlekt
p1 = Person("Stalker,","100 жизней,","у него 300 брони,","имеет 200 интелекта")
print(p1.name,p1.hp,p1.brony,p1.intlekt)



class Things:
	def __init__(self,n,t):
		self.namething = n
		self.total = t
th1 = Things("Table",5)
th2 = Things("computer",7)
print(th1.namething,th1.total)
print(th2.namething,th2.total)
th1.color = "green"
th2.color = "blue"
print(th1.color)
print(th2.color)


class Table:
	def __init__(self,l,w,h):
		self.long = 1
		self.widht = w
		self.height = h
	def outing(self):
		print(self.long,self.widht,self.height)
class Kitchen(Table):
	def howplace(self,n):
		if n < 2:
			print("it is not kitchen table")
		else:
			self.places = n
	def outplace(self):
		print(self.places)
t_room1 = Kitchen(2,1,0.5)
t_room1.outing()
t_room1.howplace(5)
t_room1.outplace()
t_2 = Table(1,3,0.7)
t_2.outing()
class Worker(Table):
	def sborka(self):
		print("рабочий собирает стол")
	def oplata(self):
		print("работа оплачена и стол собран")
w = Worker(1,2,3)
w.sborka()
w.oplata()


class Figure:
	def __init__(self,w="white"):
		self.color = w
	def changecolor(self,ch):
		self.chcolor = ch
class Oval(Figure):
	def __init__(self,r,x,y):
		self.radius = r
		self.ox = x
		self.oy = y
		super().__init__()
	def out(self):
		print (self.radius,self.ox,self.oy)
class Square(Figure):
	def __init__(self,w,h):
		self.widht = w
		self.height = h
		super().__init__()
	def howsides(self,n):
		self.sides = n
		if not self.sides == 4:
			print ("Это не квадрат")
		else:
			print ("Это квадрат")
	def outsides(self):
		print (self.sides)
x = Figure("red")
print(x.color)

o = Oval(10,2,5)
o.out()
o.changecolor("синий")
print(o.chcolor, o.radius)

s = Square(3,3)
s.howsides(7)
s.outsides()
s.changecolor("желтый")
print(s.chcolor, s.widht, s.height)