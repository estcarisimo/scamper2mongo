# scamper2mongo

Scamper is active-probing tool developed and mantained by CAIDA, which allows us to run a large number of active measurements such as ping, traceroutes, paris-traceroutes, etc. Since the first release, scamper's output has been a binary file called warts, however, recent releases have incorporated translations from warts to JSON. 

Regarding mongoDB is a NoSQL database which uses JSON inputs. Its goal is to provide access to schemeless data. Traceroute replies are likely to show irregular and schemeless patters, thus it is worth exploring mongoDB. 

This repo focuses on explaining how to load scamper's warts ouput into a mongoDB and then using Python, retrieve and handle the data.

## Requirements

It is necessary to have mongoDB and scamper.

```
$ sudo apt-get update; sudo apt-get install mongodb scamper
```

Additionally, to run python scripts pymongo have to be installed

```
$ sudo pip install pymongo
```

## How to use

1) You have to load scamper's outputs into mongoDB. The example database called 'scamper' will be filled with the warts files that contains the results, which are located in /pings and /traceroutes. The following BASH scripts fill the databse:

```
$ ./loadPingsData.sh
$ ./loadTracerouteData.sh
```
The sentence used to run the ping or the traceroute is inclueded (commented) in each file in caes you were interested in running it again by yourself.

2) You can run any python script to retrieve the results of both measurements.

```
$ python mongoTRACEROUTEexample.py
$ python mongoPINGexample.py
```

The code in each script is pretty simple and both outputs are not really meaningful but you can have a look at the code to get involved with mongo's pipeline, which is the equivalent to the SQL query.
