import requests
>>> from lxml import html
>>> response = requests.get(
...     'https://en.wikipedia.org/w/api.php',
...     params={
...         'action': 'parse',
...         'page': 'Bla Bla Bla',
...         'format': 'json',
...     }
... ).json()
>>> raw_html = response['parse']['text']['*']
>>> document = html.document_fromstring(raw_html)
>>> first_p = document.xpath('//p')[0]
>>> intro_text = first_p.text_content()
>>> print(intro_text)

first_p.t