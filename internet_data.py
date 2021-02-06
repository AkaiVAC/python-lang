import urllib.request


class InternetData:
    def __init__(self):
        self.get_data_from_url()

    def get_data_from_url(self, url='http://www.google.com'):
        web_data = urllib.request.urlopen(url)
        print('result code: ' + str(web_data.getcode()))
        data = web_data.read()
        print(data)


if(__name__ == '__main__'):
    InternetData()
