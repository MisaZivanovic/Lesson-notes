#libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os, sys


#standradne poruke za cas, ovo se treba menjati sa porukama u skajpu
#repetable messages that are sent to every student
no = 'No new sentences'
bye = "Thank you for a nice lesson :)\n It was great seeing you today :) \nI hope to see you soon :)\nHave a nice evening :)\nAll the best :)\n Bye bye (wave)"
d = '...'
#url
url2 = 'https://tutor.engoo.com/schedules/day/3382'
#a variable so that i don't have to type in the whole xpath
xpath=y.find_element_by_xpath
y.get(url2)
y.implicitly_wait(30)
#input username
y.find_element_by_class_name('css-cgadzw').click()
y.find_element_by_class_name('css-cgadzw').send_keys('')
#input password
y.find_element_by_id('label-1').click()
y.find_element_by_id('label-1').send_keys('')
#submit za login
#login button
y.find_element_by_class_name('css-bxqq9l').click()
y.implicitly_wait(30)
#pocetna strana
#first page
y.find_element_by_id("schedule-today").click()
y.implicitly_wait(30)
#trenutni cas!!
#searches for the ongoing class
y.find_element_by_link_text('DOING').click()
y.implicitly_wait(30)
time.sleep(2)
#y.find_element_by_xpath("//div[@class='sect01']//a[@type='button'][1]")
#finds the button that leads to an app, in which all the notes are typed in
xpath("//div[@class='lesson']//a[@type='button'][1]").click()
#css = 'div.container-fluid:nth-child(2) div.row-fluid:nth-child(1) div.span10 div.lesson:nth-child(3) div.sect01:nth-child(3) table.table.table-bordered.table-condensed:nth-child(3) tbody:nth-child(1) tr:nth-child(2) td:nth-child(1) > a.color.red.button'
#css2='a.color.red.button'
#y.find_element_by_css_selector(css).click()
xpath("//div[contains(text(),'Notes')]").click()
#it had to wait, because selenium was much faster than the app
time.sleep(2)
y.implicitly_wait(30)
#xpath("//textarea[@placeholder='Enter your notes here']").click()
xpath("//textarea[@class='css-jyrqiu']").click()
y.implicitly_wait(30)
time.sleep(2)
y.implicitly_wait(30)
#it selects the whole text inside this current form
xpath("//textarea[@class='css-jyrqiu']").send_keys(Keys.CONTROL, 'a')
y.implicitly_wait(30)
#copies that text
xpath("//textarea[@class='css-jyrqiu']").send_keys(Keys.CONTROL, 'c')
y.implicitly_wait(30)
y.back()
y.implicitly_wait(30)

#.send_keys(u'\ue007')#ovo je kod za enter dugme
#y.implicitly_wait(30)
#y.send_keys(u'\ue007')
#this thing here deals with javascript alert, becase it has to go back and paste
#the collected info into a form, on the previous page
alert = y.switch_to_alert()
alert.accept()

y.find_element_by_id('LessonNoteSentence').send_keys(Keys.CONTROL, 'v')
#bye bye message
#bye bye poruka
y.find_element_by_id('LessonNoteTeacherMessage').send_keys(bye)
y.implicitly_wait(30)
#recenice
#y.find_element_by_id('LessonNoteSentence').send_keys(no)
#dugmence koje otvara polja za reci
#there are hidden forms that have to be oppened by pressing buttons
y.find_element_by_id('addWordBox').click()
y.find_element_by_id('addWordBox').click()
#prva rec
y.find_element_by_xpath("//div[@id='word_list']/input[@type='text'][1]").send_keys(no)
#y.find_element_by_class_name('word_note').send_keys(no)
#y.find_element_by_class_name('word_note').send_keys(Keys.TAB, send_keys(d))
#indexing is the key here, but it starts from 1, not 0
#druga rec, obrati paznju da moze da se indeksuje, ali ne krece od nule, nego od 1, i zavisi koliko puta je kliknuto.
y.find_element_by_xpath("//div[@id='word_list']/input[@type='text'][2]").send_keys(d)
#teacher note message
y.find_element_by_id("teachers-lesson-memo-textarea").send_keys('\nIntermediate, daily news\n')
#lesson submit 
y.find_element_by_id("lesson_note_submit").click()
#closes the whole program
y.quit()

