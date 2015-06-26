import subprocess
import platform


def pingpong(host):
    """

    """
    if host == 'leo':
        host = '192.168.248.103'
    elif host == 'r2d2':
        host = '192.168.248.152'

    statistic = []

    if platform.system() == 'Linux':
        ping = subprocess.Popen(
            ["ping", "-A", "-c", "10", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, error = ping.communicate()
        flag = out.find('min/avg/max/mdev')
        loss = out[out.find('packet loss') - 3: out.find('packet loss') - 1]
        rttMin = out[flag + 19: flag + 25]
        rttMax = out[flag + 33: flag + 39]
        rttAvg = out[flag + 26: flag + 32]
        jitter = str(((float(rttAvg) - float(rttMin)) + (float(rttMax) - float(rttAvg))) / 2)
        return [64, loss, rttMin, rttAvg, rttMax, jitter]

    else:
        for foo in [64, 782, 1500]:
            ping = subprocess.Popen(
                ["ping", "-l", str(foo), "-n", "10", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            out, error = ping.communicate()
            statistic.append(foo)
            statistic.append(out[out.find('(', out.find('Lost')) + 1: out.find('loss') - 1])
            if 'Approximate round trip times in milli-seconds' in out:
                rttMin = out[out.find('Minimum') + 10: out.find('ms', out.find('Minimum'))]
                rttMax = out[out.find('Maximum') + 10: out.find('ms', out.find('Maximum'))]
                rttAvg = out[out.find('Average') + 10: out.find('ms', out.find('Average'))]
                jitter = str(((float(rttAvg) - float(rttMin)) + (float(rttMax) - float(rttAvg))) / 2)
                statistic.append(rttMin)
                statistic.append(rttMax)
                statistic.append(rttAvg)
                statistic.append(jitter)

            else:
                for i in range(0, 5):
                    statistic.append('0')
    return statistic
