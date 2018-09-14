from lxml import html
import requests
import itertools
import csv

download_dir1 = "C:\\Users\\Gowshalini\\Desktop\\FacultiesUOM.csv" #where you want the file to be downloaded to 
csv = open(download_dir1, "w") 

columnTitleRow = "Faculty name,faculty link,description\n"
csv.write(columnTitleRow)


#FACULTIES
homeurl='https://www.mrt.ac.lk/web/'
homepage = requests.get(homeurl, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(homepage.content)
FACULTYnames = hometree.xpath('//*[@id="block-toplinks"]/div/ul/li[1]/ul/li/a')

urls = ['https://www.mrt.ac.lk/web/foa','https://www.mrt.ac.lk/web/efac','https://www.mrt.ac.lk/web/itfac','https://www.mrt.ac.lk/web/business','https://www.mrt.ac.lk/web/fgs']
for fa,url in itertools.zip_longest(FACULTYnames,urls):
    facname= fa.xpath('./text()')
    faclink=url
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    tree = html.fromstring(page.content)
    desc = tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/p')
    
    for des in desc:
        de=des.xpath('.//text()')        
        de=str(de[0]).replace(',',';')
        row=facname[0]+','+faclink+','+de+'\n'
        csv.write(row)
    if len(desc)==0:
        row=facname[0]+','+faclink+'\n'
        csv.write(row)
csv.close()  

    
  
