import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Where
from sqlparse.tokens import Keyword, DML



def parse_sql(query: str) -> dict:
    parsed = sqlparse.parse(query)[0]

    result = {
        "collection": None,
        "projection": [],
        "filter" : {},
        "limit": None 
    }
    
    tokens = [token for token in parsed.tokens if not token.is_whitespace]

    for i, token in enumerate(tokens):
        val = token.value.upper()

        if val == "SELECT":
            columns = tokens[i+1]
            result["projection"] = [col.strip() for col in columns.value.split(",")]

        elif val == "WHERE":
            condition = tokens[i+1].value
            result["filter"] = parse_where(condition)
        
        elif val == "LIMIT":
        
            result["limit"] = int(tokens[i+1].value)

    return result




def parse_where(condition:str) -> dict:
    operators = [">=","<=","<",">","="]

    for op in operators:
        for op in condition:
            left,right = condition.split(op)
            return {
                left.strip(): {
                    op: parse_value(right.strip())
                }
            }
    return{}

def parse_value(val:str):
    val = val.strip()

    if val.startwith("'") and val.endwith("'"):
        return val[1:-1]
    
    if val.isdigit():
        return int(val)
    
    return val


query = "SELECT name, age from users WHERE age > 25 LIMIT 5"

print(parse_sql(query))
