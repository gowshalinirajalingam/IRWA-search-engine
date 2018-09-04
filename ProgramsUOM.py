#programs in UOM
homeurl = 'https://www.mrt.ac.lk/web/'

#write in a csv file
download_dir = "C:\\Users\\Gowshalini\\Desktop\\Academic Programs in UOM.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "program Catagory,program Type,program type link,Degree Name,degree url\n"
csv.write(columnTitleRow)


page = requests.get(homeurl, headers={'User-Agent': 'Mozilla/5.0'})
hometree = html.fromstring(page.content)

#Academic
AcademicProgram = hometree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[1]/ul/li/a/text()')
AcademicProgramlink = hometree.xpath(' //*[@id="block-menuforeducation1"]/div/div/ul/li[1]/ul/li/a/@href')

for ap in AcademicProgram:
    if ap=='Undergraduate Degrees':
        url = 'https://www.mrt.ac.lk/web/education/degrees/undergraduate'
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        undergraduatedegrees = tree.xpath(' //*[@id="block-scholarly-content"]/div/article/div/div/div/table/tbody/tr/td/a/span/text()')
        ugdegreelinks=tree.xpath('//*[@id="block-scholarly-content"]/div/article/div/div/div/table/tbody/tr/td/a/@href')
        for ud,ul in itertools.zip_longest(undergraduatedegrees,ugdegreelinks):
          print(ul)
          if not str(ul).startswith("http"):
              row="Acadamic,Undergraduate,"+"https://www.mrt.ac.lk"+AcademicProgramlink[0]+","+ud+","+"https://www.mrt.ac.lk"+ul+"\n"
              csv.write(row)
          else: 
              row="Acadamic,Undergraduate,"+"https://www.mrt.ac.lk"+AcademicProgramlink[0]+","+ud+","+ul+"\n"
              csv.write(row)

    if ap=='Postgraduate Degrees':
        url="https://www.mrt.ac.lk/web/postgraduate-degrees"
        page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        tree = html.fromstring(page.content)
        postgraduate=tree.xpath('//*[contains(text(),"Degree of")]')
        for pg in postgraduate:
          pgcourse= pg.xpath('.//text()')
          pglink=pg.xpath('.//@href')
          
          if len(pglink)==1 and not str(pglink).startswith('http') :
              row="Acadamic,Postgraduate Degree,"+"https://www.mrt.ac.lk"+AcademicProgramlink[1]+","+pgcourse[0]+","+"https://www.mrt.ac.lk"+pglink[0]+"\n"
              csv.write(row)
          elif len(pglink)==1 and not str(pglink).startswith('http'): 
              row="Acadamic,Postgraduate Degree,"+"https://www.mrt.ac.lk"+AcademicProgramlink[1]+","+pgcourse[0]+","+pglink[0]+"\n"
              csv.write(row)
          else:
              row="Acadamic,Postgraduate Degree,"+"https://www.mrt.ac.lk"+AcademicProgramlink[1]+","+pgcourse[0]+",  \n"
              csv.write(row)
              
#    if ap=='Postgraduate Diplomas':
#         #Details are in uom_postgraduatediploma.csv file  
csv.close()
