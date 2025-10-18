# File Handling

# f = open("Test File.txt", "x")
# with open("Test File.txt", "a") as f:
#     f.write("\nOne More")
#
# with open("Test File.txt") as f:
#     print(f.read())


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

