import csv

import requests
from bs4 import BeautifulSoup


def main():
	url = 'https://www.homefacts.com/offenders/Tennessee/Robertson-County-1.html'  # What the link looks like
	base_url = 'https://www.homefacts.com/offenders/Tennessee/Robertson-County'  # The link we take as a basis
	page_part = '-'  # numbering separator
	query_part = '.html'  # end of link
	total_pages = get_total_pages(get_html(url))  # defining function i to generate pages
	for i in range(1, total_pages):
		url_gen = base_url + page_part + str(i) + query_part  # generated pages
		print(url_gen)  # console output generated pages
		html = get_html(url_gen)  # definition of get_total_pages parameter
		get_page_data(html)


def get_html(url):
	r = requests.get(url)
	return r.text  # return get_html as r.text


def get_total_pages(html):
	soup = BeautifulSoup(html, 'lxml')
	pages = soup.find('ul', class_='pagination').find_all('a', class_='last')[-1].get('href')  # number of pages
	total_pages = pages.split('-')[2].split('.')[0]  # we take the number of pages
	return int(total_pages)  # return the number of pages as total_pages


def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	ads = soup.find('div', class_='registeredOffenders').find_all('li', itemtype='https://schema.org/Person')
	for ad in ads:  # starting a cycle for receiving external data
		try:
			offender_url = ad.find('a').get('href')[2:]
			full_offender_url = 'https://' + offender_url
			print(full_offender_url)
			ur = requests.get(full_offender_url).text
			soupur = BeautifulSoup(ur, 'lxml')
			findings_url = soupur.find('section', class_='main middle')
			for i in findings_url:  # internal data acquisition cycle
				try:
					title = i.find('h2').find('span').text
				except:
					title = ''
				try:
					adress = i.find('dd').text
				except:
					adress = ''
				try:
					DOB = 'Date of Brith "' + i.find_all('dd')[1].text + '"'
				except:
					DOB = ''
				try:
					Race = 'Race"' + i.find_all('dd')[2].text + '"'
				except:
					Race = ''
				try:
					Sex = 'Sex"' + i.find_all('dd')[3].text + '"'
				except:
					Sex = ''
				try:
					Eyes = 'Eyes"' + i.find_all('dd')[4].text + '"'
				except:
					Eyes = ''
				try:
					Height = 'Height"' + i.find_all('dd')[5].text + '"'
				except:
					Height = ''
				try:
					Hair = 'Hair"' + i.find_all('dd')[6].text + '"'
				except:
					Hair = ''
				try:
					Weight = 'Weight"' + i.find_all('dd')[7].text + '"'
				except:
					Weight = ''
				try:  # image acquisition and storage
					Photo = 'Photo"' + 'https://www.homefacts.com' + i.find('img').get('src')
					photo = 'https://www.homefacts.com' + i.find('img').get('src')
					j = requests.get(photo, stream=True)
					name = photo.split('/')[-1]
					with open(name, 'bw') as f:
						for chunk in j.iter_content(8192):
							f.write(chunk)
				except:
					Photo = ''
				data = {'title': title, 'adress': adress, 'DOB': DOB, 'Race': Race, 'Sex': Sex, 'Eyes': Eyes,
						'Height': Height, 'Hair': Hair, 'Weight': Weight, 'Photo': Photo, 'full_offender_url': full_offender_url}
				write_csv(data)
		except:
			offender_url = ''


def write_csv(data):
	with open('homefacts.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow((data['title'],
						 data['adress'],
						 data['DOB'],
						 data['Race'],
						 data['Sex'],
						 data['Eyes'],
						 data['Height'],
						 data['Hair'],
						 data['Weight'],
						 data['Photo'],
						 data['urls_info']))


if __name__ == '__main__':
	main()
