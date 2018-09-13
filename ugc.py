# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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



homeurl = 'http://ugc.ac.lk/'

#write in a csv file
download_dir = "C:\\Users\\YNS(Nera)\\Desktop\\ugc.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "Prgram,Unversity,unversity url\n"
csv.write(columnTitleRow)


page = requests.get(homeurl, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)

#Academic//*[@id="block-menuforeducation1"]/div/div/ul/li[1]/ul/li[1]/


AcademicProgram = hometree.xpath('//*[@id="ugc-cssmenu"]/li[5]/ul/li/a/span/text()')
AcademicProgramlink = hometree.xpath('//*[@id="ugc-cssmenu"]/li[5]/ul/li/a/@href')
#print(AcademicProgram)
#print(AcademicProgramlink)
#menu25
for ap in AcademicProgram:
    if ap=='Universities':
        url = 'http://ugc.ac.lk/en/universities-and-institutes/universities.html'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        undergraduatedegrees = tree.xpath('//*[@id="ugc-current-content"]//span/a/text()')
        ugdegreelinks=tree.xpath('//*[@id="ugc-current-content"]//span/a/@href')
       # print(undergraduatedegrees)
        #print(ugdegreelinks)
        for ud,ul in itertools.zip_longest(undergraduatedegrees,ugdegreelinks):
              row=AcademicProgramlink[0]+","+str(ud)+","+str(ul)+"\n"
              csv.write(row)
              
              
    if ap=='Institutes':
        url="http://ugc.ac.lk/en/universities-and-institutes/institutes.html"
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        institute=tree.xpath('//*[@id="ugc-current-content"]//a/text()')
        institutelinks=tree.xpath('//*[@id="ugc-current-content"]//a/@href')
        #print(institute)
        #print(institutelinks)
        
        for ud,ul in itertools.zip_longest(institute,institutelinks):
              row=AcademicProgramlink[2]+","+str(ud)+","+str(ul)+"\n"
              csv.write(row)      
            
    
    if ap=='Degree Courses':
        url="http://ugc.ac.lk/en/universities-and-institutes/degree-courses/undergraduate-courses.html"
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        Undergraduate_Courses=tree.xpath('//*[@id="ugc-current-content"]//select/option/text()')
        print(Undergraduate_Courses)
        for ud in itertools.zip_longest(Undergraduate_Courses):
              row=AcademicProgramlink[3]+","+str(ud)+","+'http://ugc.ac.lk/en/universities-and-institutes/degree-courses/undergraduate-courses.html'+"\n"
              csv.write(row) 
        

    """          
    if ap=='Postgraduate Diplomas':
        url="https://www.mrt.ac.lk/web/postgraduate-diplomas"
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        postgraduatediploma=tree.xpath('//*[contains(text(),"Diploma")]')
        for pg in postgraduatediploma:
          pdcourse= pg.xpath('.//text()')
          pdlink=pg.xpath('.//@href')
          
          if len(pdlink)==1 and not str(pdlink).startswith('http') :
              row="Academic,Postgraduate Diploma,"+"https://www.mrt.ac.lk"+AcademicProgramlink[2]+","+pdcourse[0]+","+"https://www.mrt.ac.lk"+pdlink[0]+"\n"
              csv.write(row)
          elif len(pdlink)==1 and not str(pdlink).startswith('http'): 
              row="Academic,Postgraduate Diploma,"+"https://www.mrt.ac.lk"+AcademicProgramlink[2]+","+pdcourse[0]+","+pdlink[0]+"\n"
              csv.write(row)
          else:
              row="Academic,Postgraduate Diploma,"+"https://www.mrt.ac.lk"+AcademicProgramlink[2]+","+pdcourse[0]+",  \n"
              csv.write(row)"""
csv.close()# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

