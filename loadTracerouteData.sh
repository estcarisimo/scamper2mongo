#! /bin/bash

#To generate a traceroute like the example:
# $ sudo scamper -c "trace -s 33443 -d 53 -P UDP-Paris -w 1 -q 1 -g 10" -O warts -o exampleTraceroute.warts -i 8.8.8.8

# Some ideas taken from https://gist.github.com/fabien0102/88dcaa184d801fd5e67a
# It is not necessary to create neither the DATABASE nor the COLLECTION before loading the warts file
ls -1 traceroutes/*.warts | while read wartsfile; do sc_warts2json $wartsfile|mongoimport -d scamper -c traceroutes --jsonArray -type json; done

#To create indexes
#mongo scamper --eval 'db.traceroutes.createIndex( { "src": 1 ,"dst": 1 ,"hops.addr": 1 ,"hops.reply_ttl": 1 ,"hops.probe_ttl": 1 })'

#To drop collection
#mongo scamper --eval 'db.traceroutes.drop()'