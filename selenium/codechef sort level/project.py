from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pytest

# WEBDRIVER INTIALISATION
# op = webdriver.ChromeOptions()
# op.add_argument('headless')
# driver = webdriver.Chrome(options=op)
driver = webdriver.Chrome('./chromedriver')
# URL TO MAIN WEBSITE
url="https://www.codechef.com/{}/"

# BEGINNER SECTION
driver.get(url.format("problems/school"))
problem=driver.find_elements_by_xpath("//a[@title='Submit a solution to this problem.']")
school_level=[]
for i in range(len(problem)):
    school_level.append(problem[i].text)

# EASY SECTION
driver.get(url.format("problems/easy"))
problem=driver.find_elements_by_xpath("//a[@title='Submit a solution to this problem.']")
easy=[]
for i in range(len(problem)):
    easy.append(problem[i].text)

# Medium section    
driver.get(url.format("problems/medium"))
problem=driver.find_elements_by_xpath("//a[@title='Submit a solution to this problem.']")
medium=[]
for i in range(len(problem)):
    medium.append(problem[i].text)


# time.sleep(2)
# USER PROBLEMS
url="https://www.codechef.com/{}"
driver.get(url.format("users/neel0086"))
user = driver.find_elements_by_css_selector('[rel="nofollow"]')
user_problem=set()
for i in range(len(user)):
    user_problem.add(user[i].text)

# INTERSECTION
x=[value for value in school_level if value in user_problem]
y=[value for value in easy if value in user_problem]
z=[value for value in medium if value in user_problem]

# PANDA DATAFRAME
x=pd.DataFrame({'Beginner':x})
y=pd.DataFrame({'Easy':y})
z=pd.DataFrame({'Medium':z})
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
table=pd.concat([x,y,z],axis=1)
table=table.fillna(" ")
print(table)
