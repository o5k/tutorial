__author__ = 'oussama'

import paramiko


def get_environment():
    from env import hostname, username, password
    return hostname, username, password


def remote_run(cmd):
    """
        Runs a command *cmd* remotely, returns standard and error output in case of success,
        and returns an error if the call fails.
        :return: output, error, success/failure(True/False)
    """
    hostname, username, password = get_environment()
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname, username=username, password=password)
        print hostname, username, password
        stdin, stdout, stderr = ssh.exec_command(cmd)
        _out, _err, success = stdout.readlines(), stderr.readlines(), True
        return _out, _err, success
    except Exception as e:
        print e
        return None, e, False