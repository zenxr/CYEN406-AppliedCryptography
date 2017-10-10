#       Cody Stephenson
#       Assignment 4
#       SSL Cert
#       5-10-17
#       
#       Sources used: stackoverflow, docs.python.org
#
#       Description:
#           This program connects to a foreign hostname and fetches an ssl certificate
#           It then proceeds to determine information about the certificate recieved.
#       
#       Note: BONUS NOT ATTEMPTED
#
#
import ssl
import socket
import sys
import re
import OpenSSL


# parses arguments.......
def parseArgs():
    if len(sys.argv) > 3 or len(sys.argv) <= 1:
        print("Incorrect usage:")
        print("   First argument : hostname")
        print("   Second argument : port")
        exit()
    else:
        # if given a port, use it
        if len(sys.argv) == 3:
            # return the passed address and port
            return sys.argv[1], int(sys.argv[2])
        # otherwise, use 443
        if len(sys.argv) == 2:
            # return the passed address and default port
            return sys.argv[1], 443

# searches the top level of the certificate (subject, notBefore, etc)
def topLevelSearch(obj, searchString, tabs):
    # working with dictionaries here
    for k, v in obj.items():
        if k == searchString:
            return v

# prints the DNSs registered
def getDNS(obj):
    for k, v in obj.items():
        if k == "subjectAltName":
            for i in v:
                print "\t\t" +i[1]

# prints caIssuers and OCSP
def getCAIssuersAndOCSP(obj, string):
    for k, v in obj.items():
        if k == string:
            for i in v:
                print i

# for neatly printing our output
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
    # create a socket and some context
    s = socket.socket()
    contxt = ssl.create_default_context()
    s = contxt.wrap_socket(socket.socket(), server_hostname = ip_addr)
    # connect to the hostname/ip
    s.connect((ip_addr, port))
    # binCart is a binary equivalent
    binCert = s.getpeercert(True)
    # dictCert is the dictionary object that can be returned
    dictCert = s.getpeercert(False)
    # convert the binCert into a more accessible format for openssl.crypto
    cert = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_ASN1, binCert)
    #print the output
    printOutput(cert, dictCert, s.cipher())

if __name__ == "__main__":
    main(sys.argv)
