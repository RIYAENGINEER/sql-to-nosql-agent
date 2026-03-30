import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Where
from sqlparse.tokens import Keyword, DML
from sqlparse.sql import Comparison
from sqlparse.tokens import Operator


def parse_sql(query: str) -> dict:
    parsed = sqlparse.parse(query)[0]

    result = {
        "collection": None,
        "projection": [],
        "filter" : {},
        "limit": None 
    }
    
    for token in parsed.tokens:
        if token.is_whitespace:
            continue


        if token.ttype is DML and token.value.upper() =="SELECT":
            continue

        elif isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                result["projection"].append(identifier.get_name())

        elif isinstance(token, Identifier):
            if result["collection"] is None:
                result["collection"] = token.get_name()
            else:
                result["projection"].append(token.get_name())
        
        elif isinstance(token, Where):
            for t in token.tokens:
                if isinstance(t, Comparison):

                    left = t.left.get_name()

                    operator = None
                    for tok in t.tokens:
                        if tok.ttype is Operator.Comparison:
                            operator = tok.value

                    right = t.right.value

                    result["filter"] = {
                        left: {
                            operator: parse_value(right)
                        }
                    }

        elif token.ttype is Keyword and token.value.upper() == "LIMIT":

            idx = parsed.tokens.index(token)
            limit_token = parsed.tokens[idx + 2]
            result["limit"] = int(limit_token.value)

    return result 
    
    




def parse_where(condition:str) -> dict:
    condition = condition.strip()

    condition = " ".join(condition.split())

    operators = [">=","<=","<",">","="]

    for op in operators:
        for op in condition:
            parts = condition.split(op)
            if len(parts) == 2:
                left = parts[0].strip()
                right = parts[1].strip()
                return{
                    left:{
                        op:parse_value(right)
                    }
                }

    return{}

def parse_value(val:str):
    val = val.strip().strip(";")

    if val.startswith("'") and val.endswith("'"):
        return val[1:-1]
    
    if val.isdigit():
        return int(val)
    
    return val


query = "SELECT name, age from users WHERE age > 25 LIMIT 5"

print(parse_sql(query))
