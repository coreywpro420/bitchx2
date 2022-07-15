#old code
options = Options()
options.add_argument('disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://underratedmerch.com/index.php?route=account/newsletter")

content = driver.page_source
soup = BeautifulSoup(content, 'lxml')

print(soup)



"id":9
"p_id":3
"name":"Baseball"
"last":1657655703
"special_last":1657655702





#Create boiler plate for a simple HTML website that displays the returned data from Pinnacle API.
f = open('data.json', 'w')

#HTML Code Insert


#writin the code into the HTML file
f.write(str(response.text))

#Close the file 
f.close()