from pymongo import MongoClient
import pprint

conn = MongoClient()
db_scamper = conn.scamper
col_traceroutes = db_scamper.traceroutes

result = col_traceroutes.aggregate( 
 [
                {"$group": { "_id": { "src": "$src", "dst": "$dst" } } }
            ]
        );
src_dst_list = list(result)

## This loops makes that results gets all the information of every ping.
## The SQL equivalent sentence would be: SELECT * from TABLE where src=X and dst=Y;
#for src_dst_pair in src_dst_list:
#    result = col_traceroutes.aggregate(
#            [
#                {"$match":{"src":{"$eq":src_dst_pair['_id']['src']}}},
#                {"$match":{"dst":{"$eq":src_dst_pair['_id']['dst']}}}
#            ]
#            )


for src_dst_pair in src_dst_list:
    result = col_traceroutes.aggregate( 
        [
            {"$match":{"src":{"$eq":src_dst_pair['_id']['src']}}},
            {"$match":{"dst":{"$eq":src_dst_pair['_id']['dst']}}},
            { "$unwind": "$hops" },
            {"$group": { "_id": {\
                                    "src": "$src",\
                                    "dst": "$dst" ,\
                                    "addr": "$hops.addr" ,\
                                    "probe_ttl": "$hops.probe_ttl" ,\
                                    "reply_ttl": "$hops.reply_ttl" \
                                    } } }
        ]
    );
    five_tuples = list(result)
    for five_tuple in five_tuples:
        print '---------------------------'
        pprint.pprint(five_tuple)
        result = col_traceroutes.aggregate(
        [
            {"$match":{"src":{"$eq":src_dst_pair['_id']['src']}}},
            {"$match":{"dst":{"$eq":src_dst_pair['_id']['dst']}}},
            {"$unwind":"$hops"},
            {"$match":{"hops.addr":{"$eq":five_tuple['_id']['addr']}}},
            {"$match":{"hops.probe_ttl":{"$eq":five_tuple['_id']['probe_ttl']}}},
            {"$match":{"hops.reply_ttl":{"$eq":five_tuple['_id']['reply_ttl']}}},
            { "$project": {"_id" : 0 ,"rtt":"$hops.rtt",'timestamp':'$start.sec'}}
        ]
        );
        
        print''
        
        RTTs = list(result)
        for rtt in RTTs:
            pprint.pprint(rtt)
