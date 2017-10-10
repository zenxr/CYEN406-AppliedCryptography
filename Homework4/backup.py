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

def topLevelSearch(obj, searchString, tabs):
    # working with dictionaries here
    for k, v in obj.items():
        if k == searchString:
            return v

def getDNS(obj):
    for k, v in obj.items():
        if k == "subjectAltName":
            for i in v:
                print "\t\t" +i[1]

def getCAIssuersAndOCSP(obj, string):
    for k, v in obj.items():
        if k == string:
            for i in v:
                print i

def printOutput(cert, dictCert, cipher_twopull):
    print "Output:"
    print "Domain Names:"
    getDNS(dictCert)
    print "Issue Date:\t",
    print topLevelSearch(dictCert, "notBefore", 0)
    print "Expiry Date:\t",
    print topLevelSearch(dictCert, "notAfter", 0)
    print "Issuer's CN:\t",
    print cert.get_issuer().CN
    print "CA Issuers:\t",
    getCAIssuersAndOCSP(dictCert, "caIssuers") 
    print "OCSP:\t\t",
    getCAIssuersAndOCSP(dictCert, "OCSP")
    print "Cipher:\t\t",
    print cipher_twopull[0]
    print "SSL Version:\t",
    print cipher_twopull[1]
    print "Secret Bits:\t",
    print cipher_twopull[2]

def main(argv):
    # parse arguments
    ip_addr, port = parseArgs()
    # get the certificate
    s = socket.socket()
    contxt = ssl.create_default_context()
    s = contxt.wrap_socket(socket.socket(), server_hostname = ip_addr)
    s.connect((ip_addr, port))
    binCert = s.getpeercert(True)
    dictCert = s.getpeercert(False)
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, binCert)
    #print the output
    printOutput(cert, dictCert, s.cipher())

if __name__ == "__main__":
    main(sys.argv)
