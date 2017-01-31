import json
import sys
import subprocess
import utils.errors


__version__ = 0.1
__author__ = 'weldpua2008@gmail.com'


def run_cmd(cmd):
    """run command cmd and return (stdout, stderr)"""
    handler = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = handler.communicate()
    if sys.version_info > (3,0,0):
        if isinstance(stdout, bytes):
            _stdout = str(stdout, 'UTF-8')
            stdout = _stdout
    return stdout, stderr


def run_cmd_with_ret_code(cmd):
    """run command cmd and return (stdout, stderr)"""
    handler = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = handler.communicate()
    returncode = handler.returncode
    if sys.version_info > (3,0,0):
        if isinstance(stdout, bytes):
            _stdout = str(stdout, 'UTF-8')
            stdout = _stdout
    return stdout, stderr, returncode


def run_and_get_json(cmd):
    sys_data = None
    stdout = None
    try:
        # pylint: disable=unused-variable
        stdout, stderr = run_cmd(cmd)
    # pylint: disable=broad-except,invalid-name
    except Exception as error:
        utils.errors.get_runtime_error(
            "Can't run %s because %s" % (cmd, error))
    try:
        sys_data = json.loads(stdout)
    # pylint: disable=broad-except
    except Exception as error:
        utils.errors.get_value_error(
            "Can't parse output as json of %s because %s" %
            (cmd, error))
    return sys_data
