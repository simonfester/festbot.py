#!/bin/bash
# setup festbot.py git script

sudo apt-get install -y git
mkdir festbot.py
cd festbot.py
git init
git config --global user.email syhester@gmail.com
git config --global user.name simonfester
echo ""
cat ~/.ssh/id_rsa.pub
echo""
read -e -p "Enter [Y] once you have added the key to github [Y/n] " 
git remote add origin git@github.com:simonfester/festbot.git
git pull origin master

