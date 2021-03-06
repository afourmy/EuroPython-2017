from Exscript import Host, Account
from Exscript.protocols import SSH2
from Exscript.util.start import start

# IP of the device + credentials
account = Account('cisco', 'cisco')
host = Host('ssh://192.168.1.88')
host.set_account(account)

conn = SSH2()

def do_something(job, host, conn):
    conn.execute('terminal length 0')
    conn.send("enable\r")
    conn.app_authorize(account)
    conn.execute('show running-config')
    conn.execute('configure terminal')
    conn.execute('hostname france')

start([account], [host], do_something)