from lxml import html
import requests
import itertools
import csv

download_dir = "C:\\Users\\Gowshalini\\Desktop\\Undergraduate Studies.csv" #where you want the file to be downloaded to 
csv = open(download_dir, "w") 
columnTitleRow = "program Catagory,program catagory link,faculty name,faculty link,faculty program ,faculty program links\n"
csv.write(columnTitleRow)

url = 'https://www.mrt.ac.lk/web/'
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)
#undergraduate studies
underGrad = hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[1]/strong/a/text()')
underGradprog = hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[1]/ul/li/a/text()')

for up in underGradprog:
 
  if up=='Faculty of Information Technology':
       url = 'https://www.mrt.ac.lk/web/itfac/education/undergraduate'
       page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
       tree = html.fromstring(page.content)
       itfacugp = tree.xpath('//*/article/div/div/div/ul/li/a')
       
       for it in itfacugp:
           itprograms= it.xpath('./text()')
           link=it.xpath('./@href')
           
           if str(link[0]).startswith("http"):
               row =underGrad[0]+",https://www.mrt.ac.lk/web/eugs,"+up+','+url+','+itprograms[0]+','+link[0]+'\n'
               csv.write(row)
           else:
               row =underGrad[0]+",https://www.mrt.ac.lk/web/eugs,"+up+','+url+','+itprograms[0]+',https://www.mrt.ac.lk'+link[0]+'\n'
               csv.write(row)

       
  if up=='Faculty of Business':    
       url = 'https://www.mrt.ac.lk/web/business'
       page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
       tree = html.fromstring(page.content)
       fab = tree.xpath('//*/article/div/div/div/ul/li/u/a')
       for it in itfacugp:
           fabb= it.xpath('./text()')
           link=it.xpath('./@href')
           
           if str(link[0]).startswith("http"):
               row =underGrad[0]+",https://www.mrt.ac.lk/web/eugs,"+up+','+url+','+fabb[0]+','+link[0]+'\n'
               csv.write(row)
           
           else:
               row =underGrad[0]+",https://www.mrt.ac.lk/web/eugs,"+up+','+url+','+fabb[0]+',https://www.mrt.ac.lk'+link[0]+'\n'
               csv.write(row)

csv.close()
       