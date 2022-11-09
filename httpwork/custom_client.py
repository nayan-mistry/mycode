import http.client

def main():
    conn = http.client.HTTPConnection("localhost",9021)

    conn.request('HEAD', '/')

    res = conn.getresponse()

    print(res.status, res.reason)

    conn.request('GET', '/')

    res = conn.getresponse()

    print(res.status, res.reason)

    page_data = res.read()

    print(page_data)

if __name__ == "__main__":
    main()