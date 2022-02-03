from ntpath import join
from os import system as cmd
from pathlib import Path
from platform import system as get_os_name

OS=get_os_name()

# {"execname (optional common name)":["dependency","linux command","mac command(optional)"]}
# Currently packages that depends on other packages must be below them
install_commands = {
    "vimv": ["", "curl https://raw.githubusercontent.com/thameera/vimv/master/vimv --create-dirs -o ~/bin/vimv && chmod +755 ~/bin/vimv"],

    "nvm": [
        "",
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash && . ~/.bashrc"
    ],

    "npm": ["nvm", "nvm install --lts"],

    "yarn": ["npm", "npm i -g yarn"],

    "rustup": ["", "curl https://sh.rustup.rs -sSf | sh -s -- -y && . ~/.cargo/env && . ~/.bashrc"],

    "lsd": ["rustup", "cargo install lsd"],

    "conda": [
        "", "curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /tmp/Miniconda3.sh && bash /tmp/Miniconda3.sh -b -p ~/miniconda3",

      "curl -sL \
      \"https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh\" >\
      \"/tmp/Miniconda3.sh\" && bash /tmp/Miniconda3.sh -b -p ~/miniconda3"
    ]
}


def install_packages(packages):
    if packages is None:
        print("You dont have selected any package exiting")
        return

    # Adding common directories to path
    add_common_paths()

    # Dependency Resolver
    pkgs = packages.copy()
    for p in pkgs:
        if install_commands[p][0]!="":
            pkgs.append(install_commands[p][0])
    
    # Ordering packages according to install_commands
    pkgs = list(filter(lambda p: p in pkgs,install_commands.keys()))
    commands = [install_commands[p][get_cmd_no(p)] for p in pkgs]
    cmd(";\n".join(commands))


def get_cmd_no(p):
    c = 1
    if len(install_commands[p])<3:
        c=1
    elif OS=="Linux":
        c=1
    elif OS=="Darwin":
        c=2
    return c
    
def add_common_paths():
    home = str(Path.home())
    with open(f"{home}/.bashrc",'a') as bash_init:
        bash_init.writelines([
            "export PATH=\"~/bin:$PATH\"\n",
            "export PATH=\"~/.local/bin:$PATH\"\n",
            "export PATH=\"~/miniconda3/bin:$PATH\"\n",
        ])

def main():
    from iterfzf import iterfzf as fzf
    packages = fzf(install_commands.keys(), multi=True)
    install_packages(packages)
    return  packages# For partial testing


if __name__ == "__main__":
    main()
