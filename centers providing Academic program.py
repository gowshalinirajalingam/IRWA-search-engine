from lxml import html
import requests
import itertools
import csv

download_dir = "C:\\Users\\Gowshalini\\Desktop\\Centers Providing academic program.csv" #where you want the file to be downloaded to 
csv = open(download_dir, "w") 
columnTitleRow = "Centers Providing academic program,description,url\n"
csv.write(columnTitleRow)

url = 'https://www.mrt.ac.lk/web/centres-providing-academic-programmes'
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
tree = html.fromstring(page.content)

centers=tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/ul/li')
description = tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/p')

for ce,de in itertools.zip_longest(centers,description):
    desc=de.xpath('.//text()')
    center=ce.xpath('.//text()')
    link=ce.xpath('.//@href')
    if len(link)>0 and not str(link[0]).startswith("http"):
        row = center[0]+','+desc[0]+',https://www.mrt.ac.lk'+link[0]+'\n'
        csv.write(row)
    elif len(link)>0 and str(link[0]).startswith("http"):
        row = center[0]+','+desc[0]+','+link[0]+'\n'
        csv.write(row)
    else:
        row = center[0]+','+desc[0]+'\n'
        csv.write(row)


csv.close()
    