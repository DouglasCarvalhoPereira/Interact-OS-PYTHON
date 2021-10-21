import csv

hosts = [["worstation.local","192.283.83.38"], ["webserver.cloud", "192.897.78.98"]]

with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)