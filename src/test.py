#!/usr/bin/env python
"""
Unit test/basic Daemon-Python implementation
"""
import sys
import time
from daemon import Daemon

class TestDaemon(Daemon):
    def run(self): #Define what tasks/processes to daemonize
        while True:
            time.sleep(1)

if __name__ == "__main__":
    daemon = TestDaemon('/tmp/daemon-py-test.pid') #Define a pidfile location (typically located in /tmp or /var/run)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'status' == sys.argv[1]:
            daemon.status()
        else:
            sys.stdout.write("Unknown command\n")
            sys.exit(2)
        sys.exit(0)
    else:
        sys.stdout.write("Usage: %s start|stop|restart|status\n" % sys.argv[0])
        sys.exit(2)