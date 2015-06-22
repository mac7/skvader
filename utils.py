import subprocess
import platform

def pingpong(host):

	if host == 'leo':
		host = '192.168.248.103'
	elif host == 'r2d2':
		host = '192.168.248.152'
	if platform.system() == 'Linux':
		ping = subprocess.Popen(
	    				["ping", "-A","-c", "10", host],
	    				stdout = subprocess.PIPE,
	    				stderr = subprocess.PIPE
					)
		out, error = ping.communicate()
	else:
		ping = subprocess.Popen(
	    				["ping", "-n", "10", host],
	    				stdout = subprocess.PIPE,
	    				stderr = subprocess.PIPE
					)
		out, error = ping.communicate()
	return out[out.find('---'):]	
