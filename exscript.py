from Exscript import Host, Account
from Exscript.protocols import SSH2
from Exscript.util.start import start

account = Account('cisco', 'cisco')
host = Host('ssh://192.168.1.88')
host.set_account(account)

conn = SSH2()

def do_something(job, host, conn):
    conn.execute('terminal length 0')
    conn.send("enable\r")
    conn.app_authorize(account)
    conn.execute('conf t')
    conn.execute('ip domain name http://google.fr')

start([account], [host], do_something)