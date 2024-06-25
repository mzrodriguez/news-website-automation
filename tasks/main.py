import sys
import logging
import yaml

import pandas as pd

from yaml.loader import SafeLoader
from datetime import datetime

from news_website import NewsWebsiteAutomation
from RPA.Robocloud.Items import Items

logging.basicConfig(filename=f'./logs/{datetime.today().strftime("%m_%d_%Y")}.log', format='%(asctime)s - %(message)s', filemode='w')

def config_file() -> dict:
    try:
        with open('./configuration_file/.config') as yaml_config:
            return yaml.safe_load(yaml_config)
    except IOError:
        return {}
    except yaml.YAMLError as ye:
        logging.warning('error in configuration file ' + str(ye))
        sys.exit()

config = config_file()

def main():
    items = Items()
    workitems = items.get_work_item_variable()
    newswebsite = NewsWebsiteAutomation(
            config, logging, workitems["variables"].get("url"), workitems["variables"].get("search_phrase"), 
            workitems["variables"].get("category"))
    newswebsite.open_news_website()
    newswebsite.search_news()

if __name__=="__main__":
    main()