from tools.sql_parser import parse_sql
from tools.mongo_mapper import map_to_mongo

def dict_to_mongo_str(d):
    if not isinstance(d, dict):
        return str(d)

    parts = []
    for key, value in d.items():
        if isinstance(value, dict):
            inner = dict_to_mongo_str(value)
            parts.append(f"{key}: {inner}")
        elif isinstance(value, str):
            parts.append(f"{key}: '{value}'")
        else:
            parts.append(f"{key}: {value}")

    return "{ " + ", ".join(parts) + " }"

def build_query(mongo_dict: dict) -> str:
    collection = mongo_dict['collection']
    filter_ = dict_to_mongo_str(mongo_dict["filter"])
    projection = dict_to_mongo_str(mongo_dict["projection"])
    limit = mongo_dict["limit"]


    query = f"db.{collection}.find({filter_}, {projection})"

    if limit:
        query += f".limit({limit})"

    return query

