# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# from io import StringIO
# import csv
# from github import Github

# def main():
#     url = 'https://payaneh.ir/bus/index/Esfahan/Ahvaz?date=1401-12-20'
#     response = requests.get(url)
#     print(response.status_code)
#     sleep(5)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     with open (file='./html.html',mode='w', encoding='utf-8') as file:
#         file.write(str(soup))
#         print('written!')
#     # print(soup)
#     msg_box = soup.select('#app .img-fluid')
#     print(len(msg_box))

#     raw_repo_main_url = 'https://raw.githubusercontent.com/thewoood/ticket-cloud/main/'
#     token = ''
#     previous_count = Load_Github('ticket.csv', raw_repo_main_url, token)


# def Load_Github(file_name, raw_repo_main_url, token):
#     url = raw_repo_main_url+file_name

#     # HTTP headers
#     headers = {'Authorization': f'token {token}'}

#     # Make the HTTP request
#     response = requests.get(url, headers=headers)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Convert the response content to a string buffer
#         content = response.content.decode('utf-8')
#         buffer = StringIO(content)

#         # Read the CSV file from the string buffer
#         reader = csv.DictReader(buffer)
#         data = list(reader)

#         # Print the data
#         print(f'{len(data)} rows loaded from {file_name} successfully!')
#         return data
#     else:
#         print('Failed to read the CSV file.')

# def Upload_Github(file_name_on_github, new_data, username, token, csv_headers, repo_name ):
#         # File details
#         csv_data = StringIO()
#         csv_writer = csv.DictWriter(csv_data, fieldnames=csv_headers)
#         csv_writer.writeheader()
#         csv_writer.writerows(new_data)

#         # Read CSV file content
#         file_content = csv_data.getvalue()

#         # Authenticate with GitHub
#         g = Github(username, token)

#         # Get the repository
#         repo = g.get_user().get_repo(repo_name)

#         # Check if the file exists
#         try:
#             file = repo.get_contents(file_name_on_github)
#             # Update the existing file
#             repo.update_file(file.path, 'Updated!', file_content, file.sha)
#             print(f'mew records added!')
#         except :
#             # Create a new file
#             repo.create_file(file_name_on_github, 'Created!', file_content)
#             print(f'File "{file_name_on_github}" created and uploaded successfully!')



import requests

url = 'https://ws.alibaba.ir/api/v2/bus/available?orginCityCode=36390000&destinationCityCode=21310000&requestDate=2023-03-31&passengerCount=1'
response = requests.get(url)

print(response.json())