# Importing all the essential libraries
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Opening the url
page = urlopen('https://www.flipkart.com/mens-watches-store?otracker=nmenu_sub_Men_0_Watches')

# Parsing the extracted page using BeautifulSoup
soup = BeautifulSoup(page, 'lxml')

# Getting each watch product using class id of its division
dabba = soup.find_all('div', class_="_3liAhj _2Vsm67")

# Empty list
items = []

# Traversing through all the extracted watch products
for i in range(dabba.__len__()):
    each = list()
    # Appending the watch product title to list using class name
    each.append(dabba[i].find('a', class_="_2cLu-l").text)
    # Appending the watch product price to list using class name
    each.append(dabba[i].find('div', class_="_1vC4OE").text)

    # If discount is given on any item
    if dabba[i].find('div', class_="VGWI6T"):
        # Appending the watch product discount to list using class name
        each.append(dabba[i].find('div', class_="VGWI6T").text)
    else:
        # Else append NAN
        each.append("NAN")
    # Append the list to items list
    items.append(each)

# Creating a DataFrame of items library using pandas
df = pd.DataFrame(items, columns = ["Name", "Price", "Discount"])

# Exporting the extracted data into a csv file
df.to_csv('watches.csv')

# Printing the dataframe
print(df)