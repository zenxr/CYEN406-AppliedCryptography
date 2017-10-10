import ssl
import socket
import sys
import re
import OpenSSL
#from OpenSSL import crypto

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

# pass this function a list with 
def printOutput(cert):
    print "Output:"
    print "Domain Names:"
    print "Issue Date:\t"
    print cert.get_notBefore(),
    print "Expiry Date:\t"
    print "Issuer's CN:\t",
    print cert.get_issuer().CN
    print "CA Issuers:\t",

    print "OCSP:\t\t"
    print "Cipher:\t\t"
    print "SSL Version:\t",
    print cert.get_version()
    print "Secret Bits:\t"

def getcertificate(ip_addr, port):
    s = socket.socket()
    contxt = ssl.create_default_context()
    s = contxt.wrap_socket(socket.socket(), server_hostname = ip_addr)
    s.connect((ip_addr, port))
    binCert = s.getpeercert(True)
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, binCert)
    return cert
def main(argv):
    # parse arguments
    ip_addr, port = parseArgs()
    # get the certificate
    cert = getcertificate(ip_addr, port)
    # print the output
    printOutput(cert)

if __name__ == "__main__":
    main(sys.argv)
