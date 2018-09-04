#writing cources in UOM
from lxml import html
import requests
from urllib.request import Request, urlopen
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





#international studies
internationalStudies = hometree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[2]/strong/a/text()')
internationalprogram = hometree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[2]/ul/li/a/text()')
print(internationalStudies)
for ist in internationalStudies:
  f.write("%s\n" % ist)

print(internationalprogram)
for ip in internationalprogram:
    f.write("\t%s\n" % ip)
    if ip == 'Undergraduate Studies':
        url = 'https://www.mrt.ac.lk/web/contacts-undergraduate-studies'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        undergraduatesTUDIES = tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/table/tbody/tr/td[1]/a/text()')
        print(undergraduatesTUDIES)
        for us in undergraduatesTUDIES:
          f.write("\t\t%s\n" % us)  
    if ip == 'Postgraduate Studies':
        url = 'https://www.mrt.ac.lk/web/contacts-postgraduate-studies'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        postgraduatestudies = tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/table/tbody/tr/td[1]/a/text()')
        print(postgraduatestudies)
        for pg in postgraduatestudies:
          f.write("\t\t%s\n" % pg)  


#undergraduate studies
underGrad = hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[1]/strong/a/text()')
underGradprog = hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[1]/ul/li/a/text()')
print(underGrad)
for ug in underGrad:
  f.write("%s\n" % ug)

print(underGradprog)
for up in underGradprog:
  f.write("\t%s\n" % up)
  if up=='Faculty of Information Technology':
       url = 'https://www.mrt.ac.lk/web/itfac/education/undergraduate'
       page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
       tree = html.fromstring(page.content)
       itfacugp = tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/ul/li/a/text()')
       itfacugplinks = tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/ul/li/a/@href')
       print(itfacugp)
       for ifa,ifal in itertools.zip_longest(itfacugp,itfacugplinks):
         f.write("\t\t"+ifa+"\t"+ifal+"\n")  
  if up=='Faculty of Business':    
       url = 'https://www.mrt.ac.lk/web/business'
       page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
       tree = html.fromstring(page.content)
       fab = tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/ul/li/u/a/text()')
       fablinks=tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/ul/li/u/a/@href')
       print(fab)
       print(fablinks)
       for fabb,fabl in itertools.zip_longest(fab,fablinks):
           f.write("\t\t"+fabb+"\t"+fabl+"\n")   
           
#postgraduate studies
postGrad = hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[2]/strong/a/text()')
postGradlink=hometree.xpath('//*[@id="block-menuforeducation2"]/div/div/ul/li[2]/ul/li[1]/a/@href')
postGradprog = hometree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[2]/ul/li/a/text()')
print(postGrad)
for pg,pl in itertools.zip_longest(postGrad,postGradlink):
  f.write(pg+"\t"+pl+"\n")

print(postGradprog)
for pp in postGradprog:
  f.write("\t%s" % pp)
  if pp=='Faculty of Engineering':
       f.write("\n")
  if pp=='Faculty of Information Technology':
       url = '  https://www.mrt.ac.lk/web/itfac/education/postgraduate' 
       page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
       tree = html.fromstring(page.content)
       pgp = tree.xpath('///*[@id="block-scholarly-content"]/div/article/div/div/div/ul/li/a/text()')
       pgpl=tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/ul/li/a/@href')
       print(pgp)
       print(pgpl)
       f.write("\n")
       for pgp,pgpl in itertools.zip_longest(pgp,pgpl):
           f.write("\t\t"+pgp+"\t"+pgpl+"\n")   
  if pp=='Faculty of Architecture':
       pgarchlink=hometree.xpath('//*[@id="block-menuforeducation2"]/div/div/ul/li[2]/ul/li[3]/a/@href')
       print(pgarchlink)
       for pgal in pgarchlink:
           f.write("\t\t"+pgal+"\n")   



######################################################################

#FACULTIES
url = 'https://www.mrt.ac.lk/web/'
     
f.write("\nFaculties in university of moratuwa\n")
f.write("-----------------------------------\n")

page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
tree = html.fromstring(page.content)
  
faculty = tree.xpath(' //*[@id="block-toplinks"]/div/ul/li[1]/span/text()')
facultynames = tree.xpath('//*[@id="block-toplinks"]/div/ul/li[1]/ul/li/a/text()')
facultylinks = tree.xpath('//*[@id="block-toplinks"]/div/ul/li[1]/ul/li/a/@href')
print(faculty)
for fa in faculty:
  f.write("%s\n" % fa)
print(facultynames)
print(facultylinks)
for fn,fl in  itertools.zip_longest(facultynames,facultylinks):
  f.write("\t"+fn+"\t"+fl+"\n")
##########################################################################

        
#closing the text file
f.close()



dic = {"John": "john@example.com", "Mary": "mary@example.com"} #dictionary


