# Installing Python on WSL
Congratulations for using my favourite work set-up! Getting set up on WSL is nice and easy.  

1. Update the known packages and versions for APT:
    * `sudo apt update`
1. Install "software-properties-common" which gives you the ability to add extra repositories to APT:
    * `sudo apt install software-properties-common`
1. Add the "deadsnakes" repo to APT:
    * `sudo add-apt-repository ppa:deadsnakes/ppa`
1. Update known packages again, now you have a whole new repo:
    * `sudo apt update`
1. Install your chosen Python version:
    * `sudo apt install python3.12`