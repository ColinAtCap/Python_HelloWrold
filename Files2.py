#
print("Reading from a file")
with open('/Users/colinneville/Documents/weatherAUS.csv', mode='r', encoding='utf-8') as weatherAUS:

    host_contents = weatherAUS.read(256)
    print(host_contents)

    rec = weatherAUS.tell()
    print(rec)

    host_contents = weatherAUS.read(256)
    print(host_contents)

print("End of file reached:")

