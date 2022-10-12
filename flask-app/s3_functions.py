import subprocess
import sys
import time

def upload_file(file_name):
    object_name = file_name
    object_name = object_name.split("/")

    obj = object_name[-2] +'/'+object_name[-1]

    result = subprocess.run(['ipfs', 'add', file_name], stdout=subprocess.PIPE)
    url = subprocess.run(['w3', 'put', file_name], stdout=subprocess.PIPE)
    url = url.stdout.decode('utf-8')
    url = url.split('\n')[1]
    url = url[1:]
    print('THIs is URL:  '+ str(url), file=sys.stderr)
    res = result.stdout.decode("utf-8")
    print(res.split(' ')[1], file=sys.stderr)
    res = res.split(' ')[1]
    time.sleep(5)
    f=open('flask-app/hashes.txt', 'a')
    f.write(res)
    f.write('\n')
    f.write(url)
    f.write('\n')
    f.close()

    return res

def show_songs():
    public_urls = []
    with open('flask-app/hashes.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            public_urls.append(line.strip())
    f.close()
    
    return public_urls
