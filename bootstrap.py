
#!/usr/bin/env python
import subprocess

# sudo apt-get update

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print colors.HEADER + """

  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$$$ /$$$$$$$
 /$$__  $$| $$  | $$ /$$__  $$| $$__  $$| $$__  $$| $$_____/| $$__  $$
| $$  \__/| $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$| $$      | $$  \ $$
| $$      | $$$$$$$$| $$  | $$| $$$$$$$/| $$$$$$$/| $$$$$   | $$$$$$$/
| $$      | $$__  $$| $$  | $$| $$____/ | $$____/ | $$__/   | $$__  $$
| $$    $$| $$  | $$| $$  | $$| $$      | $$      | $$      | $$  \ $$
|  $$$$$$/| $$  | $$|  $$$$$$/| $$      | $$      | $$$$$$$$| $$  | $$
 \______/ |__/  |__/ \______/ |__/      |__/      |________/|__/  |__/


""" + colors.ENDC

def sub(label, execute):
    if label != "":
        printHeader(label)
    subprocess.call(execute, shell=True)

def pip(execute):
    sub("Installing %s" % execute, "sudo -H pip install %s" % execute)


def printHeader(text):
    print colors.OKBLUE + """
--------------------------------------------------------------------------------
%s
--------------------------------------------------------------------------------
""" % text + colors.ENDC



sub("Updating apt-get", "sudo apt-get update")
sub("Installing git", "sudo apt-get install git-all")
sub("Installing pip", "wget https://bootstrap.pypa.io/get-pip.py && (sudo -H python get-pip.py; rm get-pip.py)")
sub("Installing postgresql", "sudo apt-get install postgresql postgresql-contrib")
sub("Installing nano", "sudo apt-get install nano")
pip("virtualenv")
pip("virtualenvwrapper")
pip("Flask")
pip("SQLAlchemy")
pip("Jinja2")
pip("flask")
pip("flask-login")
pip("flask-openid")
pip("flask-mail")
pip("flask-sqlalchemy")
pip("sqlalchemy-migrate")
pip("flask-whooshalchemy")
pip("flask-wtf")
pip("flask-babel")
pip("guess_language")
pip("flipflop")
pip("coverage")
