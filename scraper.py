'''you can modify anything you want but don't forget to give cradit 😅 '''

import requests
from bs4 import BeautifulSoup
from time import sleep
import os
import sys

def start():
    print('''      
     ___  ___ _ __ __ _ _ __  _ __   ___ _ __ 
    / __|/ __| '__/ _` | '_ \| '_ \ / _ | '__|
    \__ | (__| | | (_| | |_) | |_) |  __| |   
    |___/\___|_|  \__,_| .__/| .__/ \___|_|   
                        | |   | |              
                        |_|   |_|   
                        
                                Author : rajkishor patra
                                version : 0.1
    ------------------------------------------------------------
                                                            ''')
    sleep(0.5)
    print('''
    (1) Question mode :
    (2) About :
    (3) Help :
    ''')
    while True:

        q = input('Enter any options like 1,2,3 : ')
        if '1' in q:
            try:
                clearConsole()
            except:
                print('somthing want wrong')
            scr()

        elif '2' in q:
            try:
                clearConsole()
            except:
                print('somthing want wrong')

            print('''
    This is a web scrapig tool made by mr.raj 
    this tool helping in many way like searching sothing in google but in terminal 
            ''') 
  
        
        elif '3' in q:
            try:
                clearConsole()
            except:
                print('somthing want wrong')
            print('''   
    commands:
        *what is 
        *father of 
        *meaning of

        use this commands in question mode
            ''')

        elif 'exit' in q:
            print('''
         _                  _                       
        | |__  _   _  ___  | |__  _   _  ___         
        | '_ \| | | |/ _ \ | '_ \| | | |/ _ \        
        | |_) | |_| |  __/ | |_) | |_| |  __/  _ _ _ 
        |_.__/ \__, |\___| |_.__/ \__, |\___| (_|_|_)
                    
                                Thanks for using scraper \U0001F607

                                        ''')
                                        
            sys.exit()

        else:
            print('Enter a valied key')
            
def scr():
    print(''' 
                                                      
                        _   _                          _     
         ___ _ _ ___ ___| |_|_|___ ___      _____ ___ _| |___ 
        | . | | | -_|_ -|  _| | . |   |    |     | . | . | -_|
        |_  |___|___|___|_| |_|___|_|_|    |_|_|_|___|___|___|
          |_|  
                                                      v-0.1  
                                                            ''')
   
    while True:
        
        query = input('\nEnter your Question :')
        if 'father of' in query:
            try:
                URL = 'https://www.google.com/search?q='+query

                headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
                }

                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                
                result = soup.find(class_='IZ6rdc').get_text()
                tt = result.replace('1','')
             
                print('Answer: ')
                print(tt)
            
            except:
                print('sorry boss no speakable data found')

        elif 'what is' in query:
            try:
                
                URL = 'https://www.google.com/search?q='+query

                headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
                }

                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                
                result = soup.find(class_='PZPZlf hb8SAc').get_text()
                r = result.replace('Wikipedia','').replace('Description','')
                print('\nAnswer: \n',r)
            
            except:
                print('sorry no data found')

        elif 'meaning of' in query:
            try:
                URL = 'https://www.google.com/search?q='+query

                headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
                }

                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                
                headings = soup.find(class_='LTKOO sY7ric').get_text()
                
                print('\nAnswer: \n',headings)
            
            except:
                print('sorry no data found')


        elif '0' in query or 'back' in query:
            start()

        elif 'exit' in query:
            print('''

    
         _                  _                       
        | |__  _   _  ___  | |__  _   _  ___         
        | '_ \| | | |/ _ \ | '_ \| | | |/ _ \        
        | |_) | |_| |  __/ | |_) | |_| |  __/  _ _ _ 
        |_.__/ \__, |\___| |_.__/ \__, |\___| (_|_|_)
                    
                                Thanks for using scraper \U0001F607

                                        ''')
            sys.exit()

        elif 'clear' in query:
            clearConsole()

        elif 'who create you' in query or 'who made you' in query or 'your creator' in query:
            print('mr.raj create me')

        else:
            print('sorry that question is not in my program')

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
        os.system(command)
    else:
        os.system('clear')

if __name__ == '__main__':
    start()