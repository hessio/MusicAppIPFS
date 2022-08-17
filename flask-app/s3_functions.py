import boto3
import ipfshttpclient
import sys

def upload_file(file_name, bucket):
    object_name = file_name
    object_name = object_name.split("/")

    obj = object_name[-2] +'/'+object_name[-1]

    client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')
    res = client.add(file_name)

    f=open('hashes.txt')
    f.write(res)
    f.close()

    return res

def show_songs():
    public_urls = []
    with open('hashes.txt') as f:
        lines = f.readlines()
        for line in lines:
            public_urls.append(line.strip())
    f.close()
    
    return public_urls
