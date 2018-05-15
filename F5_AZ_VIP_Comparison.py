import re
import difflib
import sys

fhandle=open('Active.txt', 'r')
fhandle1=open('Standby Configs.txt', 'r')
str=fhandle.read()
str1=fhandle1.read()


f=open("AZA-LB-001.txt","w+")
g=open("AZB-LB-002.txt","w+")
h=open("Vip_Diff.txt","w+")


y=re.findally=re.findall('^.+(?:.+virtual.+-VS|virtual.+Environments-HTTP|virtual.+Environment-HTTP|virtual.+Environment-VS |virtual.+Environment-HTTP-WP) [\s\S]*?.+vs-index [0-9].*\n*}',str, re.MULTILINE)
y1=re.findall('^ltm virtual .+AZ2b {[\s\S]*? .+vs-index [0-9].*\n*}',str1, re.MULTILINE)



for line in y:
    f.write(line)

for line in y1:
    g.write(line)


with open('C:/Ramesh/Python Programs/AZa.txt', 'r') as Active:
    with open('C:/Ramesh/Python Programs/AZb.txt', 'r') as Standby:
        diff = difflib.unified_diff(
            Active.readlines(),
            Standby.readlines(),
            fromfile='lb001',
            tofile='lb002',
        )
        for line in diff:
#            sys.stdout.write(line)
			h.write(line)
