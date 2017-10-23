#! /bin/bash

#To generate a traceroute like the example:
# $ sudo scamper -c "ping -c 10 -d 53 -m 5" -O warts -o examplePing.warts -i 8.8.8.8

# Some ideas taken from https://gist.github.com/fabien0102/88dcaa184d801fd5e67a
# It is not necessary to create neither the DATABASE nor the COLLECTION before loading the warts file
ls -1 pings/*.warts | while read wartsfile; do sc_warts2json $wartsfile|mongoimport -d scamper -c pings --jsonArray -type json; done

#To create indexes
#mongo scamper --eval 'db.pings.createIndex( { "src": 1 ,"dst": 1 ,"responses.from": 1 ,"responses.reply_ttl": 1 ,"ttl": 1 })'

#To drop collection
#mongo scamper --eval 'db.pings.drop()'