
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:41:19 2018

@author: pavit
"""

from lxml import html
import requests
from urllib.request import Request, urlopen
import itertools
import csv


homeurl = 'https://cmb.ac.lk/'

#write in a csv file
download_dir = "C:\\Users\\Shashini\\Desktop\\colombo1.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "Faculty,type,Program ,Program url\n"
csv.write(columnTitleRow)


page = requests.get(homeurl, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)

#Academic
AcademicProgram = hometree.xpath('//*[@id="nav-menu-item-8773"]/ul/li[2]/ul//text()')
AcademicProgramlink = hometree.xpath('//*[@id="nav-menu-item-8773"]/ul/li[2]/ul//@href')
#print(AcademicProgram)
#print(AcademicProgramlink)
for ap in AcademicProgram:
    """
    if ap=='Certificate Courses ':
        url = 'https://cmb.ac.lk/index.php/certificate-courses/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        faculty1 = tree.xpath('//*[@id="content"]/article/div/div/div/div/div/div/div/div/div/div/h2/text()')
        facultylinks=tree.xpath('//*[@id="content"]/article/div/div/div/div/div/div/div/div/div/div/figure/a/@href')
       # print(faculty1)
        #print(facultylinks)
        for f in faculty1:
            if f=='Arts':
                url1 = 'http://arts.cmb.ac.lk/index.php/certificate-diploma-courses/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="tablepress-4"]/tbody/tr/td[3]/a/text()')
                courselink=tree1.xpath('//*[@id="tablepress-4"]/tbody/tr/td[3]/a/@href')    
                for c,pl in itertools.zip_longest(course,courselink):
                    row=faculty1[0]+","+ap+","+str(c)+","+str(pl)+"\n"
                    csv.write(row)        
                   # print(row)
            if f=='Medicine':
                url1 = 'https://med.cmb.ac.lk/index.php/2012-05-16-05-19-54/external-and-extension-programs'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="middle-column"]/div/div[2]/ul/li/a/strong/text()')
                courselink=tree1.xpath('//*[@id="middle-column"]/div/div[2]/ul/li/a/@href')    
                for c,pl in itertools.zip_longest(course,courselink):
                    row=faculty1[1]+","+ap+","+str(c)+","+str(pl)+"\n"
                    csv.write(row)        
                   # print(row)
            if f=='Science':
                url1 = 'http://science.cmb.ac.lk/academic/other-courses/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="tablepress-27"]/tbody/tr/td[3]/a/text()')
                courselink=tree1.xpath('//*[@id="tablepress-27"]/tbody/tr/td[3]/a/@href')    
                for c,pl in itertools.zip_longest(course,courselink):
                    row=faculty1[2]+","+ap+","+str(c)+","+str(pl)+"\n"
                    csv.write(row)        
                   # print(row)
            if f=='IBMBB':
                url1 = 'http://www.ibmbb.cmb.ac.lk/?page_id=2939'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="content"]/article/div/div/div/div/div/h2[1]/text()')
                #courselink=tree1.xpath('//*[@id="tablepress-27"]/tbody/tr/td[3]/a/@href')    
                for c in itertools.zip_longest(course):
                    row=faculty1[3]+","+ap+","+str(c)+","+"http://www.ibmbb.cmb.ac.lk/?page_id=2939"+"\n"
                    csv.write(row)        
                   # print(row)
            if f=='IHRA':
                url1 = 'https://www.ihra.cmb.ac.lk/ihra-courses/#1475567208655-88905491-f812'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="1475567208655-88905491-f812"]/div[2]/div/div/ul/li/a/text()')
                courselink=tree1.xpath('//*[@id="1475567208655-88905491-f812"]/div[2]/div/div/ul/li/a/@href')    
                for c,cp in itertools.zip_longest(course,courselink):
                    row=faculty1[4]+","+ap+","+str(c)+","+str(cp)+"\n"
                    csv.write(row)        
                    #print(row)
            if f=='IIM':
                url1 = 'http://iim.cmb.ac.lk/index.php/category/courses/short-courses/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="content"]/div/div/div/div/div/div/h3/a/text()')
                courselink=tree1.xpath('//*[@id="content"]/div/div/div/div/div/div/h3/a/@href')    
                for c,cp in itertools.zip_longest(course,courselink):
                    row=faculty1[5]+","+ap+","+str(c)+","+str(cp)+"\n"
                    csv.write(row)        
                   # print(row)
            if f=='UCSC':
                url1 = 'http://ucsc.cmb.ac.lk/academic-programmes/training-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="general"]/div[2]/div/div/table/tbody/tr/td[2]/strong/a/text()')
                courselink=tree1.xpath('//*[@id="general"]/div[2]/div/div/table/tbody/tr/td[2]/a/@href')    
                for c,cp in itertools.zip_longest(course,courselink):
                    row=faculty1[6]+","+ap+","+str(c)+","+str(cp)+"\n"
                    csv.write(row)        
                   # print(row)
            if f=='NILIS':
                url1 = 'http://nilis.cmb.ac.lk/?page_id=123'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="content"]/article/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/th[1]/a/text()')
                courselink=tree1.xpath('//*[@id="content"]/article/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr/th[1]/a/@href')    
                for c,cp in itertools.zip_longest(course,courselink):
                    row=faculty1[7]+","+ap+","+str(c)+","+"http://www.ibmbb.cmb.ac.lk/?page_id=2939"+"\n"
                    csv.write(row)        
                   # print(row)

    
    """    
    if ap=='Postgraduate Programmes ':
        
        url = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        faculty1 = tree.xpath('//*[@id="body"]//h2/text()')
        #facultylinks=tree.xpath('//*[@id="1449033648245-98728bcf-a64d"]/div/div/div/div/div/div/div/ul/li/a/@href')
        print(faculty1)
        #print(facultylinks)
   
        for f in faculty1:
            
            if f=='Education':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
                print(course)
                
                courselink=tree1.xpath('//*[@id="1449033461680-86b435c7-af36"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1449033461680-86b435c7-af36"]//ul/li/a/text()')
                print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[1]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
            
            if f=='Graduate Studies':
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
               # print(course)
                for c in course:
                    if c=='Mphil / PhD Programmes':
                         courselink=tree1.xpath('//*[@id="1449042948678-c9dd64b9-e1b3"]//ul/li/a/@href') 
                        # print(courselink)
                         for pl in itertools.zip_longest(courselink):
                             row=faculty1[2]+","+ap+","+str(c)+","+str(pl)+"\n"
                             csv.write(row)        
                          #   print(row)
                    if c=='Master’s Degree Programmes':
                         courselink=tree1.xpath('//*[@id="1450261181322-a0dbc3d4-1482"]//ul/li/a/@href') 
                         #print(courselink)
                         for pl in itertools.zip_longest(courselink):
                             row=faculty1[2]+","+ap+","+str(c)+","+str(pl)+"\n"
                             csv.write(row)        
                          #   print(row)
                    if c=='Post Graduate Diploma Programmes':
                         courselink=tree1.xpath('//*[@id="1450261250192-4a284f58-1b3c"]//ul/li/a/@href') 
                         #print(courselink)
                         for pl in itertools.zip_longest(courselink):
                             row=faculty1[2]+","+ap+","+str(c)+","+str(pl)+"\n"
                             csv.write(row)        
                          #   print(row)
                    if c=='Executive Diploma Programmes':
                         courselink=tree1.xpath('//*[@id="1450261288583-f4484b44-718d"]//ul/li/a/@href') 
                         #print(courselink)
                         for pl in itertools.zip_longest(courselink):
                             row=faculty1[2]+","+ap+","+str(c)+","+str(pl)+"\n"
                             csv.write(row)        
                           #  print(row)
            
            if f=='Law':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
                #print(course)
                
                         
                courselink=tree1.xpath('//*[@id="1449034930497-55bf780b-6775"]//ul/li/a/@href') 
                courseName = tree1.xpath('//*[@id="1449034930497-55bf780b-6775"]//ul/li/a/text()')
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[3]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
            
            if f=='Management & Finance':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
                #print(course)
                
                         
                courselink=tree1.xpath('//*[@id="1449034295355-959e0556-1fa9"]//ul/li/a/@href') 
                courseName=tree1.xpath('//*[@id="1449034295355-959e0556-1fa9"]//ul/li/a/text()') 
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[4]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
            
            if f=='Medicine':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
                print(course)
                
                courselink=tree1.xpath('//*[@id="1449038625394-9c416e96-1317"]//ul/li/a/@href') 
                courseName=tree1.xpath('//*[@id="1449038625394-9c416e96-1317"]//ul/li/a/text()')
                print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[5]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
            
            
            if f=='Science':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
                print(course)
                
                courselink=tree1.xpath('//*[@id="1449038016053-8a951a9c-d096"]//ul/li/a/@href') 
                courseName=tree1.xpath('//*[@id="1449038016053-8a951a9c-d096"]//ul/li/a/text()')
                print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[6]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
            
            if f=='UCSC':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
                print(course)
                
                courselink=tree1.xpath('//*[@id="1449042571280-9b9e8e11-4240"]//ul/li/a/@href') 
                courseName=tree1.xpath('//*[@id="1449042571280-9b9e8e11-4240"]//ul/li/a/text()')
                print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[7]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
            
            
            if f=='PGIM':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
                print(course)
                
                courselink=tree1.xpath('//*[@id="1450261448328-963a4060-25a2"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1450261448328-963a4060-25a2"]//ul/li/a/text()') 
                print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[8]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
                     
            
            if f=='IHRA ':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                courselink=tree1.xpath('//*[@id="1517215752290-33de5826-1ac5"]//ul/li/a/@href') 
                courseName=tree1.xpath('//*[@id="1517215752290-33de5826-1ac5"]//ul/li/a/text()') 
                print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[9]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
                         
            
            if f=='CSHR':
                
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
                print("gvwqchbednxsjMKL,VFGHC DKXS,LABHFCDNJKXS,LAZFV BCDXSAKM,LHB CXMK,LZB CSDNXA,Z")
                print(course)
                
                courselink=tree1.xpath('//*[@id="1527506564313-fa2e5abe-e4a1"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1527506564313-fa2e5abe-e4a1"]//ul/li/a/text()')
                print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[10]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)
            
            
            if f=='Arts':
                url1 = 'https://cmb.ac.lk/index.php/postgraduate-programmes/'
                page1 = requests.get(url1, headers={'User-Agent': 'Mozilla/5.0'})
                tree1 = html.fromstring(page1.content)
                course = tree1.xpath('//*[@id="body"]//h4/a/span/text()')
               # print(course)
                
                courselink=tree1.xpath('//*[@id="1449033648245-98728bcf-a64d"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1449033648245-98728bcf-a64d"]//ul/li/a/text()')
                        # print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)        
                          #   print(row)      
                    
                courselink=tree1.xpath('//*[@id="1449032447632-13a43ae1-6873"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1449032447632-13a43ae1-6873"]//ul/li/a/text()')
                         #print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)        
                          #   print(row)          
                    
                courselink=tree1.xpath('//*[@id="1449032288427-d07abbc9-550b"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1449032288427-d07abbc9-550b"]//ul/li/a/text()') 
                         #print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)        
                          #   print(row)
                              
                courselink=tree1.xpath('//*[@id="1449032602715-795d1a10-64a4"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1449032602715-795d1a10-64a4"]//ul/li/a/text()')
                         #print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                   row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                   csv.write(row)        
                           #  print(row)
       
                courselink=tree1.xpath('//*[@id="1449032713052-fd1957cd-6cc0"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1449032713052-fd1957cd-6cc0"]//ul/li/a/text()')
                        # print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)        
                           #  print(row)
                    
                courselink=tree1.xpath('//*[@id="1449032713052-fd1957cd-6cc0"]//ul/li/a/@href') 
                courseName=tree1.xpath('//*[@id="1449032713052-fd1957cd-6cc0"]//ul/li/a/text()')
                         #print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)        
                           #  print(row)
                    
                courselink=tree1.xpath('//*[@id="1449032809892-85726a1a-229d"]//ul/li/a/@href') 
                courseName=tree1.xpath('//*[@id="1449032809892-85726a1a-229d"]//ul/li/a/text()') 
                        # print(courselink)
                for pl in itertools.zip_longest(courselink):
                    row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)        
                            # print(row)
                    
                courselink=tree1.xpath('//*[@id="1449032802820-e4efd31c-c543"]//ul/li/a/@href')
                courseName=tree1.xpath('//*[@id="1449032802820-e4efd31c-c543"]//ul/li/a/text()')
                        # print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)        
                            # print(row)
                    
                courselink=tree1.xpath('//*[@id="1449032794217-a76f04d1-ed71"]//ul/li/a/@href') 
                courseName=tree1.xpath('//*[@id="1449032794217-a76f04d1-ed71"]//ul/li/a/text()') 
                         #print(courselink)
                for pn,pl in itertools.zip_longest(courseName,courselink):
                    row=faculty1[0]+","+ap+","+str(pn)+","+str(pl)+"\n"
                    csv.write(row)        
                            # print(row)                  
                            
           
                 
csv.close()# -*- coding: utf-8 -*-




