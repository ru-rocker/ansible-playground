# ansible-ping
Just try to ping target host

### Pre-requisite
Ansible already installed on your machine.

### Step-by-step
###### You can directly clone from this repository

    git clone https://TODO

###### Or you dare to create manually:
Create directory for our playbook

    cd ~
    mkdir ansible-ping && cd ansible-ping

Create two files, for host and playbook      

    touch hosts
    touch playbook.yml

Create roles folder

    mkdir roles && cd roles

Then bootstrap roles with ``ansible-galaxy``

    ansible-galaxy init ping

Then remove unneeded folder under ``~/ansible-ping/roles/ping``.

    cd ~/ansible-ping/roles/ping
    rm -rf files/ meta/ tests/ vars/ handlers/ templates/ defaults/ README.md

Setup hosts files

    vim ~/ansible-ping/hosts

Add server list

    [localhost]
    localhost ansible_connection=local #add variable ansible_connection=local in order not to try to use SSH to contact the hosts

    [ubuntu-remote]
    your_ubuntu_hostname_or_ip1
    your_ubuntu_hostname_or_ip2
    your_ubuntu_hostname_or_ip2

Setup playbook

    vim ~/ansible-ping/playbook.yml

Add lines:

    - hosts: localhost
      roles:
        - ping

    - hosts: ubuntu-remote
      roles:
        - ping

Setup task

    vim ~/ansible-ping/roles/ping/tasks/main.yml

Add lines:

    ---
    # tasks file for ping
    - name: ping servers
    ping:

### Run your playbook

    cd ~/ansible-ping
    ansible-playbook playbook.yml -i hosts
