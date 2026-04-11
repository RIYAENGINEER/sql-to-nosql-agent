# 🚀 SQL-to-NoSQL Intelligent Agent

A modular, production-style query translation system that converts SQL queries into NoSQL queries (MongoDB) using a hybrid architecture combining deterministic parsing and LLM-assisted reasoning.

---

## 🧠 Overview

This project implements an **agent-based query engine** that transforms relational SQL queries into equivalent NoSQL queries.

It supports core SQL operations such as filtering, aggregation, and joins, and maps them into MongoDB query constructs like `$match`, `$group`, and `$lookup`.

---

## ⚙️ Features

* ✅ SQL → MongoDB query translation
* ✅ Supports:

  * `SELECT`
  * `WHERE`
  * `LIMIT`
  * `GROUP BY` → `$group`
  * `JOIN` → `$lookup`
* ✅ Modular adapter-based architecture (multi-DB extensible)
* ✅ LLM integration (via Ollama) for reasoning layer
* ✅ Deterministic parsing for reliability (no hallucination risk)
* ✅ Basic query validation layer

---

## 🏗️ Architecture

```
SQL Query
   ↓
Parser (sqlparse-based)
   ↓
Intermediate Representation (IR)
   ↓
Agent (validation + orchestration)
   ↓
Adapter Layer
   ├── Mongo Adapter
   └── (Extensible to other NoSQL DBs)
   ↓
Query Builder
   ↓
MongoDB Query Output
```

---

## 📁 Project Structure

```
SQLtoNOSQL_agent/
│
├── agent/
│   └── llm_agent.py
│
├── tools/
│   ├── sql_parser.py
│
├── adapters/
│   ├── mongo_adapter.py
│   ├── mongo_builder.py
│
├── utils/
│   └── ollama_client.py
│
├── README.md
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone Repository

```
git clone https://github.com/RIYAENGINEER/sql-to-nosql-agent.git
cd sql-to-nosql-agent
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run Ollama (for LLM support)

```
ollama run llama3
```

---

### 4. Run the Agent

```
python agent/llm_agent.py
```

---

## 🧪 Example

### Input SQL

```
SELECT department, COUNT(*) FROM employees GROUP BY department;
```

### Output MongoDB Query

```
db.employees.aggregate([
  {
    $group: {
      _id: "$department",
      count: { $sum: 1 }
    }
  }
])
```

---

## 🔍 Supported Transformations

| SQL Feature | MongoDB Equivalent |
| ----------- | ------------------ |
| WHERE       | Filter (`$match`)  |
| SELECT      | Projection         |
| LIMIT       | `.limit()`         |
| GROUP BY    | `$group`           |
| JOIN        | `$lookup`          |

---

## 🧩 Extensibility

The system uses an **adapter-based architecture**, allowing easy extension to other NoSQL databases such as:

* DynamoDB
* Cassandra
* Elasticsearch

---

## 🛡️ Validation Layer

Basic query validation ensures:

* Presence of table (`FROM`)
* Valid JOIN conditions
* Correct GROUP BY usage

---

## 🔮 Future Improvements

* Multi-DB support (DynamoDB, Cassandra)
* Complex joins and nested queries
* Natural language → SQL conversion
* Query optimization layer
* UI interface (Streamlit)

---

## 🧠 Key Learnings

* AST-based query parsing
* Query translation between paradigms
* Agent-based system design
* Modular and extensible architecture
* Integration of LLMs with deterministic systems

---

## 👩‍💻 Author

Priyadharshini M

---

## ⭐ If you found this useful

Give it a star ⭐ on GitHub!
