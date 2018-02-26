# import libraries
import urllib2
from bs4 import BeautifulSoup
from scrapper.helper import *

# query the website and return the html to the variable
page = urllib2.urlopen(CONST_URL)

# parse the html using beautiful soup and store in variable
soup = BeautifulSoup(page, CONST_HTML_PARSER)

# job_classifiers : For storing all the job classifiers
# final_dict : Dictionary to store the final (to be displayed) output.
job_classifiers = []
final_dict = {}

# Get all job classifiers from the table at the top
# Planned to use this list to match the text initially but went ahead with RegEx matching approach
for subclass in soup.find_all(CONST_H3, text=CONST_HEADER_TEXT):
    # Get the tag that follows the h3 Tag
    table_tag = next_tag(subclass)
    # Get the list of job classifiers
    job_classifiers = get_titles(table_tag)

# Get the Div Tag containing description of all the job classifiers
div_tags = soup.find_all(CONST_DIV, id=CONST_DIV_TAG_ID)

for div_tag in div_tags:
    # Get all span in the div tag
    tdTags = div_tag.find_all(CONST_SPAN)
    for table_tag in tdTags:
        span_text = table_tag.get_text()
        # Match the Span text with the Reg Ex defined in helper methods
        if text_matches(span_text):
            pair = span_text.split(" ", 1)
            # Append to dictionary
            final_dict[pair[0]] = pair[1]

# Print the contents of the dictionary
print "WA_RISK_CODE_MAP = "
for key in final_dict:
    print key, final_dict[key]
