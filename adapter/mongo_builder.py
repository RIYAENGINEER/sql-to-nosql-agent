def format_dict(d):
    if not isinstance(d,dict):
        return str(d)
    
    parts =[]
    for k,v in d.items():
        if isinstance(v,dict):
            parts.append(f"{k} : {format_dict(v)}")

        else:
            parts.append(f"{k} : {v}")

    return "{" +"," .join(parts) + "}"


def build_mongo_query(mongo_dict: dict) -> str:
    if "pipeline" in mongo_dict:
        collection = mongo_dict["collection"]
        pipeline = mongo_dict["pipeline"]

        return f"db.{collection}.aggregate({pipeline})"
    collection = mongo_dict["collection"]
    filter_ = mongo_dict["filter"]
    projection = mongo_dict["projection"]
    limit = mongo_dict["limit"]

    query =f"db.{collection}.find({format_dict(filter_)}, {format_dict(projection)})"

    if limit:
        query +=f".limit({limit})"

    return query