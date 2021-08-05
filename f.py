#create function/ define func
# i, j are varables/ parameters

def iiec(*i):
	m = 0
	for j in i:
		m = j + m
	return m	


# to run / calling a func

u = iiec(2,5,8,4,1)
print(u)

d = iiec(3,2)
print(d)