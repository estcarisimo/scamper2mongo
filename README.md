# scamper2mongo

Scamper is active-probing tool developed and mantained by CAIDA, which allows us to run a large number of active measurements such as ping, traceroutes, paris-traceroutes, etc. Since the first release, scamper's output has been a binary file called warts, however, recent releases have incorporated translations from warts to JSON. 

Regarding mongoDB is a NoSQL database which uses JSON inputs. Its goal is to provide access to schemeless data. Traceroute replies are likely to show irregular and schemeless patters, thus it is worth exploring mongoDB. 

This repo focuses on explaining how to load scamper's warts ouput into a mongoDB and then using Python, retrieve and handle the data.

##Requirements

It is necessary to have mongoDB and scamper.

```
$ sudo apt update; sudo apt-get install mongodb scamper
```

Additionally, to run python scripts pymongo have to be installed

```
$ sudo pip install pymongo
``` 
