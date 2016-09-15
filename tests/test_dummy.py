import smoothwall.showwhoami as s

def test():
	assert s.whoami() == 'root\n'