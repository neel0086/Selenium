from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
import pandas as pd


# WEBDRIVER INTIALISATION
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(options=op)
# driver = webdriver.Chrome('./chromedriver')
# URL TO MAIN WEBSITE
url="https://www.codechef.com/{}/"

x,y,z=[],[],[]
# USER PROBLEMS
name=input("Enter the user name-->")
driver.get(url.format("users/"+name))
user = driver.find_elements_by_css_selector('[rel="nofollow"]')
user_problem=set()
for i in range(len(user)):
    user_problem.add(user[i].text)

# BEGINNER SECTION
driver.get(url.format("problems/school"))
problem=driver.find_elements_by_xpath("//a[@title='Submit a solution to this problem.']")
school_level=[]
for i in problem:
    school_level.append(i.text)
    if i.text in user_problem:
        x.append(i.text)

# EASY SECTION
driver.get(url.format("problems/easy"))
problem=driver.find_elements_by_xpath("//a[@title='Submit a solution to this problem.']")
easy=[]
for i in problem:
    easy.append(i.text)
    if i.text in user_problem:
        y.append(i.text)

# Medium section    
driver.get(url.format("problems/medium"))
problem=driver.find_elements_by_xpath("//a[@title='Submit a solution to this problem.']")
medium=[]
for i in problem:
    medium.append(i.text)
    if i.text in user_problem:
        z.append(i.text)


# time.sleep(2)
# PANDA DATAFRAME
x=[value for value in school_level if value in user_problem]
y=[value for value in easy if value in user_problem]
z=[value for value in medium if value in user_problem]
x=pd.DataFrame({'Beginner':x})
y=pd.DataFrame({'Easy':y})
z=pd.DataFrame({'Medium':z})
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
table=pd.concat([x,y,z],axis=1)
table=table.fillna(" ")
print(table)
