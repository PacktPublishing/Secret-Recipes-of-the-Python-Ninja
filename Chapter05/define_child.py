def child():
   print("Child {} calling".format(os.getpid()))
   os._exit(0)
