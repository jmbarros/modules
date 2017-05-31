#!/usr/bin/python 
#create inception
### todo
# add check slcli file
#######################################################################
#defs

import os

def yum_install ( pkg ):
   "install via yum"
   install = "yum install -y  " + pkg
   os.system(install)
   return;

def play_book ( pb ):
   "run playbook"
   book = "ansible-playbook ./" + pb
   os.system(book)
   return;

def install_galaxy ( galaxy ):
   "install galaxy repo"
   ig = "ansible-galaxy install " + galaxy
   os.system(ig)
   return;


 ############
yum_install("epel-release")
yum_install( "ansible" )
install_galaxy( "jmbarros.common" )
install_galaxy( "jmbarros.os_newton")
play_book ( "bs_os_newton.yml" )