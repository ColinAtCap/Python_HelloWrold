# Open a file and read its contents line by line

with open('/Users/colinneville/Documents/weatherAUS.csv', mode='r', encoding='utf-8') as weather_file:
    for line in weather_file:
        print(line.strip())

