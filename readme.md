[ ![Github-CLI](https://avatars.githubusercontent.com/u/9919?s=200&v=4) ](https://cli.github.com/)

# Remove [Github-CLI](https://cli.github.com/) from [Ubuntu](https://ubuntu.com/) based distros

## Remove all dependencies and remaining files from gh

<br />
<br />

To `run` use:

```bash
chmod +x remove-github-cli.py
sudo ./remove-github-cli.py

or 

sudo python3 remove-github-cli.py
```

`SUDO` is needed, without superuser access we can't remove some files and configs

<br />
<br />


## Explanations

* This script will not remove plugins and files from vim, oh-my-zsh, compose, and other files created by user, unless if these files are in any target directories.

* Be Careful, use this script if you know what are you doing, maybe it can break other stuffs that you might want to use


<br />
<br />


### Made with 🥰 by [Dpbm](https://github.com/Dpbm)
