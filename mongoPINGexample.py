from pymongo import MongoClient
import pprint

conn = MongoClient()
db_scamper = conn.scamper
col_pings = db_scamper.pings

result = col_pings.aggregate( 
 [
                {"$group": { "_id": { "src": "$src", "dst": "$dst" } } }
            ]
        );
src_dst_list = list(result)

## This loops makes that results gets all the information of every ping.
## The SQL equivalent sentence would be: SELECT * from TABLE where src=X and dst=Y;
#for src_dst_pair in src_dst_list:
#    result = col_pings.aggregate(
#            [
#                {"$match":{"src":{"$eq":src_dst_pair['_id']['src']}}},
#                {"$match":{"dst":{"$eq":src_dst_pair['_id']['dst']}}}
#            ]
#            )


for src_dst_pair in src_dst_list:
    result = col_pings.aggregate( 
        [
            {"$match":{"src":{"$eq":src_dst_pair['_id']['src']}}},
            {"$match":{"dst":{"$eq":src_dst_pair['_id']['dst']}}},
            { "$unwind": "$responses" },
            {"$group": { "_id": {\
                                    "src": "$src",\
                                    "dst": "$dst" ,\
                                    "from": "$responses.from" ,\
                                    "ttl": "$ttl" ,\
                                    "reply_ttl": "$responses.reply_ttl"\
                                    } } }
            ]
    );
    five_tuples = list(result)
    for five_tuple in five_tuples:
        pprint.pprint(five_tuple)
        result = col_pings.aggregate(
        [
            {"$match":{"src":{"$eq":src_dst_pair['_id']['src']}}},
            {"$match":{"dst":{"$eq":src_dst_pair['_id']['dst']}}},
            {"$unwind":"$responses"},
            {"$match":{"responses.from":{"$eq":five_tuple['_id']['from']}}},
            {"$match":{"ttl":{"$eq":five_tuple['_id']['ttl']}}},
            {"$match":{"responses.reply_ttl":{"$eq":five_tuple['_id']['reply_ttl']}}},
            { "$project": {"_id" : 0 ,"rtt":"$responses.rtt",'timestamp':'$responses.tx.sec'}}
        ]
        );
        RTTs = list(result)
        for rtt in RTTs:
            pprint.pprint(rtt)
