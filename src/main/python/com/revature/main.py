#!/usr/bin/env python3
from controller.controller import run
import logging
import logging.config
import os
import yaml
'''
This is your main script, this should call several other scripts within your packages.
'''
def main():
    configured_logging()
    run()
def configured_logging(config_path='../../../resources/logging.yaml'):
    if os.path.exists(config_path):
        with open(config_path,'r') as f:
            config = yaml.safe_load(f.read())
        
        #Enable our loaded configuration
        logging.config.dictConfig(config)
    else:
        raise ValueError('Logging configuration not found')

if __name__ == '__main__':
	main()