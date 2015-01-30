import os,glob
from pexpect import *

c = spawn('bash')
c.expect('\$')
cwd = os.getcwd()
for dir in glob.glob(cwd+os.sep+'*'):
    if os.path.isdir(dir):
        target = os.path.join(dir,".git*")
        c.sendline('rm -rf %s'%target)
        c.expect('\$')
