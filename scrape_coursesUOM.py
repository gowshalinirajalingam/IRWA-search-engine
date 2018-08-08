from lxml import html
import requests
from urllib.request import Request, urlopen

import concurrent.futures
urls = ['https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=0', 
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=1',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=2',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=3',
        'https://www.mrt.ac.lk/web/courses?field_course_tags_target_id&page=4']
     
f=open('coursesUOM.txt','w') 

for url in urls:
   page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
   tree = html.fromstring(page.content)
   prodname = tree.xpath(' //*[@id="block-scholarly-content"]/div/div/div/div/div/div/span/a/text()')
   print(prodname)
   for p in prodname:
     f.write("%s\n" % p)
     
f.close()