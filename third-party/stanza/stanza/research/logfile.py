import sys

class tee(object):
    '''
    A file-like object that duplicates output to two other file-like
    objects.

    Thanks to Akkana Peck for the implementation:

    http://shallowsky.com/blog/programming/python-tee.html
    '''
    def __init__(self, _fd1, _fd2):
        self.fd1 = _fd1
        self.fd2 = _fd2

    def __del__(self):
        if self.fd1 != sys.stdout and self.fd1 != sys.stderr:
            self.fd1.close()
        if self.fd2 != sys.stdout and self.fd2 != sys.stderr:
            self.fd2.close()

    def write(self, text):
        self.fd1.write(text)
        self.fd2.write(text)

    def flush(self):
        self.fd1.flush()
        self.fd2.flush()


def log_stdout_to(logfilename):
    stdoutsav = sys.stdout
    outputlog = open(logfilename, "w")
    sys.stdout = tee(stdoutsav, outputlog)


def log_stderr_to(logfilename):
    stderrsav = sys.stderr
    outputlog = open(logfilename, "w")
    sys.stderr = tee(stderrsav, outputlog)
