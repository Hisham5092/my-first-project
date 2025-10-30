# File Handling

# f = open("Test File.txt", "x")
# with open("Test File.txt", "a") as f:
#     f.write("\nOne More")
#
# with open("Test File.txt") as f:
#     print(f.read())

# JSON
# import json
# from urllib.request import urlopen
#
# # Get fake users
# url = "https://jsonplaceholder.typicode.com/users"
# # url = "https://api.open-meteo.com/v1/forecast?latitude=40.7128&longitude=-74.0060&current_weather=true"
#
# with urlopen(url) as response:
#     source = response.read()
#     data = json.loads(source)
#     # print(json.dumps(data, indent=2))
#     for items in data:
#         name = items['company']['name']
#         print(name)

# Directory

# import os
# from datetime import datetime
#
# # os.chdir('C:/Users/Hisham/Desktop')
#
# # for dirpath, dirnames, filenames in os.walk('/Users/Hisham/Desktop'):
# #     print("Current path: ", dirpath)
# #     print("Directories: ", dirnames)
# #     print("Files", filenames)
# #     print()
#
# print(os.environ.get("Desktop"))


# Regular Expression

import re
# from wsgiref.validate import bad_header_value_re
#
# text = '''Hey, how are you doing? Hope all is well. abc. 123-456-7898. Mr. Schafer. Mr Smith. Ms Davis. Mrs. Robinson. Mr. T
# hisham@gmail.com
# hisham.ahmed@gmail.edu
# hisham-321-ahmed@gmail.net
#
# https://www.google.com
# http://www.hisham.com
# https://www.youtube.com
# https://www.nasa.gov
# '''
# Number = 123-456-7898
# pattern = re.compile(r'abc')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
# pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z]+\.[a-z]+')
# pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# # matches = pattern.finditer(text)
# matches = pattern.findall(text)
# # subbed_urls = pattern.sub(r'\2\3', text)
# # print(subbed_urls)
#
# for match in matches:
#     print(match)
#     # print(match.group(0))

# with open('Test File.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)

# Mail Search
import re

# pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#
# emails = [
#     "test@gmail.com",      # ✓
#     "user.name@yahoo.co.uk",  # ✓
#     "invalid.email",       # ✗ (no @)
#     "@gmail.com",          # ✗ (no username)
#     "test@.com"            # ✗ (invalid domain)
# ]
#
# for email in emails:
#     if re.match(pattern, email):
#         print(f"✓ {email} is valid")
#     else:
#         print(f"✗ {email} is invalid")

# Phone Number

import re

# Match: (123) 456-7890 or 123-456-7890
# pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
#
# phones = [
#     "(123) 456-7890",  # ✓
#     "123-456-7890",    # ✓
#     "123.456.7890",    # ✓
#     "1234567890",      # ✓
#     "12-345-6789"      # ✗ (wrong format)
# ]
#
# for phone in phones:
#     if re.match(pattern, phone):
#         print(f"✓ {phone} is valid")
#     else:
#         print(f"✗ {phone} is invalid")

# Password Validation

import re

# Password must be 8-20 characters, contain letter and number
# pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$'
#
# passwords = [
#     "Pass1234",      # ✓
#     "short1",        # ✗ (too short)
#     "NoNumbers",     # ✗ (no numbers)
#     "12345678"       # ✗ (no letters)
# ]
#
# for pwd in passwords:
#     if re.match(pattern, pwd):
#         print(f"✓ {pwd} is valid")
#     else:
#         print(f"✗ {pwd} is invalid")

# Extract All Numbers from Text
# import re
#
# text = "I have 3 apples and 12 oranges. Total: 15 fruits."
#
# # Find all numbers
# numbers = re.findall(r'\d+', text)
# print(numbers)  # ['3', '12', '15']

# Find Words Starting with 'a'

# import re

# text = "apple and avocado are awesome fruits"
#
# # Find words starting with 'a'
# words = re.findall(r'\ba\w+', text)
# print(words)  # ['apple', 'and', 'avocado', 'are', 'awesome']

# Full Email Parser Script

