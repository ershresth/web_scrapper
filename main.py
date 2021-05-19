CodeWithHarry
Home
Videos
Blog
Contact Me
Search

Course Content
 1. Learn JavaScript In One Video In Hindi (2018)
Free YouTube Video
 2. Learn Python In Hindi In One Video - हिंदी में (Latest Tutorial)
Free YouTube Video
 3. Learn Php In One Video In Hindi - हिंदी में (Latest PHP Tutorial 2018)
Free YouTube Video
 4. 15 Minute Python Tutorial For Beginners In Hindi (Full & Complete Crash Course)
Free YouTube Video
 5. Learn Bootstrap In Hindi In One Video - हिंदी में (Latest Tutorial 2019)
Free YouTube Video
 6. Learn HTML In One Video
Free YouTube Video
 7. Learn jQuery In Hindi In One Video - हिंदी में (Latest Tutorial 2018)
Free YouTube Video
 8. Create A Responsive Website Using HTML, CSS And Bootstrap 4 In Hindi
Free YouTube Video
 9. Login And Registration Form Using Php & MySQL [Php Login System In Hindi]
Free YouTube Video
 10. C Programming Tutorial For Beginners: Learn C In Hindi
Free YouTube Video
 11. JavaScript Registration Form Validation - हिंदी में (Latest Tutorial 2019)
Free YouTube Video
 12. CSS 3 Tutorial For Beginners: Learn CSS In One Video In Hindi
Free YouTube Video
 13. C++ Tutorial For Beginners: Learn C Plus Plus In Hindi
Free YouTube Video
 14. Learn Python Programming For Free | Python Programming Tutorial In Hindi
Free YouTube Video
 15. Java tutorial in hindi
Free YouTube Video
 16. Android Development Tutorial in Hindi
Free YouTube Video
 17. Web Scraping Tutorial using Python and BeautifulSoup
Free YouTube Video
 18. Git & GitHub Tutorial For Beginners In Hindi - हिंदी में (2019)
Free YouTube Video
 19. Login And Registration Form Using Php & MySQL [Php Login System In Hindi]
Free YouTube Video
 20. Linux Tutorial For Beginners in Hindi
Free YouTube Video
 21. Numpy Tutorial in Hindi
Free YouTube Video
 22. Php Tutorial for Beginners in Hindi with MySQL Project
Free YouTube Video
 23. Learn JavaScript In One Video In Hindi (2020)
Free YouTube Video
 24. C Language Tutorial For Beginners (With Notes)
Free YouTube Video
 25. How To Make a WordPress Website | Wordpress Tutorial for Beginners | Elementor Tutorial In Hindi
Free YouTube Video
 26. Python Tutorial For Beginners In Hindi (With Notes)
Free YouTube Video
 27. Python Programming Course in Hindi (Advanced)
Free YouTube Video
 28. Android Application Development Tutorial in Hindi With Notes
Free YouTube Video
 29. React Tutorial in Hindi
Free YouTube Video
 30. HTML Tutorial For Beginners In Hindi (With Notes)
Free YouTube Video
 31. CSS Tutorial In Hindi (With Notes)
Free YouTube Video
Overview
Q&A
Files
Announcements
Web Scraping Tutorial using Python and BeautifulSoup
Introduction:
In this blog we will learn web scrapping from start to end. We will cover topics like:

How does a website works in the backend?
What is web scrapping?
Installing modules:
Why use modules?
How to install modules?
Requests
Getting data(HTML)
BeautifulSoup (bs4)
Parsing Data
HTML Tree Traversal (Targeting Data)
Our First Code(Getting title)
find()
find_all()
Getting class of an element
Finding elements through class name
Finding elements through element ID
Getting text from tags(text/get_text())
Getting all the links
Taking HTML from a variable instead of requests
Contents
Children, parent, next_sibling and previous_siblings
Difference between children and contents
stripped_strings
exit()
Writing data in CSV file
Tip
How does a website works in the backend?
Step 1: User requests a page. Eg:- www.google.com

