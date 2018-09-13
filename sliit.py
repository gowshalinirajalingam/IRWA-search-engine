# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 09:35:23 2018

@author: pavit
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:08:14 2018

@author: pavit
"""

from lxml import html
import requests
from urllib.request import Request, urlopen
import itertools
import csv



homeurl = 'https://www.sliit.lk/'

#write in a csv file
download_dir = "C:\\Users\\pavit\\Desktop\\ir_project\\sliit.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "Faculty,type,Program ,Program url\n"
csv.write(columnTitleRow)


page = requests.get(homeurl, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)

#Academic//*[@id="block-menuforeducation1"]/div/div/ul/li[1]/ul/li[1]/


Faculty = hometree.xpath('//*[@id="menu-item-2692"]/ul/li/a/span/text()')
FacultyLink = hometree.xpath('//*[@id="menu-item-2692"]/ul/li/a/@href')
print(Faculty )
print(FacultyLink)
#menu25//*[@id="menu-item-3192"]/ul
for fn in Faculty :
    if fn =='Business':
        url = 'https://www.sliit.lk/business/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="menu-item-3242"]/ul/li/a/span/text()')
        Programlinks=tree.xpath('//*[@id="menu-item-3242"]/ul/li/a//@href')
        for p,pl in itertools.zip_longest(Programs,Programlinks):
            row=Faculty[2]+", undegraduate ,"+str(p)+","+str(pl)+"\n"
            csv.write(row)        
            print(row)
    
    if fn =='Computing':
        url = 'https://www.sliit.lk/computing/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="menu-item-3192"]/ul/li/a/span/text()')
        Programlinks=tree.xpath('//*[@id="menu-item-3192"]/ul/li/a//@href')
        for p,pl in itertools.zip_longest(Programs,Programlinks):
            row=Faculty[0]+", undegraduate ,"+str(p)+","+str(pl)+"\n"
            csv.write(row)  
            print(row)
            
    if fn =='Engineering':
        url = 'https://www.sliit.lk/engineering/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="menu-item-3220"]/ul/li/a/span/text()')
        Programlinks=tree.xpath('//*[@id="menu-item-3220"]/ul/li/a//@href')
        #print(Programs)
        #print(Programlinks)
        for p,pl in itertools.zip_longest(Programs,Programlinks):
            row=Faculty[1]+", undegraduate ,"+str(p)+","+str(pl)+"\n"
            csv.write(row)  
            print(row)

    if fn =='Humanities & Sciences':
        url = 'https://www.sliit.lk/humanities-sciences/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programtype = tree.xpath('//*[@id="menu-item-3304"]/ul/li/a/span/text()')
        Programtypelinks=tree.xpath('//*[@id="menu-item-3304"]/ul/li/a//@href')
        #print(Programtype)
        for pn in Programtype :
            if pn =='Certificate Courses':
                url1 = 'https://www.sliit.lk/humanities-sciences/programmes/certificate-course/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                Programs = tree1.xpath( '//*[contains(text(),"Certificate in")]')
                prglink = tree.xpath('//*[@id="eluid95398cd7"]//a/@href')
                print(prglink)#//*[@id="eluid95398cd7"]/div/div/div/a
                for cp in Programs:
                    Ccourse= cp.xpath('.//text()')
                    row=Faculty[3]+", Certificate ,"+str(Ccourse)+",\n"
                    csv.write(row)  
                    print(row)
                   
            if pn =='Diploma Courses':
                url1 = 'https://www.sliit.lk/humanities-sciences/programmes/diploma-courses/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                Programs = tree1.xpath( '//*[contains(text(),"Diploma in")]')
                for dp in Programs:
                    Dcourse= dp.xpath('.//text()')
                    row=Faculty[3]+", Diploma ,"+str(Dcourse)+",\n"
                    csv.write(row)  
                    print(row)   
       
            if pn =='Undergraduate Degree Programmes':
                url1 = 'https://www.sliit.lk/humanities-sciences/programmes/undergraduate-degree-programs/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                Programs = tree1.xpath( '//*[contains(text(),"B.Ed (Hons) in")]')
                for dp in Programs:
                    Dcourse= dp.xpath('.//text()')
                    row=Faculty[3]+", UnderGraduate ,"+str(Dcourse)+",\n"
                    csv.write(row)  
                    print(row) 
                
            if pn =='Post Graduate Degree Programmes':
                url1 = 'https://www.sliit.lk/humanities-sciences/programmes/post-graduate-degree-programs/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                Programs = tree1.xpath( '//*[contains(text(),"in Education")]')
                for dp in Programs:
                    Dcourse= dp.xpath('.//text()')
                    row=Faculty[3]+", Post Graduate ,"+str(Dcourse)+",\n"
                    csv.write(row)  
                    print(row) 
    
    if fn =='Graduate Studies & Research':
        url = 'https://www.sliit.lk/graduate-studies-research/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programtype = tree.xpath('//*[@id="menu-item-3269"]/ul/li/a/span/text()')
        Programtypelinks=tree.xpath('//*[@id="menu-item-3269"]/ul/li/a//@href')
        print(Programtype)
        print(Programtypelinks)
        for pn in Programtype :
            if pn =='Masters Programmes':
                url1 = 'https://www.sliit.lk/graduate-studies-research/programms/masters-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                Programs1 = tree1.xpath( '//*[@id="eluidf5086ec1"]/div/div/div[1]/a/h3/span/text()')
                prglink = tree1.xpath( '//*[@id="eluidf5086ec1"]/div/div/div[1]/a/@href')
                row1=Faculty[4]+", Post Graduate ,"+str(Programs1)+","+str(prglink)+"\n"
                csv.write(row1)  
                print(row1)
                Programs2 = tree1.xpath( '//*[@id="eluidb8a41e47"]//h3/span/text()')
                prglink2 = tree1.xpath( '//*[@id="eluidb8a41e47"]/div/div/div[1]/a/@href')
                row2=Faculty[4]+", Post Graduate ,"+str(Programs2)+","+str(prglink2)+"\n"
                csv.write(row2)  
                print(row2)
                Programs3 = tree1.xpath( '//*[@id="eluiddc13ff8c"]//h3/span/text()')
                prglink3 = tree1.xpath( '//*[@id="eluiddc13ff8c"]/div/div/div[1]/a/@href')
                row3=Faculty[4]+", Post Graduate ,"+str(Programs3)+","+str(prglink3)+"\n"
                csv.write(row3)  
                print(row3)
                Programs4 = tree1.xpath( '//*[@id="eluidf5086ec1"]//h3/span/text()')
                prglink4 = tree1.xpath( '//*[@id="eluidf5086ec1"]/div/div/div[1]/a/@href')
                row4=Faculty[4]+", Post Graduate ,"+str(Programs4)+","+str(prglink4)+"\n"
                csv.write(row4)  
                print(row4)
                Programs5 = tree1.xpath( '//*[@id="eluidd81bd8f9"]//h3/span/text()')
                prglink5 = tree1.xpath( '//*[@id="eluidd81bd8f9"]/div/div/div[1]/a/@href')
                row5=Faculty[4]+", Post Graduate ,"+str(Programs5)+","+str(prglink5)+"\n"
                csv.write(row5)  
                print(row3)
                Programs6 = tree1.xpath( '//*[@id="eluid0a62a160"]//h3/span/text()')
                prglink6 = tree1.xpath( '//*[@id="eluid0a62a160"]/div/div/div[1]/a/@href')
                row6=Faculty[4]+", Post Graduate ,"+str(Programs6)+","+str(prglink6)+"\n"
                csv.write(row6)  
                print(row6)
            if pn =='MPhil Programmes':
                url1 = 'https://www.sliit.lk/graduate-studies-research/programms/mphil-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                Programs1 = tree1.xpath( '//*[@id="eluidc114ca7e"]/div/div/div[1]/a/h3/span/text()')
                prglink = tree1.xpath( '//*[@id="eluidc114ca7e"]/div/div/div[1]/a/@href')
                row1=Faculty[4]+", Post Graduate ,"+str(Programs1)+","+str(prglink)+"\n"
                csv.write(row1)  
                print(row1)                
            if pn =='PhD Programmes':
                url1 = 'https://www.sliit.lk/graduate-studies-research/programms/phd-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                Programs1 = tree1.xpath( '//*[@id="eluidf75c0cfa"]/div/div/div[1]/a/h3/span/text()')
                prglink = tree1.xpath( '//*[@id="eluidf75c0cfa"]/div/div/div[1]/a/@href')
                row1=Faculty[4]+", Post Graduate ,"+str(Programs1)+","+str(prglink)+"\n"
                csv.write(row1)  
                print(row1)
csv.close()# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

