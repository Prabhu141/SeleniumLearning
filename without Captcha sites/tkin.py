import tkinter as tk
import webbrowser
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import csv 

win = tk.Tk()

win.title("Maximized Window")

# Maximize the window
win.attributes("-alpha", True)
win.title("Python GUI App")

ttk.Label(win, text="Selenium Automation").pack()

# Define the dropdown options
options = [
    "|   |   |___Internet and Web Skills",
    "|   |   |___Web Skills",
    "|   |___Internet",
    "|   |___Developers and Publishers",
    "|   |___Hospitality",
    "|   |___Web Design and Development"

]

# Create the combobox widget
combobox = ttk.Combobox(win, values=options)
combobox.pack()



def open_website():
    Username = 0
    Email = 1
    URL = 2

    with open('data.csv', 'r') as csv_file:

        csv_reader = csv.reader(csv_file)

    #-------------------------------------------------------------------------------
    # Web Automation

        for line in csv_reader:


            driver = webdriver.Chrome()
            driver.get('https://www.angelsdirectory.com/submit.php')
            driver.maximize_window()
            time.sleep(5)

            username_field = driver.find_element("xpath", '/html/body/div[3]/div/div[1]/div/form/table/tbody/tr[4]/td[2]/input')
            username_field.send_keys(line[0])
            time.sleep(3)

            Email_field = driver.find_element("xpath", '/html/body/div[3]/div/div[1]/div/form/table/tbody/tr[5]/td[2]/input')
            Email_field.send_keys(line[1])
            time.sleep(3)

            URL_field = driver.find_element("xpath", '/html/body/div[3]/div/div[1]/div/form/table/tbody/tr[2]/td[2]/input')
            URL_field.send_keys(line[2])
            time.sleep(3)

            Title_field = driver.find_element("xpath", '/html/body/div[3]/div/div[1]/div/form/table/tbody/tr[1]/td[2]/input')
            Title_field.send_keys(line[3])
            time.sleep(3)

            Description_field = driver.find_element("xpath", '/html/body/div[3]/div/div[1]/div/form/table/tbody/tr[3]/td[2]/textarea')
            Description_field.send_keys(line[4])
            time.sleep(3)
            element = driver.find_elements(By.NAME, 'CATEGORY_ID')
            print('ok')
            drp = Select(element[0])
            selected_option = combobox.get()  # Get the selected option from the combobox
            drp.select_by_visible_text(selected_option)
            time.sleep(4)
    driver.quit()  # Close the WebDriver

button = ttk.Button(win, text="Open Website", command=open_website)
button.pack()
win.mainloop()
