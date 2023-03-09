from telnetlib import Telnet
with Telnet('127.0.0.1', 9000) as tn:
    tn.interact()