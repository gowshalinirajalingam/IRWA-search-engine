# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 07:55:09 2018

@author: Shashini
"""

#################  UPCOMING COURSES (CERTIFICATE, DIPLOMA, UNDERGRADUATE, POSTGRADUATE) ################

from lxml import html
import requests
import itertools
import csv


#########################Certificate Courses in university of Colombo#####################

#urls of multiplepages CERTIFICATE
urls = ['https://cmb.ac.lk/index.php/u_course_cat/certificate-courses/page/1/', 
        'https://cmb.ac.lk/index.php/u_course_cat/certificate-courses/page/2/',
        'https://cmb.ac.lk/index.php/u_course_cat/certificate-courses/page/4/']


#write in a csv file
download_dir1 = "C:\\Users\\Shashini\\Desktop\\UOC\\UpcomingCourses.csv" #where you want the file to be downloaded to 

csv1 = open(download_dir1, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "Cource Name,Course Duration, Course Link\n"
csv1.write(columnTitleRow)
csv1.write("***Upcoming Certificate Courses***\n")




#looping through multiple pages DIPLOMA
for url in urls:
#fetches datafrom banded urls also
   page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#mapping the web page content to xml tree 
   tree = html.fromstring(page.content)
   coursename = tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[2]/a/text()')
   print(coursename)
   courseDuration = tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[3]/text()')
   print (courseDuration)
   courseLink =tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[2]/a/@href')
   print(courseLink)
#printing the elements in the list 
   for cn,cd,cl in itertools.zip_longest(coursename,courseDuration,courseLink):
        cn=str(cn).replace(",","\t") 
        cd= str(cd).replace(",","\t") 
        cl=str(cl)
        row=cn+","+cd+","+cl+"\n"
        csv1.write(row)
        
csv1.write("***Upcoming Diploma Courses***\n")

################DIPLOMA COURSES IN UNIVERSITY OF COLOMBO##########################
        
#urls of multiplepages
urls1 = ['https://cmb.ac.lk/index.php/u_course_cat/diploma-courses/page/1/', 
        'https://cmb.ac.lk/index.php/u_course_cat/diploma-courses/page/3/']


#looping through multiple pages
for url in urls1:
#fetches datafrom banded urls also
   page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#mapping the web page content to xml tree 
   tree = html.fromstring(page.content)
   coursename1 = tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[2]/a/text()')
   print(coursename1)
   courseDuration1 = tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[3]/text()')
   print (courseDuration1)
   courseLink1 =tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[2]/a/@href')
   print(courseLink1)
#printing the elements in the list 
   for cn1,cd1,cl1 in itertools.zip_longest(coursename1,courseDuration1,courseLink1):
        cn1=str(cn1).replace(",","\t") 
        cd1= str(cd1).replace(",","\t") 
        cl1=str(cl1)
        row1=cn1+","+cd1+","+cl1+"\n"
        csv1.write(row1)
        
csv1.write("***Upcoming Postgraduate Courses***\n")
        
############## POSTGRADUATE COURSES IN UOC#########################################
        
urls1 = ['https://cmb.ac.lk/index.php/u_course_cat/postgraduate-courses/page/1/', 
        'https://cmb.ac.lk/index.php/u_course_cat/postgraduate-courses/page/2/',
        'https://cmb.ac.lk/index.php/u_course_cat/postgraduate-courses/page/3/',
        'https://cmb.ac.lk/index.php/u_course_cat/postgraduate-courses/page/5/',
        'https://cmb.ac.lk/index.php/u_course_cat/postgraduate-courses/page/6/']


#looping through multiple pages
for url in urls1:
#fetches datafrom banded urls also
   page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#mapping the web page content to xml tree 
   tree = html.fromstring(page.content)
   coursename2 = tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[2]/a/text()')
   print(coursename2)
   courseDuration2 = tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[3]/text()')
   print (courseDuration2)
   courseLink2 =tree.xpath('//*[@id="content"]/div[2]/table/tbody/tr/td[2]/a/@href')
   print(courseLink2)
#printing the elements in the list 
   for cn2,cd2,cl2 in itertools.zip_longest(coursename1,courseDuration1,courseLink1):
        cn2=str(cn2).replace(",","\t") 
        cd2= str(cd2).replace(",","\t") 
        cl2=str(cl2)
        row2=cn2+","+cd2+","+cl2+"\n"
        csv1.write(row2)
        
        
csv1.close()