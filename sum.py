import pandas as pd
import re


# URL for parsing
url = 'https://archive.org/download/sat2352repo'
# Reading the tables on the page
df = pd.read_html(url)
# Selecting the desired table
df = df[0]
# Removing uninformative first row
df = df.drop(0)
# We are inerested in "Size" column
#print(df['Size'])
# Setting the variable for total size in bytes (in 'float' format).
# Size at this point it's zero.
total_b = 0.0
# For each cell entry, we need to sort the data by units (B - Bytes, K - Kilobytes or M - Megabytes)
for i in df['Size']:
    # Data is in float format, but sum gives us nothing at this point, and act as concatenation of strings
    if 'B' in i:
        # Converting data to string format
        i = str(i)
        # Let's get the digits
        number = re.findall('[1-9]\d*\.\d+?',i)
        # and convert it to float
        number = float(number[0])
        #print(number)
        # As this data is in bytes - we don't need to do any extra math with it
        # and we can just add it to our total bytes counter
        total_b = total_b + number
    if 'K' in i:
        # Logic is the same
        i = str(i)
        number = re.findall('[1-9]\d*\.\d+?',i)
        # But we are handling data in Kilobytes (1Kb = 1024 bytes)
        number = float(number[0]) * 1024
        #print(number)
        total_b = total_b + number
    if 'M' in i:
        # Same logic
        str(i)
        i = i.replace('M',' M')
        number = re.findall('[1-9]\d*\.\d+?',i)
        # The data is in Megabytes (1Mb = 1024 Kilobytes)
        number = float(number[0]) * 1024 * 1024
        #print(number)
        total_b = total_b + number
    if 'G' in i:
        str(i)
        number = re.findall('[1-9]\d*\.\d+?',i)
        # The data is in Gigabytes (1Gb = 1024 Megabytes)
        number = float(number[0]) * 1024 * 1024 * 1024
        #print(number)
        total_b = total_b + number

print('Library size in bytes: ' + str(total_b))
print('Library size in Kilobytes: ' + str(total_b/1024))
print('Library size in Megabytes: ' + str(total_b/1024/1024))
print('Library size in Gigabytes: ' + str(total_b/1024/1024/1024))
