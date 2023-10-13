class webscrapping:
	from bs4 import BeautifulSoup


	with open("WEBSCRAPPER.html", "r") as myfile:
		content = myfile.read()

		soup = BeautifulSoup(content, "lxml")
		tags = soup.find_all('p')
		print(tags)