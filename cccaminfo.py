import sys
import telnetlib

def usage():
    print """
    cccaminfo - by Jay Turla @shipcod3

    *********
    Usage:
    *********
    python cccaminfo.py <host>
    example -> cccaminfo.py localhost
    """
    
"""
    Supported Commands:
    - info
    - activeclients
    - clients
    - servers
    - shares
    - providers
    - entitlements
"""

def main(argv):
    if len(argv) < 2:
        return usage()

    host = sys.argv[1]
    
    #info command
    tn = telnetlib.Telnet(host, 16000)
    tn.read_until("Welcome to the CCcam information client.")
    print "[+] Getting information on the receiver\n"
    tn.write("info\r")
    print tn.read_all()
    
    #activeclients command
    tn = telnetlib.Telnet(host, 16000)
    tn.read_until("Welcome to the CCcam information client.")
    print "[+] Active clients\n"
    tn.write("activeclients\r")
    print tn.read_all()

    #clients command
    tn = telnetlib.Telnet(host, 16000)
    tn.read_until("Welcome to the CCcam information client.")
    print "[+] Clients\n"
    tn.write("clients\r")
    print tn.read_all()

    #servers command
    tn = telnetlib.Telnet(host, 16000)
    tn.read_until("Welcome to the CCcam information client.")
    print "[+] Servers\n"
    tn.write("servers\r")
    print tn.read_all()
    
    #shares command
    tn = telnetlib.Telnet(host, 16000)
    tn.read_until("Welcome to the CCcam information client.")
    print "[+] Shares\n"
    tn.write("shares\r")
    print tn.read_all()

    #providers command
    tn = telnetlib.Telnet(host, 16000)
    tn.read_until("Welcome to the CCcam information client.")
    print "[+] Providers\n"
    tn.write("providers\r")
    print tn.read_all()

    #entitlements command
    tn = telnetlib.Telnet(host, 16000)
    tn.read_until("Welcome to the CCcam information client.")
    print "[+] Entitlements\n"
    tn.write("entitlements\r")
    print tn.read_all()

if __name__ == "__main__":
    main(sys.argv)
