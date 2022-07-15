#Title: UnderRated Sports Bot
#Author: Corey Woodworth
#Version: 1.0
#Language: Python
#Synapsys:
#   This program is to scrape multiple betting sites and grab correct data to parse from source code.
# WARNING: This program is for testing purposes, please read the sites TOS and Robots.txt file
#          You will want to use a Proxy or VPN so you do not get your IP address blocked

#Libraries not used 
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

#Import Working Libraries From Classes
from bs4 import BeautifulSoup
from dateutil.parser import parse
from dateutil.tz import tzlocal 
from urllib.request import urlopen

#Import Libraries
import pandas as pd
import time
import string
import requests
import pytz
import pandas.io.sql as pd_sql
import sqlite3
import numpy as np
import datetime
import csv
import html
import re
import urllib.request
import urllib.error
import urllib.parse
import typing
import json
import json.decoder

url = "https://pinnacle-odds.p.rapidapi.com/kit/v1/special-markets/" #Call Pinnacle API

querystring = {"sport_id":"9","is_have_odds":"true"} #Query Prop Bets

#API headers that return Data
headers = {
	"X-RapidAPI-Key": "1d82cfea6dmsh2f04cebd560da75p15c81cjsne808b2b5e0e8",
	"X-RapidAPI-Host": "pinnacle-odds.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring) #Call the URL we requested and append it to the response variable. 

#Convert JSON file to CSV for database upload. Frame data for insertion.
df = pd.read_json (r'data.json')
df.to_csv (r'data1.csv', index = None)
df = pd.read_csv('data1.csv')