# import re
# import json
# from pprint import pprint
#
# def parse_email(email_body):
#     result = {}
#     mail_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}'
#     result['email'] = re.findall(mail_pattern, email_body)
#
#     phone_number = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
#     result['phone no'] = re.findall(phone_number, email_body)
#
#     order_pattern = r'ORD(?:ER)?-[A-Z0-9]+'
#     result['order'] = re.findall(order_pattern, email_body)
#
#     date_pattern = r'\d{2}[-/]\d{2}[-/]\d{4}'
#     result['date'] = re.findall(date_pattern, email_body)
#
#     price_pattern = r'\$[\d,]+\.?\d*'
#     result['price'] = re.findall(price_pattern, email_body)
#
#     positive = bool(re.search(r'\b(great|excellent|happy|satisfied)\b', email_body, re.IGNORECASE))
#     negative = bool(re.search(r'\b(bad|terrible|disappointed|poor)\b', email_body, re.IGNORECASE))
#
#     if positive:
#         result['sentiment'] = 'positive'
#     elif negative:
#         result['sentiment'] = 'negative'
#     else:
#         result['sentiment'] = 'neutral'
#     return result
#
# # Test
# email = """
# Hi there,
#
# Your order ORDER-12345 has been shipped!
# Total: $99.99
# Expected delivery: 12/25/2024
#
# Contact us at support@company.com or call (123) 456-7890
#
# Thanks for your purchase! We're happy to serve you.
# """
#
# result = parse_email(email)
# for key, value in result.items():
#     print(f"{key}: {value}")
# print(json.dumps(result, indent=2))
# pprint(result)


# Requests

import requests
# payload = {'page': 2, 'count': 25}
# r = requests.get("https://httpbin.org/get", params=payload)
# payload = {'username': 'hisham', 'count': 'testing'}
# r = requests.post("https://httpbin.org/post", data=payload)
# r = requests.get("https://httpbin.org/basic-auth/hisham/testing", auth=('hisham', 'testing'))
# print(r.text)

# Try Catch

# try:
#     f = open('Test File.txt')
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f.read())
#     f.close()
# finally:
#     print("Executing finally!")

# Error Handling

# import requests
#
# try:
#     response = requests.get('https://api.example.com/data', timeout=5)
#     response.raise_for_status()  # Raises error for 4xx, 5xx
#     data = response.json()
# except requests.exceptions.Timeout:
#     print("Request timed out")
# except requests.exceptions.RequestException as e:
#     print(f"Error: {e}")

import requests

# urls = [
#     'https://jsonplaceholder.typicode.com/users/1',  # Success
#     'https://jsonplaceholder.typicode.com/users/999999',  # 404 Error
#     'https://httpbin.org/delay/10',  # Timeout (if timeout=5)
#     'https://thissitedoesnotexist123456789.com'  # Connection Error
# ]

# for url in urls:
#     print(f"\nTrying: {url}")
#     try:
#         response = requests.get(url, timeout=5)
#         response.raise_for_status()
#         data = response.json()
#         print(f"✓ Success: {list(data.keys())[:3]}")
#     except requests.exceptions.Timeout:
#         print("⏱️ Timeout!")
#     except requests.exceptions.RequestException as e:
#         print(f"❌ Error: {type(e).__name__}")

# Excel

# from openpyxl import load_workbook, Workbook
#
# wb = Workbook()
# sheet = wb.active
# sheet.append(['Name', 'Email'])
# sheet.append(['John', 'john@example.com'])
# wb.save('output.xlsx')


# Python to JSON
# import json
# from urllib.request import urlopen
# url = "https://jsonplaceholder.typicode.com/users"
# with urlopen(url) as response:
#     source = response.read()
#     data = json.loads(source)
    # print(json.dumps(data, indent=2))
    # for items in data:
    #     name = items['company']['name']
    #     print(name)



# Saving JSON to A new File

# import json
#
# from urllib.request import urlopen
#
# url = 'https://jsonplaceholder.typicode.com/users'
#
# with urlopen(url) as response:
#     source = response.read()
#     data = json.loads(source)
#     # print(json.dumps(data, indent=2))
#     users_info =[]
#     for items in data:
#         # name = items['name']
#         # name = items['name'], items['email'], items['address']['city'], items['phone'], items['website'], items['company']['name']
#         user_data = {
#             'Name': items['name'],
#             'Email': items['email'],
#             'Address[City]': items['address']['city'],
#             'Phone No': items['phone'],
#             'Website': items['website'],
#             'Company Name': items['company']['name']
#         }
#         users_info.append(user_data)
#         # print(json.dumps(user_data, indent=2))
#         with open('data.json', 'w') as f:
#             json.dump(users_info, f, indent=2)

# with open('data.json', 'w') as f:
#     try:
#         f.write('')
#     except Exception as e:
#         print(f"Error: {e}")
#     else:
#         print('Successful')


# Loading JSON File and Updating Value and Saving It Back

import json

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
    data[0]['Name'] = 'Lisa'
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
except FileNotFoundError as e:
    print(f"Error: {e}")
else:
    print("Name updated successfully")







