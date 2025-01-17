[<- go back](../01_set_up.md)
# Installing Python on WSL
Congratulations for using my favourite work set-up! Getting set up on WSL is nice and easy.  


## Homebrew - Current releases

Go [here](https://brew.sh/) and follow the instructions **_carefully!_**  
Now, when you install Homebrew it will give you additional instructions on how to finish setup right there in the command line. It is imperative that you read all the output and follow the additional instructions or you risk not setting up homebrew right.  
Once you got homebrew installed, you can just give commands like:
```
brew install python@3.12
```

## deadsnakes - Unsupported legacy releases

| **WARNING** |
|-------------|
| I totally got burned by deadsnakes recently, they messed up the installer for Python13 so badly that it prevented my package manager from being able to update anything at all and I had to get rid of the deadsnakes repo entirely. _Now_, if you're working on some legacy code that still runs on some super old Python version, then deadsnakes might be your only option and this is the only time I would recommend you using it.

1. Update the known packages and versions for APT:
    * `sudo apt update`
1. Install "software-properties-common" which gives you the ability to add extra repositories to APT:
    * `sudo apt install software-properties-common`
1. Add the "deadsnakes" repo to APT:
    * `sudo add-apt-repository ppa:deadsnakes/ppa`
1. Update known packages again, seeing as you have a whole new repo to update:
    * `sudo apt update`
1. Install your chosen Python version:
    * `sudo apt install python3.12`