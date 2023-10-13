class webscrapping:
	from bs4 import BeautifulSoup


	with open("WEBSCRAPPER.html", "r") as myfile:
		content = myfile.read()

		soup = BeautifulSoup(content, "lxml")
		course_codes = soup.find_all("h1")
		course_title = soup.find_all("h2")
		other_courses = soup.find_all("li")

		for codes in course_codes:
			print(codes.text)
		print("")
		for titles in course_title:
			print(titles.text)
		print("")
		for others in other_courses:
			print(others.text)
