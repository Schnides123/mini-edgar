# -*- coding: utf-8 -*-
import scrapy
from ..items import EdgarData

from bs4 import BeautifulSoup

class Crawler(scrapy.Spider):

    name = 'crawler'
    allowed_domains = ['sec.gov']
    start_urls = []

    def __init__(self, cik_ticker=None, output_path="data", output_name=None):
        if not cik_ticker:
            cik_ticker = input("Enter a CIK number or ticker to search for.")
        self.id = cik_ticker.strip()
        self.path = output_path
        self.output_name = output_name if output_name else self.id
        self.start_urls = [
            'https://www.sec.gov/cgi-bin/browse-edgar?CIK={}&owner=exclude&action=getcompany&Find=Search'.format(self.id)
        ]

    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        table = soup.find("table", {"class": "tableFile2"})
        rows = table.findAll("tr") if table else []
        link = None
        for row in rows:
            cell = row.find(text="13F-HR")
            if cell:
                # *Cries in HTML*
                link = row.find("a", {"id": "documentsbutton"})
                break
        if link and len(link) > 0:
            link = "https://"+self.allowed_domains[0]+link["href"]
            return scrapy.Request(link, self.parse_docs_page)

    def parse_docs_page(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        rows = soup.find("table", {"class": "tableFile"}).findAll("tr")
        file_url = None
        for row in rows:
            cell = row.find(text="INFORMATION TABLE")
            link = row.find("a", href=lambda ref: ref and ".xml" in ref, text=lambda text: text and ".xml" in text)
            if cell and link:
                file_url = "https://" + self.allowed_domains[0] + link["href"]
                break
        if file_url:
            return scrapy.Request(file_url, self.parse_data)

    def parse_data(self, response):
        soup = BeautifulSoup(response.body, "lxml-xml")
        rows = soup.find_all("infoTable")
        if rows:
            first = rows[0]
            keys = []
            data = []
            for row in rows:
                row_data = {}
                for tag in row.find_all():
                    #strip container tags to flatten out rows
                    if len(tag.contents) <= 1:
                        if tag.name not in keys:
                            keys.append(tag.name)
                        row_data[tag.name] = tag.text
                data.append(row_data)
            results = EdgarData()
            results["keys"] = keys
            results["data"] = data
            return results