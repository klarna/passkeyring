import keyring.backend

import os
from subprocess import Popen, PIPE

class PassKeyring(keyring.backend.KeyringBackend):
    """A keyring interfacing with Pass
    """
    priority = 1

    def set_password(self, servicename, username, password):
        p1 = Popen(["echo", password], stdout=PIPE)
        p2 = Popen(["pass", "insert", "-e", "-f", servicename+"/"+username], stdin=p1.stdout, stdout=PIPE)
        p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
        (stdout, stderr) = p2.communicate()
        exit_code = p2.wait()
        return exit_code

    def get_password(self, servicename, username):
        process = Popen(["pass", servicename+"/"+username], stdout=PIPE)
        (stdout, stderr) = process.communicate()
        exit_code = process.wait()
        if exit_code == 0:
            return stdout.rstrip()
        else:
            return None

    def delete_password(self, servicename, username):
        process = Popen(["pass", "rm", "-f", servicename+"/"+username], stdout=PIPE)
        (stdout, stderr) = process.communicate()
        exit_code = process.wait()
        return exit_code

