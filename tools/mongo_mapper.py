from tools.sql_parser import parse_sql


def map_operator(op:str):
    mapping ={
        ">": "$gt",
        "<":"$lt",
        ">=": "$gte",
        "<=":"$lte",
        "=":None

    }
    return mapping.get(op)

def map_filter(filter_dict:dict) -> dict:
    if not filter_dict:
        return {}
    
    field = list(filter_dict.keys())[0]
    condition = filter_dict[field]

    op = list(condition.keys())[0]
    value = condition[op]

    mongo_op = map_operator(op)

    if mongo_op:
        return {field: {mongo_op: value}}
    else:
        return {field: value}
    
def map_projection(projection: list) -> dict:
    return{field: 1 for field in projection}

def map_to_mongo(parsed: dict) -> dict:
    return {
        "collection": parsed["collection"],
        "filter":map_filter(parsed["filter"]),
        "projection":map_projection(parsed["projection"]),
        "limit":parsed["limit"]
    }


