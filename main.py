from os import system
from platform import system as get_os_name

# {"execname (optional common name)":["dependency","linux command","mac command(optional)"]}
install_commands = {
    'vimv': ['', "mkdir ~/bin ; curl https://raw.githubusercontent.com/thameera/vimv/master/vimv -o ~/bin/vimv && chmod +755 ~/bin/vimv"],

    'nvm': [
        "",
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash && . ~/.bashrc"
    ],

    'npm': ['nvm', "nvm install --lts"],

    'yarn': ['npm', "npm i -g yarn"],

    'rustup': ['', "curl https://sh.rustup.rs -sSf | sh -s -- -y && . ~/.cargo/env"],

    'lsd':['rustup',"cargo install lsd"],

    'alacritty':['rustup',"cargo install alacritty"],

    "conda or miniconda": [
        "", "curl -sL \
      \"https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh\" >\
      \"Miniconda3.sh\" && bash Miniconda3.sh -b -p $HOME/miniconda && . ~/.bashrc && conda init",

      "curl -sL \
      \"https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh\" >\
      \"Miniconda3.sh\" && bash Miniconda3.sh -b -p $HOME/miniconda && . ~/.bashrc && conda init"
    ]
}


def install_packages(packages):
    if packages is None:
        print("You dont have selected any package exiting")
        return

    commands = []

    for pkg in packages:
        p = pkg

        cmd_no = 1 if get_os_name() == "Linux" else 2  # Configuring according to OS
        # Checking if unique command is there or not
        cmd_no = 1 if len(install_commands[p]) < 3 else 2

        commands.append(install_commands[p][cmd_no])

        while install_commands[p][0] != "":
            commands.append(install_commands[p][cmd_no])
            p = install_commands[p][0]
        commands.append(install_commands[p][cmd_no])

    # Adding common directories to path
    commands.extend([
        "echo \"export PATH=\"\$HOME/bin:\$PATH\"\" >> ~/.bashrc",
        "echo \"export PATH=\"\$HOME/.local/bin:\$PATH\"\" >> ~/.bashrc"
        ])
    commands = list(dict.fromkeys(commands))  # Removing Duplicates
    system(" && ".join(commands[::-1]))  # Running commands


def main():
    from iterfzf import iterfzf as fzf
    install_pkg = fzf(install_commands.keys(), multi=True)
    install_packages(install_pkg)
    return install_pkg # For partial testing


if __name__ == "__main__":
    main()
