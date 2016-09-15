import subprocess as s

def whoami():
	return s.Popen(["whoami"], stdout=s.PIPE).communicate()[0]
