# Open a file and read its contents line by line
with open('/Users/colinneville/Documents/PythonTemp.csv', mode='w', encoding='utf-8') as weather_file:
    weather_file.write('Hello World!' + '\n')