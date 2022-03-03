#!/usr/bin/python3
"""save the data in a csv file from properati's api"""

import requests
import csv
from sys import argv


if __name__ == "__main__":
    url = "https://www.properati.com.co/_next/data/PLZGi_t9oPLT59HJnhDxo/s/rionegro-antioquia.json?search_params=rionegro-antioquia"
    todo = requests.get(url, verify=False).json()
    with open(f'{argv[1]}.csv', 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i, j in todo.items():
            if i == "pageProps":
                if type(j) == dict:
                    for n, m in j.items():
                        if n == "searchParams":
                            for o, p in m.items():
                                if o == "places":
                                    try:
                                        id_city = p[0]['id']
                                        name_city = p[0]['name']
                                        lon = p[0]['lon']
                                        lat = p[0]['lat']
                                        taskwriter.writerow([id_city, name_city, lon, lat])
                                    except:
                                        break
                        if n == "results":
                            for x, y in m.items():
                                if x == "data":
                                    b = 0
                                    for a in y:
                                        id_lote = y[b]['id']
                                        try:
                                            stratum = y[b]['stratum']
                                        except:
                                            stratum = "None"
                                        price = y[b]['price']['amount']
                                        try:
                                            mt2 = y[b]['surface']['total']
                                        except:
                                            mt2 = "None"
                                        if len(y[b]['address']) > 0:
                                            for k in y[b]['address'].keys():
                                                if k == 'street':
                                                    address = y[b]['address']['street']
                                                else:
                                                    address = y[b]['title']
                                        else:
                                            address = y[b]['title']
                                        b += 1
                                        taskwriter.writerow([id_lote, stratum, price, mt2, address])
            else:
                pass
