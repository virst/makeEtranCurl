import xml.etree.ElementTree as ET

lines = []
for line in open('login.info'):
    lines.append(line.strip())

curl = 'curl -vvv --header Accept: --header User-Agent: --header "Cache-Control: no-cache, max-age=0" --header ' \
       '\'SOAPAction: "urn:SysEtranInt"\' --compressed --header "Content-Type: text/xml; charset=utf-8" --data ' \
       '@req.bin '
curl += lines[2]
curl += ' -o reply.bin'

req = open('req.xml').read()

x = ET.Element('s:Envelope')
x.set('xmlns:s', 'http://schemas.xmlsoap.org/soap/envelope/')
b = ET.SubElement(x, 's:Body')
b = ET.SubElement(b, 'GetBlock')
b.set('xmlns', 'SysEtranInt')
ET.SubElement(b, 'Login').text = line[0]
ET.SubElement(b, 'Password').text = line[1]
ET.SubElement(b, 'Text').text = req

z = ET.tostring(x, encoding='unicode')

f = open('req.bin', 'w')
f.write(z)
f.close()

f = open('req.sh', 'w')
f.write('#!/bin/bash')
f.write('\n\n')
f.write(curl)
f.write('\n\n')
