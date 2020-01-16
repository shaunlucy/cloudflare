# -*- coding: utf-8 -*-
# python 3.8.1 by:chunlai
import json
import CloudFlare

def main():
    filename = input('Please input filename: ')
    try:
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line: break
                zone_name = line.strip()
                print(zone_name)
                try:
                    cf = CloudFlare.CloudFlare(email='@gmail.com', token='904655a9908c0072d6e809b300f5302d9cae6') 
                    zone_info = cf.zones.post(data={'jump_start':False, 'name': zone_name})
                    zone_id = zone_info['id']

                    dns_records = [
                        {'type':'A','name':'@','content':'204.188.215.213','proxied':True},
                        {'type':'A','name':'www','content':'204.188.215.213','proxied':True},
                        {'type':'A','name':'wap','content':'204.188.215.213','proxied':True},
                        {'type':'A','name':'m','content':'204.188.215.213','proxied':False}
                    ]

                    for dns_record in dns_records:
                        r = cf.zones.dns_records.post(zone_id, data=dns_record)
                    #exit(0)

                except CloudFlare.exceptions.CloudFlareAPIError as e:
                    exit('api error: %d %s' % (e, e))

    except CloudFlare.exceptions.CloudFlareAPIError as e:
        exit('api error: %d %s' % (e, e))


if __name__ == '__main__':
    main()
