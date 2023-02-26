import os,sys,subprocess
pydev_host = os.environ.get('PYDEV_HOST', None)
pydev_port = os.environ.get('PYDEV_PORT', None)

if pydev_port is not None:
    # this is a subprocess running under a debugger
    import pydevd
    # connect back to the PyCharm debugger and resume as normal
    # PyCharm will set pending breakpoints upon connection before resuming
    pydevd.settrace(pydev_host, port=int(pydev_port), suspend=False)


def run_tb():
    try:
        import pydevd
        pydevd_setup = pydevd.SetupHolder.setup
        if pydevd_setup is not None:
            # get a new debugger port for the subprocess to connect to
            host, port = pydevd.dispatch()
            os.environ['PYDEV_HOST'] = host
            os.environ['PYDEV_PORT'] = str(port)
    except ImportError:
        pass # not running under debugger

    try:
        r = subprocess.call(["make"])
    except:
        r = -1
    return r