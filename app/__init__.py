import io
import json
import os

PATH = 'config.json'
config = {}

def config_verify():
    if not (os.path.isfile(PATH) and os.access(PATH, os.R_OK)):
        print('Enter the data of the ESB application.')
        address = None
        address_conf = None
        while (not test_information(address, address_conf)):
            address = input("IP address: ")
            address_conf = input("IP address confirmation: ")

        port = None
        port_conf = None
        while (not test_information(port, port_conf)):
            port = input("Port: ")
            port_conf = input("Port confirmation: ")
        
        print('Creating configuration file.')
        return create_configuration_file(address, port)
    else:
        return open_configuration_file()

def test_information(value, value_conf):
    return (value != None and value.strip() != "" and value == value_conf)

def create_configuration_file(address, port):
    config['address'] = address
    config['port'] = int(port)

    with open(PATH, 'w') as outfile:
        json.dump(config, outfile)

    return config

def open_configuration_file():
    with open(PATH) as json_file:
        return json.load(json_file)