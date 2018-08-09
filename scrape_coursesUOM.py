

#writing cources in UOM
from lxml import html
import requests
from urllib.request import Request, urlopen
import itertools
#urls of multiplepages
urls = ['https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=0', 
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=1',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=2',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=3',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=4']
#opening the text file     
f=open('UOM.txt','w') 
#writing in test file 
f.write("Courses in university of moratuwa\n")
f.write("-----------------------------------\n")

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
       f.write(cn+"\t"+cl+"\n")
    
################################################################################


#programs in UOM
homeurl = 'https://www.mrt.ac.lk/web/'
     
f.write("\nprograms in university of moratuwa\n")
f.write("-----------------------------------\n")


page = requests.get(homeurl, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)

#Academic
Academic = hometree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[1]/strong/a/text()')
AcademicProgram = hometree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[1]/ul/li/a/text()')
print(Academic)
for ac in Academic:
  f.write("%s\n" % ac)

print(AcademicProgram)
for ap in AcademicProgram:
    f.write("\t%s\n" % ap)
    if ap=='Undergraduate Degrees':
        url = 'https://www.mrt.ac.lk/web/education/degrees/undergraduate'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        undergraduatedegrees = tree.xpath(' //*[@id="block-scholarly-content"]/div/article/div/div/div/table/tbody/tr/td/a/span/text()')
        ugdegreelinks=tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/table/tbody/tr/td/a/@href')
        print(undergraduatedegrees)
        print (ugdegreelinks)
        for ud,ul in itertools.zip_longest(undergraduatedegrees,ugdegreelinks):
          f.write("\t\t"+ud+"\t"+ul+"\n")
#    if ap=='Postgraduate Degrees':
#         #Details are in uom_postgraduate_degree.csv file
#    if ap=='Postgraduate Diplomas':
#         #Details are in uom_postgraduatediploma.csv file  
#    


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
