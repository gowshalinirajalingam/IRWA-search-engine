from lxml import html
import requests
import itertools
import csv

download_dir = "C:\\Users\\Gowshalini\\Desktop\\International Programs.csv" #where you want the file to be downloaded to 
csv = open(download_dir, "w") 
columnTitleRow = "program Catagory,program Type,program type link,faculty name,url,contact person,email,tel\n"
csv.write(columnTitleRow)

url = 'https://www.mrt.ac.lk/web/'
page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)
#international studies
internationalStudies = hometree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[2]/strong/a/text()')
internationalprogram = hometree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[2]/ul/li/a/text()')

for ip in internationalprogram:
    
    if ip == 'Undergraduate Studies':
      
        url = 'https://www.mrt.ac.lk/web/contacts-undergraduate-studies'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        courseinfo = tree.xpath('//table/tbody/tr')
        

        for c in courseinfo:
            fname=c.xpath('./td[1]//text()')
            clink=c.xpath('./td[1]//@href')
            conperson=c.xpath('./td[2]//text()')
            email=c.xpath('./td[3]//text()')
            tel=c.xpath('./td[4]//text()')
            
            if str(clink[0]).startswith("http"):
                row=internationalStudies[0]+','+ip+','+url+','+fname[0]+','+clink[0]+','+conperson[0]+','+email[0]+','+tel[0]+'\n'
            else: 
                row=internationalStudies[0]+','+ip+','+url+','+fname[0]+',https://www.mrt.ac.lk'+clink[0]+','+conperson[0]+','+email[0]+','+tel[0]+'\n'
                csv.write(row)
 
    if ip == 'Postgraduate Studies':
        
        
        url = 'https://www.mrt.ac.lk/web/contacts-postgraduate-studies'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        courseinfo = tree.xpath('//table/tbody/tr')
        

        for c in courseinfo:
            fname=c.xpath('./td[1]//text()')
            clink=c.xpath('./td[1]//@href')
            conperson=c.xpath('./td[2]//text()')
            email=c.xpath('./td[3]//text()')
            tel=c.xpath('./td[4]//text()')
            
            if str(clink[0]).startswith("http"):
                row=internationalStudies[0]+','+ip+','+url+','+fname[0]+','+clink[0]+','+conperson[0]+','+email[0]+','+tel[0]+'\n'
            else: 
                row=internationalStudies[0]+','+ip+','+url+','+fname[0]+',https://www.mrt.ac.lk'+clink[0]+','+conperson[0]+','+email[0]+','+tel[0]+'\n'

            csv.write(row)
csv.close()    
