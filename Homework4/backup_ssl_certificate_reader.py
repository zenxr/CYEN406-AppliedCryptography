import ssl
import socket
import sys

def parseArgs():
    if len(sys.argv) > 3 or len(sys.argv) <= 1:
		print("Incorrect usage:")
		print("   First argument : hostname")
		print("   Second argument : port")
		exit()
	else:
		if len(sys.argv) == 3:
			# return the passed address and port
			return {sys.argv[1], sys.argv[2]}
		if len(sys.argv) == 2:
			# return the passed address and default port
			return {sys.argv[1], "443"}

# pass this function a list with 
def printOutput():
	print "Output:\t" + l[0]
	print "Domain Names:\t" + l[1]
	print "Issue Date:\t" + l[2]
	print "Expiry Date:\t" + l[3]
	print "Issuer's CN:\t" + l[4]
	print "CA Issuers: \t" + l[5]
	print "OCSP:\t\t" + l[6]
	print "Cipher:\t\t" + l[7]
	print "SSL Version:\t" + l[8]
	print "Secret Bits:\t" + l[9]

# parse arguments
ip_addr, port = parseArgs()

# create socket and get cert
s = socket()
c = ssl.wrap_socket(s,cert_reqs=CERT_NONE)
# attempt to connect
try:
    c.connect((ip_addr, port))
except:
    response = False
else:
    certObject = c.getpeercert()
    
# c.cipher() returns encryption used



{'issuer': ((('countryName', 'IL'),),
            (('organizationName', 'StartCom Ltd.'),),
            (('organizationalUnitName',
              'Secure Digital Certificate Signing'),),
            (('commonName',
              'StartCom Class 2 Primary Intermediate Server CA'),)),
 'notAfter': 'Nov 22 08:15:19 2013 GMT',
 'notBefore': 'Nov 21 03:09:52 2011 GMT',
 'serialNumber': '95F0',
 'subject': ((('description', '571208-SLe257oHY9fVQ07Z'),),
             (('countryName', 'US'),),
             (('stateOrProvinceName', 'California'),),
             (('localityName', 'San Francisco'),),
             (('organizationName', 'Electronic Frontier Foundation, Inc.'),),
             (('commonName', '*.eff.org'),),
             (('emailAddress', 'hostmaster@eff.org'),)),
 'subjectAltName': (('DNS', '*.eff.org'), ('DNS', 'eff.org')),
 'version': 3}
