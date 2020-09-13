#!/bin/bash
#
# Script to Install

### GENERAL LINUX ###

apt-get update  # updates the package index cache
apt-get upgrade -y  # updates packages
apt-get install -y bzip2 gcc git htop screen vim wget
apt-get upgrade -y bash  # upgrades bash if necessary
apt-get clean  # cleans up the package index cache

### INSTALL MINICONDA ###
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O Miniconda.sh
bash Miniconda.sh -b  # installs it
rm -rf Miniconda.sh  # removes the installer file
export PATH="/root/miniconda3/bin:$PATH"  # prepends the new path

### Install Python Libraries  ###
conda install -y pandas  # installs pandas incl. NumPy
conda install -y numpy
conda install -y pytables

### Install Binance
pip install python-binance
