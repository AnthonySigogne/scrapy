# Scrapy
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)

This repository contains a list of simple scrapers made with Scrapy :

- basicspider.py - A simple spider that scraps data from a list of pages :  
```
scrapy runspider basicspider.py -a file=list_pages.txt -o data.csv
```

- basicrawler.py - A simple crawler that scraps data from a list of domains :
```
scrapy runspider basicrawler.py -a file=list_pages.txt -o data.csv
```

- persistencespider.py - A simple spider that scraps data from a list of pages, and saves it in the Elasticsearch database running at http://localhost:9200/ :
```
scrapy runspider persistencespider.py -a file=list_pages.txt
```

- persistencecrawler.py - A simple crawler that scraps data from a list of domains, and saves it in the Elasticsearch database running at http://localhost:9200/ :
```
scrapy runspider persistencecrawler.py -a file=list_pages.txt
```

## LICENCE
MIT
