import json
import requests
import os
import sys
from flask import jsonify
from app import *
#from mercury_parser import *

#import feedparser
"""
import json
  
basepath = os.path.dirname(__file__)
static_folderpath = os.path.abspath(os.path.join(basepath, "..", "static"))
params = {
	    'api_key': 'Rec3FsQTp1OMimcWPgDWfhTeCUQZ3LZxYR0DPjPr',
	  }
response = requests.get(
	      'https://mercury.postlight.com/parser?url=https://trackchanges.postlight.com/building-awesome-cms-f034344d8ed',
		  params=params)
#data = json.loads(response)
"""
from mercury_parser import ParserAPI


basepath = os.path.dirname(__file__)
static_folderpath = os.path.abspath(os.path.join(basepath, "..", "static"))
mercury = ParserAPI(api_key='Rec3FsQTp1OMimcWPgDWfhTeCUQZ3LZxYR0DPjPr')
p = mercury.parse('https://www.huffingtonpost.com/entry/donald-trump-wiretapping-reaction_us_5aeb42b9e4b0c4f193201a43')
'''
# Available attributes:
print (p.content)

p.content
p.date_published
p.lead_image_url
p.dek
p.url
p.domain
p.excerpt
p.word_count
p.direction
p.total_pages
p.rendered_pages
p.next_page_url
'''
if __name__=="__main__":
    with open(static_folderpath+'/options.txt', 'w') as outfile:
        outfile.write(p.content)
            #json.dump(response, outfile, indent=4, sort_keys=True)

	