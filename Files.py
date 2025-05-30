#Files

#open('/tmp/python_file.csv', mode='w', encoding='utf-8')

hosts = open('/Users/colinneville/Documents/weatherAUS.csv', mode='r', encoding='utf-8')
host_contents = hosts.read(256)
#print(host_contents)

rec=hosts.tell()
print(rec)

host_contents = hosts.read(256)
print(host_contents)

reset=hosts.seek(0)

rec=hosts.tell()
print(rec)

if not hosts.closed:
    print("File is open")
    hosts.close()
else:
    print("File is closed")


