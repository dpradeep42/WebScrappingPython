import json
from urllib.request import Request, urlopen


def apicall():
    try:
        url = 'https://reqres.in/api/users/2'
        req = Request(url, headers={'User-Agent': 'Chrome/93.0'})
        content = urlopen(req)

        for line in content:
            decoded_line = line.decode("utf-8")
        data = json.loads(decoded_line).get('data')
        #print(type(data))
        with open("file.txt", 'w') as f:
            for temp in data.items():
                #print(temp)
                f.write('%s:%s\n' % (temp['id']))
        f = open("file.txt", "r")
        print(f.read())
    except:
        print("Error occured in apicall")


if __name__ == '__main__':
    apicall()
