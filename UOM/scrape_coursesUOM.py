#writing cources in UOM
from lxml import html
import requests
import itertools
import csv


#Courses in university of moratuwa

#urls of multiplepages
urls = ['https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=0', 
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=1',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=2',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=3',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=4']


#write in a csv file
download_dir = "C:\\Users\\Gowshalini\\Desktop\\courses in UOM.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "Cource Name,Course url\n"
csv.write(columnTitleRow)



#looping through multiple pages
for url in urls:
#fetches datafrom banded urls also
   page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
#mapping the web page content to xml tree 
   tree = html.fromstring(page.content)
   coursename = tree.xpath(' //*[@id="block-scholarly-content"]/div/div/div/div/div/div/span/a/text()')
   print(coursename)
   courselink = tree.xpath('//*[@id="block-scholarly-content"]/div/div/div/div[2]/div/div[1]/span/a/@href')
   print (courselink)
#printing the elements in the list 
   for cn,cl in itertools.zip_longest(coursename,courselink):
        cn=str(cn).replace(","," ")      # as csv is a coma delemeted if there is a comma in the text it is delemeting that text by the comma and storing in ceperate colums.so convering lxml.etree._ElementUnicodeResult type to string and replacing comma by " "
        row=cn+","+"https://www.mrt.ac.lk"+cl+"\n"
        csv.write(row)
csv.close()
################################################################################








