import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
  with open(filename) as fobj:
      startup_file = fobj.read()
   exec(startup_file)
