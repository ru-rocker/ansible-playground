# ansible-vault
Encrypting sensitive playbook files using ansible vault.
*Note: I just test on my local machine. But for remote machine, there will be no different*

### Pre-requisite
Ansible already installed on your machine.

### Step-by-step
#### You can directly clone from this repository and select ansible-vault directory

    git clone https://github.com/ru-rocker/ansible-playground

#### Or you dare to create manually:
###### Create directory for our playbook

    cd ~
    mkdir ansible-vault && cd ansible-vault

###### Create two files, for host and playbook      

    touch hosts
    touch playbook.yml

###### Create roles folder

    mkdir roles && cd roles

Then bootstrap roles with ``ansible-galaxy``

    ansible-galaxy init vault

Then remove unneeded folder under ``~/ansible-vault/roles/vault``.

    cd ~/ansible-vault/roles/vault
    rm -rf meta/ tests/ vars/ handlers/ templates/ defaults/ README.md .travis.yml

###### Setup hosts files

    vim ~/ansible-vault/hosts

Add server list

    [localhost]
    localhost ansible_connection=local #add variable ansible_connection=local in order not to try to use SSH to contact the hosts

###### Setup playbook

    vim ~/ansible-vault/playbook.yml

Add lines:

    - hosts: localhost
      roles:
        - vault

###### Create secret file

    touch ~/ansible-vault/roles/vault/secret.txt

And type the secret message. My messae is:

    This is a very confidential information.
    Because this file contains username and password.
    Do not store this file into repository without encrypting first.

Then encrypt secret.txt using ansible-vault. But first you have to create the secret code and stored into file.

     echo '2016$10$05' > ~/.vault_pass.txt

     ansible-vault encrypt ~/ansible-vault/roles/vault/files/secret.txt --vault-password-file ~/.vault_pass.txt

Of couse you can decrypt the files, using

     ansible-vault decrypt ~/ansible-vault/roles/vault/files/secret.txt --vault-password-file ~/.vault_pass.txt

But in this step, we do not need to decrpyt since the **ansible-playbook** command will do the magic.

##### Setup task

    vim ~/ansible-vault/roles/vault/tasks/main.yml

Add lines:

    ---
    # tasks file for copy files
    - name: copy secret.txt
      copy: src=secret.txt dest=/tmp

### Run your playbook

    cd ~/ansible-vault
    ansible-playbook playbook.yml -i hosts --vault-password-file ~/.vault_pass.txt

You can check the result in the **/tmp/secret.txt**. The file is copied and decrypted as well.
