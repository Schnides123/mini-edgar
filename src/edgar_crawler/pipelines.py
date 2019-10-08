# -*- coding: utf-8 -*-

import csv

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class EdgarCrawlerPipeline(object):
    def process_item(self, item, spider):
        file_path = spider.path+"/"+spider.output_name+".tsv"
        print("saving "+spider.id+" to file "+file_path+"...")
        with open(file_path, "w+", newline='') as file:
            writer = csv.DictWriter(file, item['keys'], restval="n/a", delimiter='\t')
            writer.writeheader()
            for row in item["data"]:
                writer.writerow(row)
            file.close()
        print("file saved successfully.")
        return
