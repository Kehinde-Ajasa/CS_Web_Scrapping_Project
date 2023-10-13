class webscrapping:
	from bs4 import BeautifulSoup


	with open("WEBSCRAPPER.html", "r") as myfile:
		content = myfile.read()

		soup = BeautifulSoup(content, "lxml")
		course_template = soup.find_all("div", class_="course")
		for courses in course_template:
			course_name = courses.h2.text
			course_price = soup.find_all("p")[-1].text
			course_description = soup.find_all("p")[0].text
			print(course_name)
			print(f'Description: {course_description}')
			print(course_price)
