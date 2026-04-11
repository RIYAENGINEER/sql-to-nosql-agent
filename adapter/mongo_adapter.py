def to_mongo(parsed: dict) -> dict:
    if parsed.get("group_by"):
        group_field = parsed["group_by"]

        if parsed.get("aggregation") =="count":
            return {
                "collection": parsed["collection"],
                "pipeline":[
                    {"$group" : {
                        "_id": f"${group_field}",
                        "count":{"$sum":1}
                    }
                    }

                ]
            }
        

    if parsed.get("join"):
        join = parsed["join"]

        return {
            "collection" : parsed["collection"],
            "pipeline":[
                {
                    "$lookup": {
                        "from":join["table"],
                        "localfield": join["local_field"],
                        "foreignfield" : join["foreign_field"],
                        "as": join["table"]
                    }
                }
            ]
        }
    filter_ = parsed["filter"]
    projection = {field: 1 for field in parsed["projection"]}

    mongo_filter = {}

    op_map = {
        ">" : "$gt",
        "<" : "$lt",
        ">=" : "$gte",
        "<=" : "$lte",
        "=" : None
    }

    for field, condition in filter_.items():
        for op, value in condition.items():
            mongo_op = op_map.get(op)

            if mongo_op:
                mongo_filter[field] = {mongo_op:value}
            else:
                mongo_filter[field] = value
    

    return {
        "collection" : parsed["collection"],
        "filter" : mongo_filter,
        "projection" : projection,
        "limit":parsed.get("limit")

    }
