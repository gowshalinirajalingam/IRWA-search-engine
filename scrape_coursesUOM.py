

#writing cources in UOM
from lxml import html
import requests
from urllib.request import Request, urlopen

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
#printing the elements in the list 
   for c in coursename:
     f.write("%s\n" % c)
     

################################################################################


urls = ['https://www.mrt.ac.lk/web/']
     
f.write("\nprograms in university of moratuwa\n")
f.write("-----------------------------------\n")


page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
tree = html.fromstring(page.content)

Academic = tree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[1]/strong/a/text()')
AcademicProgram = tree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[1]/ul/li/a/text()')
print(Academic)
for ac in Academic:
  f.write("%s\n" % ac)
print(AcademicProgram)
for ap in AcademicProgram:
  f.write("\t%s\n" % ap)


internationalStudies = tree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[2]/strong/a/text()')
internationalprogram = tree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[2]/ul/li/a/text()')
print(internationalStudies)
for ist in internationalStudies:
  f.write("%s\n" % ist)
  print(internationalprogram)
for ip in internationalprogram:
  f.write("\t%s\n" % ip)

underGrad = tree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[1]/strong/a/text()')
underGradprog = tree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[1]/ul/li/a/text()')
print(underGrad)
for ug in underGrad:
  f.write("%s\n" % ug)
print(underGradprog)
for up in underGradprog:
  f.write("\t%s\n" % up)

postGrad = tree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[1]/strong/a/text()')
postGradprog = tree.xpath(' //*[@id="block-menuforeducation2"]/div/div/ul/li[1]/ul/li/a/text()')
print(postGrad)
for pg in postGrad:
  f.write("%s\n" % pg)
print(postGradprog)
for pp in postGradprog:
  f.write("\t%s\n" % pp)



#closing the text file
f.close()
