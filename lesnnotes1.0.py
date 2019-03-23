from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os, sys
import json
from tkinter import *

#this part here exist to check if the user has data.json file available
#from that file user name and password will be used

def doesFileExists(data):
    return os.path.exists(data)
  
#if data.json exists, it goes on and performs the rest of the script
#using the info from data.json
if doesFileExists('data.json'):
    pass
    
#if it doesn;t exist it starts this GUI part
#in which a user will input vaules for this dictionary    
else:
    window = Tk()

    def create():
        data = {  
            'user': e1_val.get(),
            'pass': e2_val.get()
        }

        with open('data.json', 'w') as outfile:  
            json.dump(data, outfile)
        def quit1():
            window.destroy()
        quit1()
        
    l1 = Label(window, text="Username")
    l1.grid(padx=15,pady=10,ipady=3) 
    e1_val = StringVar()    

    e1 = Entry(window, width="50", textvariable= e1_val)
    e1.grid(row=0, column = 2)
    l3 = Label(window)
    l3.grid(row = 0, column = 3) 
    l3 = Label(window)
    l3.grid(row = 0, column = 4) 

    l2 = Label(window, text="Password")
    l2.grid(row = 1, column = 0) 
    e2_val = StringVar()


    e2 = Entry(window,  width="50", textvariable= e2_val)
    e2.grid(row=1, column = 2)

    b1 = Button(window, text = "Be BIBO!", command = create, width = '10', height='3')  
    b1.grid(row=3, column=2, rowspan=3)     
    l4 = Label(window)
    l4.grid(row = 5, column = 0) 
        
        
    window.mainloop()

with open('data.json', 'r') as read_file:
    data = json.load(read_file)

user = list(data.values())[0]  
pas = list(data.values())[1]

options = Options()
options.headless = True

if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe",)
    y = webdriver.Chrome(chromedriver_path, options=options)
else:
    y = webdriver.Chrome(options=options)

#y = webdriver.Chrome(options=options)
#y = webdriver.Chrome()
#standradne poruke za cas, ovo se treba menjati sa porukama u skajpu
no = 'No new sentences'
bye = "Thank you for a nice lesson :)\n It was great seeing you today :) \nI hope to see you soon :)\nHave a nice evening :)\nAll the best :)\n Bye bye (wave)"
d = 'No new words'

url2 = 'https://tutor.engoo.com/schedules/day/3382'

xpath=y.find_element_by_xpath

y.get(url2)
y.implicitly_wait(30)
#input username
y.find_element_by_class_name('css-cgadzw').click()
y.find_element_by_class_name('css-cgadzw').send_keys(user)
#input sifre
y.find_element_by_id('label-1').click()
y.find_element_by_id('label-1').send_keys(pas)
#submit za login
y.implicitly_wait(30)
y.find_element_by_xpath("//button[@type='submit']//div[contains(text(),'Sign In')]").click()
y.implicitly_wait(30)
#pocetna strana
y.find_element_by_id("schedule-today").click()
y.implicitly_wait(30)
#trenutni cas!!
y.find_element_by_link_text('DOING').click()
y.implicitly_wait(30)
time.sleep(2)
xpath("//div[@class='lesson']//a[@type='button'][1]").click()
y.implicitly_wait(30)
time.sleep(5)
xpath("//div[contains(text(),'Notes')]").click()
time.sleep(5)
y.implicitly_wait(30)
#this part scrapes the text, i wanted to use beautiful soup and requests
#however this is all in javascript, and bs couldn't scrape it.
tekst = xpath("//textarea[@class='css-jyrqiu']")
lesn = tekst.text
y.implicitly_wait(30)
y.back()
y.implicitly_wait(30)
alert = y.switch_to_alert()
alert.accept()

y.find_element_by_id('LessonNoteSentence').send_keys(lesn)

#bye bye poruka

y.find_element_by_id('LessonNoteTeacherMessage').send_keys(bye)
y.implicitly_wait(30)

#recenice
#y.find_element_by_id('LessonNoteSentence').send_keys(no)
#dugmence koje otvara polja za reci

y.find_element_by_id('addWordBox').click()
y.find_element_by_id('addWordBox').click()

#prva rec

y.find_element_by_xpath("//div[@id='word_list']/input[@type='text'][1]").send_keys(no)

#druga rec, obrati paznju da moze da se indeksuje, ali ne krece od nule, nego od 1, i zavisi koliko puta je kliknuto.
y.find_element_by_xpath("//div[@id='word_list']/input[@type='text'][2]").send_keys(d)
#teacher note message
y.find_element_by_id("teachers-lesson-memo-textarea").send_keys('\nIntermediate, daily news\n')
#lesson submit dugme
y.find_element_by_id("lesson_note_submit").click()

y.quit()

