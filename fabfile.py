## Importing all the libraries that we require
from fabric.api import run,env,sudo,task,local,runs_once,put,abort
import os
import platform
import argparse
import socket
import time
import fabric



 

#env.user = os.environ['FAB_USERNAME']
#env.password = os.environ['FAB_PASSWORD']



#env.hosts=[""]


def get_hosts():
    env.hosts = open('hosts', 'r').readlines()

def filesystem():
	sudo("df -h")
	sudo("fdisk -l /dev/sdb")

def blade_gen():
    sudo("dmidecode -t system")

def timezone():
	sudo("date")
	sudo("mv /etc/localtime /etc/localtime_BKP")
	sudo("ln -s /usr/share/zoneinfo/EST5EDT /etc/localtime")
	sudo("date")

def checktime():
	sudo("date")
def zonelist():
        sudo("sudo su - root")
	sudo("zoneadm list -vc")

def filesystem():
	host=run('echo $(hostname) |cut -d "." -f1')	
	sudo("mkdir /tmp/" + host)

def checkos():
	sudo("cat /etc/*-release ")
	
def chefclient():
	sudo("chef-client -o neustar-yum::yum_cleanup")
	sudo("chef-client -o neustar-yum::latest")

def chekchef():
	sudo("cat /etc/chef/client.rb")

def enummount():
	if  ("vgdisplay |grep -i free |awk {'print $7;'}") >= "20.00":
	  print "Passed"
	  ("lvextend -L+20G /dev/rootvg/lvopt")
	  ("resize2fs /dev/rootvg/lvopt")
	  print ("df -h|grep -i opt")

        else:
	  print "Failed"
def rhmkey():
	put("/Users/kyanaman/fab/rhmkey.pub","/tmp",use_sudo=True)
	sudo("cat /tmp/rhmkey.pub >> /root/.ssh/authorized_keys")
	sudo("rm /tmp/rhmkey.pub")

def samba_version():
	sudo ("rpm -q samba |grep 3.6.23")

def check_sshconfig():
	sudo("cat /etc/ssh/sshd_config |grep -i tcpforward")

def check_ssh():
	sudo("rpm -qa |grep -i openssh")

def samba_singning():
	sudo("cat /etc/samba/smb.conf |grep -i signing")

def hostname():
	sudo("hostname")

def xenhost():
        sudo("cat /etc/*-release")
        sudo("xm list")

def chef_gems():
	host=run('echo $(hostname)')
        run("echo $host")
	os.system("scp /Users/kyanaman/fab/chef-gems/'di-ruby-lvm-0.2.1.gem' host:/tmp")

 
def file_send(localpath,remotepath):
    put(localpath,remotepath,use_sudo=True)
 
def file_send_mod(localpath,remotepath,mod):
    put(localpath,remotepath,mode=int(mod, 8))
	
def monit_summary():
	sudo("monit summary")
