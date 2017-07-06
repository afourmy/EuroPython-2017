from Exscript import Host, Account
from Exscript.protocols import SSH2
from Exscript.util.start import start

hosts = []
for ip in ('192.168.1.88', '192.168.1.88'):
    account = Account('cisco', 'cisco')
    host = Host('ssh://{host_ip}'.format(host_ip=ip))
    host.set_account(account)
    hosts.append(host)
    
conn = SSH2()

def do_something(job, host, conn):
    conn.execute('terminal length 0')
    conn.send("enable\r")
    conn.app_authorize(account)
    conn.execute('configure terminal')
    conn.execute('hostname router2')

start([account], hosts, do_something, max_threads=5)