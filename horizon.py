# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:44:32 2018

@author: pavit
"""

from lxml import html
import requests
from urllib.request import Request, urlopen
import itertools
import csv


#programs in UOM
homeurl = 'http://horizoncampus.edu.lk/'

#write in a csv11 file
download_dir = "C:\\Users\\Shashini\\Desktop\\Horizon1.csv" #where you want the file to be downloaded to

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "Faculty Name,Faculty Link,Type,Program Name ,Program Url\n"
csv.write(columnTitleRow)


page = requests.get(homeurl, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)

#
Faculty = hometree.xpath('//*[@id="menu-item-2928"]//a/span/text()')
FacultyLink = hometree.xpath('//*[@id="menu-item-2928"]//a/@href')
print(Faculty )
print(FacultyLink)
for fn in Faculty:
    type="Undergraduate"
    if fn =='Faculty of Management':
        url = 'http://horizoncampus.edu.lk/faculty-of-management/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="eluidf710f971"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/text()')
        Programlinks=tree.xpath('//*[@id="eluidf710f971"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/@href')
        print(Programlinks)
        for p,pl in itertools.zip_longest(Programs,Programlinks):
            row=Faculty[1]+","+url+","+str(type)+","+str(p)+","+"http://horizoncampus.edu.lk/faculty-of-management/"+str(pl)+"\n"
            csv.write(row)        
            print(row)
                    
                    
    if fn =='Faculty of Information Technology':
        url = 'http://horizoncampus.edu.lk/faculty-of-information-technology/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="eluidf5da513f"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/text()')
        Programlinks=tree.xpath('//*[@id="eluidf5da513f"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/@href')
        print(Programlinks)
        for p,pl in itertools.zip_longest(Programs,Programlinks):
            row=Faculty[4]+","+url+","+str(type)+","+str(p)+","+"http://horizoncampus.edu.lk/faculty-of-information-technology/"+str(pl)+"\n"
            csv.write(row)        
            print(row)
                   
    if fn =='Faculty of Science':
        url = 'http://horizoncampus.edu.lk/faculty-of-science/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="eluid39d01a7d"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/text()')
        Programlinks=tree.xpath('//*[@id="eluid39d01a7d"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/@href')
        print(Programlinks)
        for p,pl in itertools.zip_longest(Programs,Programlinks):
            row=Faculty[8]+","+url+","+str(type)+","+str(p)+","+"http://horizoncampus.edu.lk/faculty-of-science/"+str(pl)+"\n"
            csv.write(row)        
            print(row)
            
    
                    
    if fn =='Faculty of Education':
        url = 'http://horizoncampus.edu.lk/faculty-of-education/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="eluidd371f97f"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/text()')
        Programlinks=tree.xpath('//*[@id="eluidd371f97f"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/@href')
        print(Programlinks)
        for p,pl in itertools.zip_longest(Programs,Programlinks):
            row=Faculty[12]+","+url+","+str(type)+","+str(p)+","+"http://horizoncampus.edu.lk/faculty-of-education/"+str(pl)+"\n"
            csv.write(row)        
            print(row)
            
    
                    
    if fn =='Faculty of International Programs':
        url = 'http://horizoncampus.edu.lk/faculty-of-international-programs/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="eluide1881df2"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/text()')
        Programlinks=tree.xpath('//*[@id="eluide1881df2"]/div/div/div/div/div[2]/div[2]/ul/li/span/a/@href')
        print(Programlinks)
        for p,pl in itertools.zip_longest(Programs,Programlinks):
            row=Faculty[18]+","+url+","+str(type)+","+str(p)+","+"http://horizoncampus.edu.lk/faculty-of-international-programs/"+str(pl)+"\n"
            csv.write(row)        
            print(row)
            
################################### course tab#########################
         
Course = hometree.xpath('//*[@id="menu-item-2929"]//a/span/text()')
CourseLink = hometree.xpath('//*[@id="menu-item-2929"]//a/@href')
print("avsgwvqgadic")
print(Course )
print(CourseLink) 

for fn in Course:
    
    if fn =='CERTIFICATE & DIPLOMA':
        
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="menu-item-2855"]//a/span/text()')
        Programlinks=tree.xpath('//*[@id="menu-item-2855"]//a/@href')
        print("abcd")
        print(Programs)
        print(Programlinks)
        for pg in Programs:
            if pg == 'Diploma in Biotechnology – (Nilai)':
                fac ='Faculty of Science'
                url ='http://horizoncampus.edu.lk/faculty-of-science/'
                type="Diploma"
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row) 
                    print("qwer")
                    print(row)           
                
            if pg == 'Certificate of Higher Education in Common Law':
                fac ='Faculty of Education'
                url ='http://horizoncampus.edu.lk/faculty-of-education/'
                type="Certificate"
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)
                
            if pg == 'Diploma in Pre School Education':
                fac ='Faculty of Education'
                url ='http://horizoncampus.edu.lk/faculty-of-education/'
                type="Diploma"
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)
               
    if fn =='GOVERNMENT INTEREST FREE LOAN SCHEME':
        
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="menu-item-2854"]//a/span/text()')
        Programlinks=tree.xpath('//*[@id="menu-item-2854"]//a/@href')
        type="Undergraduate"
        print(Programs)
        print(Programlinks)
        for pg in Programs:
            if pg == 'BSc (Hons) in Information Technology':
                fac ='Faculty of Information Technology'
                url ='http://horizoncampus.edu.lk/faculty-of-information-technology/'
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)           
                
            if pg == 'BIT (Hons) in Networking & Mobile Computing':
                fac ='Faculty of Information Technology'
                url ='http://horizoncampus.edu.lk/faculty-of-information-technology/'
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)
                
            if pg == 'Bachelor of Management (Hons) in Marketing':
                fac ='Faculty of Management'
                url ='http://horizoncampus.edu.lk/faculty-of-management/'
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)
                
            if pg == 'BSc in Business Management (HRM)':
                fac ='Faculty of Management'
                url ='http://horizoncampus.edu.lk/faculty-of-management/'
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)           
                
            if pg == 'Bachelor of Education (Hons)':
                fac ='Faculty of Education'
                url ='http://horizoncampus.edu.lk/faculty-of-education/'
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)
                
            if pg == 'Bachelor of Education in English (Hons)':
                fac ='Faculty of Education'
                url ='http://horizoncampus.edu.lk/faculty-of-education/'
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)
                
            if pg == 'Bachelor of Education in Physical Science (Hons)':
                fac ='Faculty of Education'
                url ='http://horizoncampus.edu.lk/faculty-of-education/'
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)
                
            if pg == 'Bachelor of Education in Biological Science (Hons)':
                fac ='Faculty of Science'
                url ='http://horizoncampus.edu.lk/faculty-of-science/'
                for p,pl in itertools.zip_longest(Programs,Programlinks):
                    row=fac+","+url+","+str(type)+","+str(p)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)
               
    if fn =='POSTGRADUATE PROGRAMS':
        print("postttttttttttttttttttttttttttttttt")
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Programs = tree.xpath('//*[@id="menu-item-2857"]//a/span/text()')
        Programlinks=tree.xpath('//*[@id="menu-item-2857"]//a/@href')
        type="Postgraduate"
        print(Programs)
        print(Programlinks)
        for pg in Programs:
                if pg == 'Master of Business Administration':
                    fac ='Faculty of Management'
                    url ='http://horizoncampus.edu.lk/faculty-of-management/'
                    #for p in :
                    row=fac+","+url+","+str(type)+","+str(Programs)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row)               
                    
                if pg == 'Food Safety, Animal Plant Hygiene':
                    fac ='Faculty of Science'
                    url ='http://horizoncampus.edu.lk/faculty-of-science/'
                    row=fac+","+url+","+str(type)+","+str(Programs)+","+str(pl)+"\n"
                    csv.write(row)        
                    print(row) 
                            
                        

    
    
csv.close()
