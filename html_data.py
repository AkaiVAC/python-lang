from html.parser import HTMLParser


class HTMLData(HTMLParser):
    def handle_comment(self, data: str) -> None:
        self.print_data('comment', self.getpos(), data)

    def handle_starttag(self, tag: str, attrs):
        self.print_data(tag, self.getpos(), attrs)

    def handle_endtag(self, tag: str) -> None:
        self.print_data(tag, self.getpos())

    def handle_data(self, data: str) -> None:
        if(data.isspace):
            return
        self.print_data('data', self.getpos(), data)

    def print_data(self, tag, pos, data=''):
        print('Encountered ' + tag + ':', data,
              'line:', pos[0], 'position:', pos[1])


def main():
    parser = HTMLData()
    html_file = open('files/index.html')
    if html_file.mode == 'r':
        contents = html_file.read()
        parser.feed(contents)
    html_file.close()


if (__name__ == '__main__'):
    main()
