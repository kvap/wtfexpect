#!/usr/bin/python3

import wtfexpect

we = wtfexpect.WtfExpect()
try:
	we.spawn('alpha', ['./slowls.sh', '-l', '/'])
	we.spawn('bravo', ['./slowls.sh', '-l', '/'])

	while we.alive():
		timeout = 0.5
		name, line = we.readline(timeout)
		if name is None:
			print("no lines for %0.2f sec" % timeout)
		elif line is None:
			print("%s finished" % name)
		else:
			print("[%s] %s" % (name, line))
finally:
	we.finish()
