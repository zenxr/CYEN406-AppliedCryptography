import ssl
import socket
import sys
import re
import OpenSSL
from OpenSSL import crypto

def parseArgs():
    if len(sys.argv) > 3 or len(sys.argv) <= 1:
        print("Incorrect usage:")
        print("   First argument : hostname")
        print("   Second argument : port")
        exit()
    else:
        if len(sys.argv) == 3:
            # return the passed address and port
            return sys.argv[1], int(sys.argv[2])
        if len(sys.argv) == 2:
            # return the passed address and default port
            return sys.argv[1], 443

def searchDict(obj, stringQ, tabs):
    # prepare tabs for formatting
    t = ""
    tabsOG = tabs
    while tabs > 0:
        t = t + "\t"
        tabs = tabs -1
    # if we're searching a dictionary
    if type(obj) == dict:
        # k = key, v = value
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                # print v
                searchDict(v, stringQ, tabsOG)
            else:
                if k == stringQ:
                    #print the value
                    print v
    elif type(obj) == list:
        for v in obj:
            if hasattr(v, '__iter__'):
                searchDict(v, stringQ, tabsOG)
    elif type(obj) == tuple:
        printNext = 0
        for v in obj:
            if printNext:
                print t+v
                printNext = 0
            if hasattr(v, '__iter__'):
                searchDict(v, stringQ, tabsOG)
            if v == stringQ:
                # print the next element
                printNext = 1

# pass this function a list with 
def printOutput(cert, pemCert):
    print "Output:"
    print "Domain Names:"
    searchDict(cert, "DNS", 1)
    print "Issue Date:\t",
    searchDict(cert, "notBefore", 0)
    print "Expiry Date:\t",
    searchDict(cert, "notAfter", 0)
    print "Issuer's CN:\t"
    #searchDict(cert, "commonName", 0)
    print "CA Issuers:\t"
    searchDict(cert, "caIssuers", 0)
    print "OCSP:\t\t"
    print "Cipher:\t\t"
    print "SSL Version:\t",
    searchDict(cert, "version", 0)
    print "Secret Bits:\t"

def main(argv):
    # parse arguments
    ip_addr, port = parseArgs()

    s = socket.socket()
    contxt = ssl.create_default_context()
    s = contxt.wrap_socket(socket.socket(), server_hostname = ip_addr)
    s.connect((ip_addr, port))
    # formatted cert
    cert = s.getpeercert(False)
    # binary cert
    pemCert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, s.getpeercert(True))
    #printOutput(cert, pemCert)
    print cert
if __name__ == "__main__":
    main(sys.argv)