Step 2: On whichever server the data is, that server sends you back a raw html file.





Step 3: Web browser converts the html file into a readable webpage(the one that you are seeing right now).

What is web scrapping?
The technique of taking the html file sent by the server into python and scrapping it instead of giving it to the browser and displaying it is called Web scrapping.

Two ways of getting data from a website:

Using API
HTML web scrapping using some tool like bs4
Installing modules:
Why use modules?
In order to use the power of python to scrap websites, we don’t have to write new code for everything. We can use existing code written by experts. Why take the hard path when the outcome is same, when you can do it easily in some lines of code in very short period of time?

How to install modules?
Modules are very easy to install. Open command prompt and just write these three lines one by one:

pip install requests
pip install html5lib
pip install bs4
and you are good to go! If you get any error you can watch this video:

https://www.codewithharry.com/videos/general-python-errors-1

Requests:
Getting data(HTML):
In order to work with the HTML, we will have to get the HTML as a string. We can easily get HTML data by using get() function in requests module. We first need to import this module by writing:

import requests
Then we can make a variable or directly write the link in get() function as a string:

url = "https://codewithharry.com"
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	# r returns response so if we want the code we write r.content
print(htmlContent)		# printing the code


Instead of “content” we can also use “text”:

htmlTexr = r.text
print(htmlText)


r.text is the response in Unicode and r.content is the response in bytes.

BeautifulSoup (bs4):
Beautiful Soup is the perfect module to parse or transverse through HTML code. We can easily target any div, table, td, tr, class, id, etc. The basic template(boilerplate code) which is used everytime is:

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify())	# to print html in tree structure
Parsing Data:
Once the HTML is fetched using requests the next step will be to parse the HTML content. For that we will use python’s BeautifulSoup module which will create a tree like structure for our DOM. This line is parsing the data:

soup = BeautifulSoup(htmlContent, 'html.parser')
We have given two arguments to BeautifulSoup function. One is our HTML content another is our parser. We can also save an HTML file instead of getting data everytime, take that HTML file’s data in a variable and in the same way just write the variable in the function, both are same things. In second argument we are giving it a parser. Here we are using html.parser, we can also use lxml. The parsed data is saved in our soup variable. That is our soup, a mixture of everything. All the data we want is there, we just have to target it and get it. Simple, right?

HTML Tree Traversal (Targeting Data):
From here the main thing starts, from here we start playing with the data. HTML Tree traversal is travelling through the tree branches(HTML tags) and to target the branches we want and scrapping them. Just for excitement wanna see something? Copy and run this code:

import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
for i in soup.find_all("code"):
    print(i.text)
    # We can also do it like this
    # print(i.get_text())
Yes! It scrapped all the codes on this page! See how powerful scrapping is, how much it can help you and how much time it can save! I hope you are all powered up, let’s start scrapping!

Our first code:
If we want to scrap title of the page(which is shown in the tab button) then we can get it by:

title = soup.title
print(title)
There is a title tag in all HTML pages, for this page it is:

<title>Web Scraping Tutorial using Python and BeautifulSoup in Hindi - Code With Harry</title>
So with soup.title we can directly get the title of the page. soup.title is like saying soup>title, going inside soup and getting title. In windows like we go into folders like that soup/title. If say there is code:

<div>
    <div>
        <code>
            This is file.
        </code>
    </div>
</div>
We can get data of code tag by simply writing “soup.div.div.code”. It’s like giving path of a file through folders where every tag is a folder and whatever is in code tag is the file.

find():
It is used to get first element in the HTML page. It could be any element. For eg:

print(soup.find('p')) 
This line will get you first p tag of the page. If we want all paragraphs(all p tags) of the page then we can use find_all() function.

find_all():
This line will get you all p tags of the page:

