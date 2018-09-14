from lxml import html
import requests
import itertools
import csv

#programs in researchandpsychology
homeurl = 'https://researchandpsychology.com/Academic/index/'

download_dir = "C:\\Users\\Gowshalini\\Desktop\\Programs in CIRP.csv" #where you want the file to be downloaded to 
csv = open(download_dir, "w") 


columnTitleRow = "program Type,program Type url,Degree name,degree url,degree desc\n"
csv.write(columnTitleRow)


page = requests.get(homeurl, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)

undergraduateurl=homeurl+hometree.xpath('//*[@id="spy"]/ul/li[2]/a/@href')[0]
postgraduateurl=homeurl+hometree.xpath('//*[@id="spy"]/ul/li[13]/a/@href')[0]
diplomaurl=homeurl+hometree.xpath('//*[@id="spy"]/ul/li[16]/a/@href')[0]

degree = hometree.xpath('//*[@id="spy"]/ul/li/a')

dename=[]
link=[]
newlink=[]
for de in degree:
    dename.append(de.xpath('./text()'))
    link.append(de.xpath('./@href'))
    

for lin in link:
    if not str(lin[0]).startswith('https'):
        newlink.append('https://researchandpsychology.com/'+lin[0])
    else:
        newlink.append(lin[0])
    
for de,li in  itertools.zip_longest(dename[1:11],newlink[1:11]):
    #undergraduate
    page = requests.get(li, headers={'User-Agent': 'Mozilla/5.0'})
    tree = html.fromstring(page.content)
    desc=tree.xpath('//*[@class="intro-container"]/p/text()')
    
    for d in desc:
        d=str(d).replace(',',';')
        row='undergraduate,'+undergraduateurl+','+de[0]+','+li+','+d+'\n'
        csv.write(row)
    
for de,li in  itertools.zip_longest(dename[12:14],newlink[12:14]):
    #postgraduate
    page = requests.get(li, headers={'User-Agent': 'Mozilla/5.0'})
    tree = html.fromstring(page.content)
    desc=tree.xpath('//*[@class="intro-container"]/p/text()')
    
    for d in desc:
        d=str(d).replace(',',';')        
        row='postgraduate,'+postgraduateurl+','+de[0]+','+li+','+d+'\n'
        csv.write(row)
    
for de,li in  itertools.zip_longest(dename[15:20],newlink[15:20]):
    #diploma
    page = requests.get('https://researchandpsychology.com/Diplomacriminalandforensicpscyhology', headers={'User-Agent': 'Mozilla/5.0'})
    tree = html.fromstring(page.content)
    desc=tree.xpath('//*[@class="intro-container"]/p/text()')
    
    for d in desc:
        d=str(d).replace(',',';')
        row='diploma,'+diplomaurl+','+de[0]+','+li+','+d+'\n'
        csv.write(row)

csv.close()

