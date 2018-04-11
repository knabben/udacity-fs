#!/bin/sh
# Install bootstrap system to run ansible provisioner
export LC_ALL=C

# Update Ubuntu package
sudo apt-get update

# Install Python dependencies
sudo apt-get install -y python python-pip libssl-dev libcurl4-openssl-dev \
python-virtualenv

# PIP install Ansible
sudo pip install --upgrade pip

# Install psycopg2
sudo pip install psycopg2
