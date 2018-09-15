# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 22:03:08 2018

@author: Shashini
"""

from lxml import html
import requests
import itertools
import csv


urls = ['https://www.sjp.ac.lk/courses/undergraduate-courses/']
urls1 =['http://graduate.sjp.ac.lk/course/']
urls2 =['http://external.sjp.ac.lk/degrees/']

download_dir2 = "C:\\Users\\Shashini\\Desktop\\UniJapura Done.csv" #where you want the file to be downloaded to 

csv2 = open(download_dir2, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "Faculty Name,url,type,dName, ,dUrl \n"
csv2.write(columnTitleRow)

for url in urls:
#fetches datafrom banded urls also
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    #mapping the web page content to xml tree 
    tree = html.fromstring(page.content)
    FacultyName = tree.xpath('//*[@id="content"]/div/div[1]/div[3]//h2/text()')
    print(FacultyName)
   
  
      
   
#printing the elements in the list 
    for fn in FacultyName:
        
        type ="Undergraduate"
        if fn == 'Faculty of Huminities & Social Sciences' :
            
            url = 'https://www.sjp.ac.lk/courses/undergraduate-courses/#art'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/p[5]/text()')
            
            for p in itertools.zip_longest(degName):
                print(p)
                row = FacultyName[1]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
                

        if fn == 'Faculty of Management Studies & Commerce' :
            
            url = 'https://www.sjp.ac.lk/courses/undergraduate-courses/#mgt'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/p[8]/text()')
            
            for p in itertools.zip_longest(degName):
                print(p)
                row = FacultyName[2]+","+url+","+str(type)+","+str(p)+","+url+"\n"
            
                print(row)
                csv2.write(row)
          
        if fn == 'Faculty of Applied Sciences' :
            
            url = 'https://www.sjp.ac.lk/courses/undergraduate-courses/#applied'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/table/tbody/tr/td[3]/text()')
           
            for p in itertools.zip_longest(degName):
                print(p)
                row = FacultyName[3]+","+url+","+str(type)+","+str(p)+","+url+"\n"
            
                print(row)
                csv2.write(row)
            
        if fn == 'Faculty of Medical Sciences' :
            
            url = 'https://www.sjp.ac.lk/courses/undergraduate-courses/#med'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/p[13]/text()')
            for p in itertools.zip_longest(degName):
                print(p)
            
                row = FacultyName[4]+","+url+","+str(type)+","+str(p)+","+url+"\n"
            
                print(row)
                csv2.write(row)
                    
        if fn == 'Faculty of Technology' :
            
            url = 'https://www.sjp.ac.lk/courses/undergraduate-courses/#tech'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('///*[@id="content"]/div/div[1]/div[3]/p[15]/text()')
            for p in itertools.zip_longest(degName):
                print(p)
                row = FacultyName[5]+","+url+","+str(type)+","+str(p)+","+url+"\n"
            
                print(row)
                csv2.write(row)
            
        if fn == 'Faculty of Engineering' :
            
            url = 'https://www.sjp.ac.lk/courses/undergraduate-courses/#eng'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/div/text()')
            for p in itertools.zip_longest(degName):
                print(p)
            
                row = FacultyName[6]+","+url+","+str(type)+","+str(p)+","+url+"\n"
            
                print(row)
                csv2.write(row)
                
########PostGraduate ##########
    
for url in urls1:
    
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    #mapping the web page content to xml tree 
    tree = html.fromstring(page.content)
    FacultyName = tree.xpath('//*[@id="content"]/div/div[1]/div[3]/div[1]/div/div/div/div/div[2]/div/div/div/a/text()')
    print(FacultyName)
    
    for fn in FacultyName:
        
        type ="Postgraduate"
        if fn == ' Humanities' :
            
            url = 'http://graduate.sjp.ac.lk/humanities/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/p[1]/strong/text()')
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[0]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
        """
         ############################################################      
        if fn == ' Social Sciences' :
            
            url = 'http://graduate.sjp.ac.lk/social-sciences/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath(' ')
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[1]+","+url+","+str(type)+","+"MA/ M.Sc. in Social Science"+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
        ################################################################ 
        
        """
        if fn == ' Life Sciences' :
            
            url = 'http://graduate.sjp.ac.lk/life-sciences/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            print("fff")
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div/ul/li/a/strong/text()')
            print("bbb")
            degUrl= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/div[1]/div/div/div/div/ul/li/a/@href')
            print(degName)
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[1]+","+url+","+str(type)+","+str(p)+","+str(degUrl)+"\n"
                print(row)
                csv2.write(row)
                
        if fn == ' Physical Sciences' :
            
            url = 'http://graduate.sjp.ac.lk/physical-sciences/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            print("fff")
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/div/table/tbody/tr/td[3]/text()')
            print("bbb")
            
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[2]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
                
        if fn == ' Management Studies & Commerce' :
            
            url = 'http://graduate.sjp.ac.lk/management-and-commerce/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            print("fff")
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/ul/li/a/text()')
        
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[3]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
                
                
        if fn == ' Medical Sciences' :
            
            url = 'http://graduate.sjp.ac.lk/medical-sciences/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            print("fff")
            degName= tree.xpath('//*[@id="content"]/div/div[1]/div[3]/h3/text()')
        
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[4]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
               
########External Degrees#################
for url in urls2:
    
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    #mapping the web page content to xml tree 
    tree = html.fromstring(page.content)
    FacultyName = tree.xpath('//*[@id="wpv-view-layout-2941-TCPID11"]/div/div/div/a/div/div[2]/h5/text()')
    print(FacultyName)
    
    for fn in FacultyName:
        
        type ="External"
        if fn == 'Humanities and Social Sciences' :
            
            url = 'http://external.sjp.ac.lk/degree/bachelor-of-humanities-and-social-sciences-general-external-degree/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[1]/div/div/div/h2/text()')
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[0]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
                
        if fn == 'Business Administration' :
            
            url = 'http://external.sjp.ac.lk/degree/bachelor-of-science-business-administration-general-external-degree-programme/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[1]/div/div/div/h2/text()')
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[1]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
                
        if fn == 'Bachelor of Commerce' :
            
            url = 'http://external.sjp.ac.lk/degree/bachelor-of-commerce-general-external-degree/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[1]/div/div/div/h2/text()')
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[2]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
                
        if fn == 'Management (Public)' :
            
            url = 'http://external.sjp.ac.lk/degree/bachelor-of-science-management-public-general-external-degree/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[1]/div/div/div/h2/text()')
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[3]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
                
        if fn == 'Environment and  Development  Studies' :
            
            url = 'http://external.sjp.ac.lk/degree/bachelor-of-social-sciences-general-external-degree-in-environment-and-development-studies/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[1]/div/div/div/h2/text()')
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[4]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
                
        if fn == 'Bachelor Of Arts In English' :
            
            url = 'http://external.sjp.ac.lk/degree/bachelor-of-arts-general-external-degree-in-english/'
            page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            tree = html.fromstring(page.content)
            
            degName= tree.xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[1]/div/div/div/h2/text()')
            
            for p in itertools.zip_longest(degName):
                print("haaai")
                print(p)
                row = FacultyName[5]+","+url+","+str(type)+","+str(p)+","+url+"\n"
                print(row)
                csv2.write(row)
        
        
        
                
       
      

csv2.close()
