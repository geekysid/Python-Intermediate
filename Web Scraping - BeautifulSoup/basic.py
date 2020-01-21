from bs4 import BeautifulSoup 
import lxml

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister one" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister two" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister three" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.get_text())    # returns all the text inside the soup
print(soup.title)     # returns the tag title
print(soup.title.name)    # returns name of the tag title
print(soup.title.text)    # returns text inside the tag title
print(soup.title.parent)  # returns parent tag of the tag title
print(soup.title.parent.parent.name)      # returns 2nd level parent tag of the tag title
print(soup.p.text)    # returns text of the 1st para title
print(soup.p['class'])  # returns class name of 1st paragraph tag
print(soup.find('p', class_='title'))     # returns 1st para with class as title

print()
para = soup.find('p')     # returns 1st para tag
print(para)   prints everything this inside 1st para
print(para.a)     # returns bold tag inside 1st para
print(para.text)    # returns only text inside the 1st paragraph tags
print(para.b.text)  # returns only text inside the 1st bold tag inside 1st paragraph tags
print(para.name)    # returns name of the 1st paragraph tags

anchors = soup.find_all('a')      # returns list of all the tanchor tag
for anchor in anchors:
    print(anchor)     # returns the entire anchor tag
    print(anchor.text)    # returns only the text part of anchor tag
    print(anchor['href'])     # returns value of href attribute of anchor tag. gives error if no attribute is found inside tag
    print(anchor.get('href'))     # returns value of href attribute of anchor tag. returns NONE if no attribute is found inside the tag
    print()

para = soup.find(class_='story')    # returns 1st tag with class as story
print(para)     # prints entire paragraph
print(para.a.text)  # prints just the text part
print(para.a.get('id'))     # prints balue of attribute id in tag 


print("TAG_NAME")
print(soup.p.name)  # returns name of the tag
print()

print("TAG_ATTRIBUTES")
print(soup.a['href'])   # returns value of attribute and error if attribute is not present
print(soup.a.get('href'))   # returns value of attribute and None if attribute is not present
print(soup.a.attrs)   # returns dictionary of attributes and its value
print()

soup.a['href'] = "htttp://google.com"   # changing value if the attribute
print(soup.a.attrs)

del soup.a['id']   # removes an attribute from a tag
print(soup.a.attrs)


soup.a['title'] = "This is a title"   # adds an attribute to a tag

print(soup.a.attrs)     # returns all attributs inside 1st anchor tag as a dictionary

print()
print("GOING DOWN THE TREE")
# print(soup.p.b)     # using tags name to go down
print(soup.body.contents)   # returns list of all tags inside body
for tag in soup.body.contents:
    print(tag)

for tag in soup.body.children:    # children returns iterator of the direct child of the tag
    print(tag)
print()
for descendant in soup.body.descendants:    # descendants returns an iterator of all the child/child of child elements
    print(descendant)
print()

print('GOING UP')
print(soup.b.parent)    # returns every thing inside the parent tag of the element
print()
print(soup.b.parent.parent)


print('GOING SIDEWAYS')
print(soup.a.next_sibling)    # returns the very next sibling tag at the same level of the element
print(soup.a.next_sibling.next_sibling)
print()
print(soup.a.previous_sibling)   # returns the just previous sibling tag at same level of the element. None if no such sibling tag is present.
print(soup.a.previous_sibling.previous_sibling)

for sibling in soup.a.next_siblings:   # returns iterator of all sibling tag with same level appearing after the element.
    print(sibling)

for sibling in soup.a.previous_siblings:    # returns iterator of all sibling tag with same level appearing before the element.
    print(sibling)

print()
print("BACK & FORTH")
print(soup.a.next_element)  # returns immidiate next element of the tag.
print(soup.a.next_element.next_element)  
print(soup.a.next_element.next_element.next_element)

print(soup.a.previous_element)  # returns immidiate previous element of the tag.
print(soup.a.previous_element.previous_element)

print(soup.a.next_elements)     # returns iterator of all th eelements appeariang after the tag.
for next_e in soup.a.next_elements:
    print(next_e)

print(soup.a.previous_elements)     # returns ietrator for all the elements appearing before the tag
for prev_e in soup.a.previous_elements:
    print(prev_e)

print()
print("FILTERS")
print("Search By Tag")
print(soup.find('a'))   # searching for 1st appearance of tag <a>
print(soup.find_all('a'))   # returns list of all appearnce of <a> tag
print(soup.find_all(['a', 'b']))   # searching for all appearance of tags inside the list
print(soup.find_all(True))      # retuns list of all tags
for tag in soup.find_all(True):
    print(tag.name)

print()
print("find_all(name, attrs, recursive, string, limit, **kwargs)")
print(soup.find_all('a', 'sister'))     # return list osf all anchor tag with class sister
print(soup.find_all('a', class_='sister'))     # also return list of all anchor tag with class sister
print()
print(soup.find_all(class_='sister'))     # also return list of all tags with class sister
print()
print(soup.find_all('a', id='link2'))   # return list of all anchr tag with id as link2
print()
print(soup.find_all(id='link2'))   # return list of all tags with id as link2
print()
print(soup.find_all(href='http://example.com/elsie'))   # return list of all tags with href as http://example.com/elsie
print()
print(soup.find_all('a', id='link2', class_='sister'))   # using multiple kwargs
print()
print(soup.find_all(class_='sister', limit=2))     # also return list of 1st 2 tags with class sister.
print()
print(soup.find_all(href=True))     # returns all tag which has href attribute
print()

print("Search By CSS")
print(soup.find_all(class_='sister'))   # returns list of tags with class 'sister'
print()
print(soup.find_all(class_='one'))   # returns list of tags with class 'one'
print()
print(soup.find_all(class_='sister one'))   # returns list of tags with class 'sister one'
print()
print(soup.find_all(class_='one sister'))   # returns list of tags with class 'one sister'
print()

print()

print("Search By find_parents")
a = soup.find('a')
print(a.find_parent('body').find_parent())


print()
print("CSS SELECT")
print(soup.select('body p'))    # returns list of all p tags inside body tag
print()
print(soup.select('body p a'))    # returns list of all p tags inside body tag
print()
print(soup.select('a:nth-of-type(1)'))    # returns list of all 1st anchor tags 
print()
print(soup.select('a:nth-of-type(2)'))    # returns list of all 2nd anchor tags 
print()
print(soup.select('p:nth-of-type(2)'))    # returns list of all 2nd p tags 
print()
print(soup.select('#link1'))    # returns list of all tag with id link1
print()
print(soup.select('#link2, .sister'))    # retunrs list of all tags with id as link2 or class as sister
print()
print(soup.select('#link2, #link1'))    # retunrs list of all tags with id as link2 or class as sister
print()
print(soup.select('a#link1, a.sister'))     # returns list of all anchor tags with id as link1 or with class as sister
print()
print(soup.select('#link1 ~ .sister'))      # returns list of all next sibling tags wit id = link1 and sibling tag have class = sister
print()
print(soup.select('#link1 ~ #link3'))   # returns list of all sibling tags with id as link3 of the tag with id link1
print()
print(soup.select('a[href]'))  # returns all anchor tag with attribute href
print()
print(soup.select('a[href^="http://"]'))
print()
print(soup.select('a[href*="lac"]'))
print()
print(soup.select('a[href$="elsie"], .two'))
print()
print(soup.select_one('a'))