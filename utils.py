import subprocess
import platform


def pingpong(host):
	if host == 'leo':
		host = '192.168.248.103'
	elif host == 'r2d2':
		host = '192.168.248.152'
	if platform.system() == 'Linux':
		ping = subprocess.Popen(
			["ping", "-A", "-c", "10", host],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		)
		out, error = ping.communicate()
		flag = out.find('min/avg/max/mdev')
		loss = out[out.find('packet loss') - 3 : out.find('packet loss') - 1]
		rttMin = out[flag + 19 : flag + 25]
		rttMax = out[flag + 33 : flag + 39]
		rttAvg = out[flag + 26 : flag + 32]
		jitter = str(((float(rttAvg) - float(rttMin)) + (float(rttMax) - float(rttAvg))) / 2)
		return [loss, rttMin, rttAvg, rttMax, jitter]

	else:
		ping = subprocess.Popen(
			["ping", "-n", "10", host],
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE
		)
		out, error = ping.communicate()
	return out[out.find('Ping statistics'):]

