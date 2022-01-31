from iterfzf import iterfzf as fzf

Sep = " &\n"
pkg_list = {
    'nvm': [
        "",
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash"
    ],
    'npm': ['nvm', "nvm install --lts"],
    'yarn': ['npm', "npm i -g yarn"],
    'rustup':
    ['', "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"],
    'miniconda': [
        "", "curl -sL \
      \"https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh\" >\
      \"Miniconda3.sh\" && bash Miniconda3.sh -b"
    ]
}


def install_packages(packages):
    commands = []
    for pkg in packages:
        p = pkg
        commands.append(pkg_list[p][1])

        while pkg_list[p][0] != "":
            commands.append(pkg_list[p][1])
            p = pkg_list[p][0]
        commands.append(pkg_list[p][1])

    commands = list(dict.fromkeys(commands))  # Removing Duplicates
    print(" && ".join(commands[::-1]))


print("Select the packages you want to install")
install_packages(fzf(pkg_list.keys(), multi=True))
