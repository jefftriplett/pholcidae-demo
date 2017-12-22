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
   writing localhost-8000.toml
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

## Contact / Social Media

Here are a few ways to keep up with me online. If you have a question about this project, please consider opening a GitHub Issue. 

[![](https://jefftriplett.com/assets/images/social/github.png)](https://github.com/jefftriplett)
[![](https://jefftriplett.com/assets/images/social/globe.png)](https://jefftriplett.com/)
[![](https://jefftriplett.com/assets/images/social/twitter.png)](https://twitter.com/webology)
[![](https://jefftriplett.com/assets/images/social/docker.png)](https://hub.docker.com/u/jefftriplett/)
