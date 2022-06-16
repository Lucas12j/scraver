# Scraver

:construction:  Project in Construction  :construction:

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=Alpha%20Version&color=GREEN&style=for-the-badge)

## Description:

Scraver is a dedicated tool for scraping data on the web. Was planned to be a microservice with one function, to receive the parameters of the collection and returning the clean data. It can be used to collect data on static web pages or web page with dynamic javascript.

## Installation:

1. A Scraver docker image can be mounted using the following command:

```bash
docker build -t scraver .
```
   - You can also download a scraver image ready from Docker-hub from the following command:

```
docker pull lucas12j/scraver:latest
```

2. To generate a scraver container, run the following command:

```
docker run -ti --name scraver --hostname scraver -p 8080:80 lucas12j/scraver
```

## How use:

After installation, the tool will be ready to use. For more information, see the official Scraver documentation, available in following address:
> http://152.67.52.155/docscraver.html

### Hello world

In this first test, a request will be sent to the microservice. In this request we will collect the developer's contact data, available on the main page of the tool's documentation. 

For send the request, we will use the [cUrl](https://curl.se/).

``` cUrl

```


