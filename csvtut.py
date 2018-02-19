import csv
html_list = ''
username = []
with open('sponsers.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    html_list += f'<p>HTML list of top six sponsers </p>'
    html_list += '\n<ul>'
    for line in csv_reader:
      username=line['Username']
      html_list += f'\n\t<li>{username}</li>'
    html_list += '\n</ul>'
print(html_list)
