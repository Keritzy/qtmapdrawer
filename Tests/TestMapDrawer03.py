from MapDrawer import *
import sys

def main( args ):
	a=QApplication(sys.argv)					    
	map_drawer=MapDrawer()

	names=[]
	caller={}
	called={}
	comments={}

	for i in range(0,10,1):
		names.append(str(i))
	import random
	random.seed()
	for i in range(0,len(names),1):
		name=names[i]
		if not caller.has_key(name):
			caller[name]=[]
		for j in range(0,3,1):
			k=random.randint(0,len(names)-1)
			caller[name].append(names[k])

	map_drawer.SetMapData(names,caller,called,comments,layout='graphviz')
	a.setMainWidget(map_drawer)
	map_drawer.show()  
	a.exec_loop()

main(sys.argv)
