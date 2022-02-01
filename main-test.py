from main import install_commands, install_packages

packages = list(install_commands.keys())

exec_names = [i.split()[0] for i in packages]  # Getting executable names

# Installing all packages

install_packages(packages)

# Testing commands
print()  # Creating blank line
test_commands = [". ~/.nvm/nvm.sh",
                 ". ~/.bashrc"]  # Loading environment

for e in exec_names:
    test_commands.append(
        f"if [ $(command -v {e} | wc -l) -lt 1 ] ; then echo \"Installation of {e} failed ❌\" 1>&2 && exit 1 ; else echo passed ✅ ; fi"
    )

with open("test.sh", 'w') as test_script:
    test_script.writelines(" && ".join(test_commands))
