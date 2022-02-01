from os import system
from main import install_commands, install_packages

packages = install_commands.keys()

exec_names = [i.split()[0] for i in packages] # Getting executable names 

# Installing all packages

install_packages([packages])

# Testing commands
print() # Creating blank line
test_commands = [". ~/.bashrc"]

for e in exec_names:
    test_commands.append(f"command -v {e}")

system(" && ".join(test_commands))
