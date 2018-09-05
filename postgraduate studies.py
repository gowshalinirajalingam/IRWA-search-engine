from lxml import html
import requests
import itertools
import csv

download_dir = "C:\\Users\\Gowshalini\\Desktop\\Postgraduate Programs.csv" #where you want the file to be downloaded to 
csv = open(download_dir, "w") 
columnTitleRow = "program Catagory,program catagory link,faculty name,faculty link,faculty program ,faculty program links\n"
csv.write(columnTitleRow)

url = 'https://www.mrt.ac.lk/web/'
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)

#postgraduate studies
postGrad = hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[2]/strong/a/text()')
postGradlink=hometree.xpath('//*[@id="block-menuforeducation2"]/div/div/ul/li[2]/ul/li[1]/a/@href')
faculty = hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[2]/ul/li/a/text()')
facultylink=hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[2]/ul/li/a/@href')
for pp in faculty:

  if pp=='Faculty of Engineering':
       row=postGrad[0]+',https://www.mrt.ac.lk'+postGradlink[0]+','+pp+'\n'
       csv.write(row)
       
  if pp=='Faculty of Information Technology':
       url = '  https://www.mrt.ac.lk/web/itfac/education/postgraduate' 
       page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
       tree = html.fromstring(page.content)
       pgp = tree.xpath('///*[@id="block-scholarly-content"]/div/article/div/div/div/ul/li/a')

       for pg in pgp:
           program=pg.xpath('./text()')
           link=pg.xpath('./@href')
           row=postGrad[0]+',https://www.mrt.ac.lk'+postGradlink[0]+','+pp+',https://www.mrt.ac.lk'+facultylink[1]+','+program[0]+',https://www.mrt.ac.lk'+link[0]+'\n'
           csv.write(row)
           
      
  if pp=='Faculty of Architecture':
       row=postGrad[0]+',https://www.mrt.ac.lk'+postGradlink[0]+','+pp+',https://www.mrt.ac.lk'+facultylink[2]+'\n'
       csv.write(row)
           
csv.close()