import bs4
import re
from scrapper.constants.constants import *

# Find next tag for the provided tag
def next_tag(tag):
    tag = tag.next_sibling
    while not isinstance(tag, bs4.Tag):
        tag = tag.next_sibling
    return tag

# Helper method to match a given text to Reg Ex : 999 ABC or 999-000 ABC
def text_matches(text):
    pattern = re.compile("^\d+\s+")
    pattern2 = re.compile("^\d+-\d+\s+")
    return pattern.match(text) or pattern2.match(text)

# Get all the titles into a list
def get_titles(tag):
    classifiers_list = []
    if tag.name == CONST_TABLE:
        rows = tag.find(CONST_TBODY).find_all(CONST_TR)
        for row in rows:
            cells = row.find_all(CONST_TD)
            if (len(cells) > 0):
                innner_divs = cells[0].find_all(CONST_DIV)
                if len(innner_divs) > 0:
                    links = innner_divs[0].find_all(CONST_A)
                    if len(links) > 0:
                        a_text = links[0].get_text()
                        text_arr = a_text.split('-')
                        classifiers_list.append(text_arr[2])
    return classifiers_list
