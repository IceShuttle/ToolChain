from os import system

install_commands = {
    'nvm': [
        "",
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash && . ~/.bashrc"
    ],
    'npm': ['nvm', "nvm install --lts"],
    'yarn': ['npm', "npm i -g yarn"],
    'rustup':
    ['', "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"],
    "conda or miniconda": [
        "", "curl -sL \
      \"https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh\" >\
      \"Miniconda3.sh\" && bash Miniconda3.sh -b"
    ]
}


def install_packages(packages):
    if packages is None:
        print("You dont have selected any package exiting")
        return

    commands = []
    for pkg in packages:
        p = pkg
        commands.append(install_commands[p][1])

        while install_commands[p][0] != "":
            commands.append(install_commands[p][1])
            p = install_commands[p][0]
        commands.append(install_commands[p][1])

    commands = list(dict.fromkeys(commands))  # Removing Duplicates
    system(" && ".join(commands[::-1])) # Running commands


def main():
    from iterfzf import iterfzf as fzf
    install_packages(fzf(install_commands.keys(), multi=True))


if __name__ == "__main__":
    main()
