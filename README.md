# Pholcidae Demo

[Pholcidae](https://github.com/bbrodriges/pholcidae) is a "Tiny python web crawler" which makes writing customer spiders for checking for bad links on websites easily. 

This is a simple demo that I use as a starting point for building a crawler. 

The website's status code and URL are printed in CSV parse-able output. 

## Installation

```shell
$ git clone git@github.com:jefftriplett/pholcidae-demo.git
$ cd pholcidae-demo
$ pipenv install
```

## Usage

```shell
$ python spider.py
Usage: spider.py [OPTIONS] URL

Options:
  -t, --threads INTEGER
  --help                 Show this message and exit.

Usage Examples:

   Spider localhost with two threads:
   $ python spider.py --threads=2 http://localhost:8000/
   200,http://localhost:8000/
   200,http://localhost:8000/about/
   200,http://localhost:8000/blog/
   done

   # view results in toml format for easy digestion
   $ cat localhost-8000.toml
   ["http://localhost:8000/"]
   status = "200"

   ["http://localhost:8000/about/"]
   status = "200"

   ["http://localhost:8000/blog/"]
   status = "200"
```
