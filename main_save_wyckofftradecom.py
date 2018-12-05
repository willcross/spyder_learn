# main function to save wyckofftrade.com tutorial htmls
from function_nav2pageurl import *
from function_page2url import *
from function_url2docx import *
import time
pageurls = nav2pageurl(r'https://wyckofftrade.com/blog/category/tutorial')


for i in pageurls:
    urls,filenames = page2url(i)
    for j in urls:
        index = urls.index(j)
        url2docx(j,filenames[index])
        time.sleep(5)