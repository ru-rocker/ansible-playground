# Ansible Playground
This workspace is intended to play around using ansible.

## How to Install Ansible
For my mac, I use python and pip installation.

    sudo pip install ansible

Or if you are Ubuntu user

    sudo apt-get install ansible -y

Or Redhat/CentOS

    sudo yum install ansible

## Configure ssh authorization
Use locally available keys to authorize logins on a remote machine

    ssh-copy-id -i ~/ssh/id_rsa.pub user@hostname

## Sub-directories
#### ansible-ping
In this sub-module, the playbook is intended to ping remote server.
