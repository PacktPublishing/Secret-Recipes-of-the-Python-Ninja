def parent():
   for i in range(10):
   	newchild = os.fork()
   	if newchild == 0:
   		child()
   	else:
   		print("Parent {parent} calling. Creating child {child}".format(parent=os.getpid(), child=newchild))
   	i += 1