paras = soup.find_all('p')
print(paras)
Whatever tag you want to scrap, write that tag in the function as argument. Also when we print paras variable,  it will print it like a list. If we want every item one by one, we just put it through a for loop and iterate it, like this:

for i in paras:
    print(i)
gcae fecn feid gtgt gatl cont cpnp dbcc sdss

Getting class of an element:
Earlier we were getting text from the tag, this time we are getting class of the element. To get class of an element we need to write:

# print(soup.find('p')['class'])
Here we are using find() function to get p tag like before but we added [‘class’] in it. It’s like list slicing, tag has a class variable, we are getting that variable’s value. If we want other variables like id, style, role, type, we can get them all.

Finding elements through class name:
Most of the times we don’t want to find by tag name because it isn’t that accurate so we use class name there. Code to find elements by class name:

# print(soup.find_all("p", class_="lead"))
We can also avoid writing tag name if you are not sure about tag name. You can simply write like:

# print(soup.find_all(class_="code-toolbar"))
Finding elements through element ID:
Sometimes some elements are not given classes or we just want to target the element with id. We can do it like this:-

# print(soup.find(id='qna'))
There is no find_all() function for id because id can be given to only one element.

Getting text from tags(text/get_text()):
When we write soup.find(‘element’) it returns the whole tag like this:

<title>Web Scraping Tutorial using Python and BeautifulSoup in Hindi - Code With Harry</title>
But if we write:

soup.find(‘element’).text
# OR
soup.find(‘element’).get_text()
It will return:

Web Scraping Tutorial using Python and BeautifulSoup in Hindi - Code With Harry
Getting all the links:
With the information I have mentioned till now, you can do it yourself. You can try it. But if unable to do then keep reading. If we want all the links from a webpage then we have to use find_all() function. The tag for links is anchor tag. So, code would be:

anchors = soup.find_all('a')
This will get all the anchor tags but anchor tags have text in them. Links are in href and href is a variable written in the tag. What did I tell you about getting variables from tags? Slicing! It can be done like this:

for i in paras:
    print(i['href'])
I also told you that we need to iterate find_all() that’s why for loop. It can also be done like:

for i in paras:
    print(i.get('href'))
Taking HTML from a variable instead of requests:
Bs4 just needs the HTML. It doesn't matter where it came from. We can also make a variable, write HTML in that and give it to bs4. It can be done like this:

html = '''
<body>
    <ul>
        <li>This</li>
        <li><a>This</a>This</li>
        <li>This</li>
        <li>This</li>
        <li id="li">This</li>
        <li>    This    </li>
    </ul>
</body>
'''
soup = BeautifulSoup(html, 'html.parser')
We made a multi-line string and put it in the html variable then we gave that to beautifulsoup. For convenience in the rest of the codes shown below we will use this HTML instead of getting it through requests.

Contents:
If we want to go one step deeper in the tree then we use contents. Eg:-

If this is the HTML code:

<ul>
    <li>This</li>
    <li><a>This</a>This</li>
    <li>This</li>
    <li>This</li>
    <li>This</li>
</ul>
and we have targeted ul tag but we want to go inside ul then we can simply write:

ul = soup.find("ul")
print(ul.contents)
It will return a list which we can iterate.

Children, parent, next_sibling and previous_siblings:
You can see HTML tree like a family tree. In a family tree there are parents, children, siblings, exactly like that in HTML tree we have children, parent and siblings. You can understand it like children means one step inside the tree, parent means one step outside the tree and siblings mean in the same step, other elements. Here is a simple code to understand it better:

<body>
    <ul>
        <li>This</li>
        <li><a>This</a>This</li>
        <li>This</li>
        <li>This</li>
        <li>This</li>
    </ul>
</body>
Here body is parent to ul and ul is parent to li. li is children to ul and ul is children to body. All li tags are each others siblings, easy way to understand is their parent(ul) is same so siblings. Code for all three is:

1. Children:
ul = soup.find("ul")
for i in ul.children:
	print(i)
