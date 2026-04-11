import sys
import os

# 🔧 Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.sql_parser import parse_sql
#from tools.mongo_mapper import map_to_mongo
#from tools.query_builder import build_query
from utils.ollama_client import generate_with_ollama
from adapter.mongo_adapter import to_mongo
from adapter.mongo_builder import build_mongo_query

class SQLToMongoAgent:

    def __init__(self):
        pass

    def run(self, query: str):
        print("\n[Agent] Received Query:", query)

        #  Step 1: LLM reasoning (optional but powerful)
        prompt = f"""
You are an AI assistant that converts SQL queries to MongoDB queries.

SQL Query:
{query}

Return only the MongoDB query.
"""

        llm_output = generate_with_ollama(prompt)
        print("\n[LLM Suggestion]:", llm_output)

        # 🔥 Step 2: Deterministic pipeline (core system)
        parsed = parse_sql(query)
        print("\n[Parsed SQL]:", parsed)

        mongo = to_mongo(parsed)
        print("\n[Mongo Mapping]:", mongo)

        final_query = build_mongo_query(mongo)
        print("\n[Final Query]:", final_query)

        return {
            "llm_output": llm_output,
            "final_query": final_query
        }


# 🧪 Test Runner
if __name__ == "__main__":
    agent = SQLToMongoAgent()

    query = "SELECT department, COUNT(*) FROM employees GROUP BY department"

    result = agent.run(query)

    print("\n FINAL OUTPUT:")
    print(result["final_query"])