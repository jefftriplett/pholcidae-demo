import click
import toml

from pholcidae2 import Pholcidae
from slugify import slugify
from urllib import parse


OUTPUT = {}


class MySpider(Pholcidae):

    def crawl(self, data):
        status = str(data['status'])
        url = data['url']

        OUTPUT[url] = {
            'status': status,
        }

        if status != '200':
            if status not in OUTPUT:
                OUTPUT[status] = []
            OUTPUT[status].append(url)

        click.secho(
            f'{status},{url}',
            fg='white' if status == '200' else 'green' if status == '404' else 'red'
        )


@click.command()
@click.option('--threads', '-t', default=1)
@click.argument('url')
def main(threads, url):
    value = parse.urlparse(url)

    settings = {
        'protocol': f'{value.scheme}://',
        'domain': value.netloc,
        'start_page': value.path,
        'threads': threads,
    }

    domain_slug = slugify(settings['domain'])

    spider = MySpider()
    spider.extend(settings)
    spider.start()

    output_filename = f'{domain_slug}.toml'
    click.secho(f'writing {output_filename}', fg='green')

    with open(output_filename, 'w') as output_buffer:
        toml.dump(OUTPUT, output_buffer)

    click.secho('done', fg='green')


if __name__ == '__main__':
    main()