With for loop we are iterating ul.children. For more info read ‘Difference between Children and Contents’

2. Parent:
ul = soup.find("ul")
print(ul.parent)
You just have to write “.parent”, to get parent of parent, write:

print(ul.parent.parent)
Simple!

3. next_sibling and previous_siblings:
Like parent we can go to next sibling and then next sibling like this:

ul = soup.find(id="li")
print(ul.next_sibling.next_sibling)
We can also get all siblings by next_siblings() function. This functions gives a generator because of which we have to iterate it, which means code would be like:

ul = soup.find(id="li")

for j in ul.next_siblings:
    print(j)
There is also a function named previous_siblings() to get previous siblings. Code is like this:

for i in ul.previous_siblings:
    print(i)
Like next_sibling, we can also use previous_sibling() function and code is similar like earlier:

print(ul.previous_sibling.previous_sibling)
Difference between Children and Contents:
Children and content are no different. The only difference is content returns a list but children gives a generator. If we print contents we can just see the list but if we print children we see:

<list_iterator object at 0x000002532ABDF190>
This is an object which is iterable so if we want to get values from it then we just have to iterate it by using a for loop. But why generator? When to use contents and when to use children? Contents simply takes whatever is there and store it in memory but generator doesn’t store it, it only processes when we ask for the value and it processes on the fly because of which there is no storage happening which helps when we have to scrap big data. If we scrap big data with contents, it will store everything and fill up our memory because of which code may crash. So at that time we can use children. This was a brief explanation on generator if you want to know in detail you can check out this blog!

stripped_strings:
stripped_strings does the same thing which in-built strip() function does. It takes away all the spaces. For eg:-

ul = soup.find(id="li")
elem = ul.next_sibling.next_sibling
print(elem)
for i in elem.stripped_strings:
    print(i)
We have only one element in ul but even then we are using for loop because stripped_strings gives a generator. Output:

<li>    This    </li>
This
See it took away all the spaces.

exit():
exit() function is used to exit a program. It is helpful while finding errors or when we want to see code in pieces. If you have written a code of say 100 lines and on 71st line you have written exit() then it will not compile rest of the 29 lines, it will exit right there.

Writing data in CSV:
CSV is a comma separated file which makes writing data very easy. There are two ways of writing data in CSV. Both ways are as follows:

In this we will open a file and close it. We don’t have to create the file, it will automatically create it.
f = open("file.csv", "w")
f.write("Every,word,will,go,in,separate,column\n")
f.write("This,will,go,in,next,row")
f.close()​
In this we will open a file but we don’t have to close it, it will be handled automatically. File will also be automatically created.
with open("file.csv", "w") as f:
    f.write("Every,word,will,go,in,separate,column\n")
    f.write("This,will,go,in,next,row")
We open the file, in arguments gave it a name with file format. Second argument, i.e. “w” means write format. There are different formats for different things like “r” for reading.
write() function helps us to write in file. Whatever we want to write, we pass through write() function.
Close() function is very important, until your file is not closed, your no data is saved. After closing the file, the file is made. So closing it is very important. In 2nd method it’s automatic so we don’t have to worry.
Tip: If you need to hit and try your code and you don't want to run your program again and again because of request.get() or any reason, you can use this tip. This tip helped me alot.

Open your terminal and write:

python -i filename.py    # write file name with format(.py)
This command will not let the program end. You can keep writing code in the terminal and it will play that code right there.

Code as described/written in the video
# If you want to scrape a website:
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal
# 
# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# # 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))


# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)

# print(anchors)

# Get first element in the HTML page
# print(soup.find('p') ) 

# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# find all the elements with class lead
# print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        # print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
# for elem in navbarSupportedContent.contents:
#     print(elem)
 
# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents: 
#     print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# elem = soup.select('.modal-footer')
# print(elem)
elem = soup.select('#loginModal')[0] 
print(elem)

Copyright © 2020-2021 CodeWithHarry.com
