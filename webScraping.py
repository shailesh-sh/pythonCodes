from bs4 import BeautifulSoup
html_file=open("D://Django//csspractice.html","r")
page=html_file.read()
print(page)
soup=BeautifulSoup(page,"html.parser")
paragraph=soup.find_all('ol')
for p in paragraph:
    print(p.get_text())
