import imp
from os import system as cmd
from main import main as get_installed_pkg
from full_test import create_test_script

if __name__=="__main__":
    packages = get_installed_pkg()
    packages = [i.split()[0] for i in packages]
    create_test_script(packages)
    cmd("bash test.sh")
    input("press enter to stop container")