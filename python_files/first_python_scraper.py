import requests
from bs4 import BeautifulSoup
import csv

# url = "https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s"
url = "https://apps.dca.ga.gov/DRI/Submissions.aspx"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:136.0) Gecko/20100101 Firefox/136.0'}
response = requests.get(url, headers=headers)
print(response.status_code)

# html = response.content
# # print(html)

# soup = BeautifulSoup(html, features="html.parser")
# # print(soup.prettify())

# # Grab all the <tr> elements where valign = bottom

# rows = soup.find_all('tr', attrs={'valign':'bottom'})

# # and print them.  How do they look? 
# for row in rows[0:10]:
#     print(row.get_text())

# They look kind of rough.  
# Let's remember the principle of each cell having just one piece of info.
# Let's separate each line of text into a list of strings. 
# uncomment the next section

# for row in rows[0:10]:
#     # start with an empty list. 
#     list_of_cells = []
#     # Then find all the <td> elements on a given row
#     cells = row.find_all('td')
#     for cell in cells:
#         text = cell.text
#         # find the text in each cell and append it onto that list
#         list_of_cells.append(text)
#     print(list_of_cells)

# This is starting to look a little better. Like a spreadsheet! But how to output it? 
# Re-comment the above section and uncomment the section below:
# start with creating another empty list.  It'll be a list of lists when we're done

# output = []

# for row in rows[0:10]:
#     # start with an empty list. 
#     list_of_cells = []
#     # Then find all the <td> elements on a given row
#     cells = row.find_all('td')
#     for cell in cells:
#         text = cell.text
#         # find the text in each cell and append it onto that list
#         list_of_cells.append(text)
#     print(list_of_cells)
#     # Now this list of cells, append it to output
#     output.append(list_of_cells)

# outfile = open('python_files/ten_rows.csv', 'w')
# writer = csv.writer(outfile)
# for row in output:
#     writer.writerow(row)

#########################################
# NEXT EXERCISE
# MAKE YOUR OUTPUT .CSV have links!
# Re-comment the above section and work on what's below
#########################################


# output = []

# for row in rows[0:10]:
#     # start with an empty list. 
#     list_of_cells = []
#     # Then find all the <td> elements on a given row
#     cells = row.find_all('td')
#     for cell in cells:
#         try:
#             link = cell.find('a')
#             print(link)
#             print(link['href'])
#             list_of_cells.append('https://apps.dca.ga.gov/DRI/' + link['href'])
#         except:
#             text = cell.text
#             list_of_cells.append(text)
#     print(list_of_cells)
#     # Now this list of cells, append it to output
#     output.append(list_of_cells)


# outfile = open('python_files/ten_rows_with_links.csv', 'w')
# writer = csv.writer(outfile)
# for row in output:
#     writer.writerow(row)

##################
# GREAT, now you have scraped text and links from <td> elements 
# A no-coding tool could have done that though.
# 
# But custom scrapers can do more customized jobs, on any schedule you like.  You can run any number of them
# And on your own computer, it will be free too. 
# 
# For more practice, say you cover Fulton County
# And you want to print a message to the terminal every time a Fulton entry appears.
# What do you do?
# 
# 
# For yet more practice, say you cover Fulton and Bulloch counties
# Create an output file that ONLY includes rows from Fulton or Bulloch County
####################

