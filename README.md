# SQLite-Report
Very simple Python script to generate a report on an sqlite db, into markdown.

Created for feeding into Language models.


## Installation

```bash
git clone https://github.com/tmceld/SQLite-Report
cd SQLite-Report
python3.11 -m venv .venv
source .venv/bin/activate 
pip install -r requirements.txt
echo "alias sqlreport=$PWD/.venv/bin/python $PWD/sqlreport.py" >> ~/.aliases 
source ~/.aliases
```

## Usage

```
sqlreport "Developer/ai/articleMetadata/summaries.sqlite3"
```

## Example Output

# SQLite Database Report: `Developer/ai/articleMetadata/summaries.sqlite3`

## Summary

- **Number of Tables**: 3

### Table: `sqlite_sequence`

- **Row Count**: 2

#### Schema:

| Column | Type | Not Null | Default Value |
|--------|------|----------|---------------|
| name |  | False | None |
| seq |  | False | None |

#### Data Preview (First 5 Rows):

| name    |   seq |
|:--------|------:|
| summary |     5 |
| people  |    32 |

#### Indexes:

No indexes defined.

#### Foreign Keys:

No foreign keys defined.

#### Last Modified (if available):

- Last modified row ID: 2

### Table: `summary`

- **Row Count**: 5

#### Schema:

| Column | Type | Not Null | Default Value |
|--------|------|----------|---------------|
| id | INTEGER | False | None |
| title | TEXT | True | None |
| url | TEXT | False | None |
| fingerprint | TEXT | False | None |
| article_date | TEXT | False | None |
| article_text | TEXT | False | None |
| author | TEXT | False | None |
| short_summary | TEXT | False | None |
| medium_summary | TEXT | False | None |
| date | TEXT | False | None |
| model | TEXT | False | None |
| created | TIMESTAMP | False | None |
| last_updated | TIMESTAMP | False | CURRENT_TIMESTAMP |

#### Data Preview (First 5 Rows):

|   id | title         | url           | fingerprint   | article_date   | article_text   | author        | short_summary   | medium_summary   | date   | model   | created       | last_updated   |
|-----:|:--------------|:--------------|:--------------|:---------------|:---------------|:--------------|:----------------|:-----------------|:-------|:--------|:--------------|:---------------|
|    1 | Starmer ne... | https://ww... | bMoq+elqTt... | 2023-09-22     |                | Bronwen Ma... | No summary...   | No summary...    |        | gemma2  | 2024-07-31... | 2024-07-31...  |
|    2 | The meanin... | https://ww... | 5iyiADUVaR... | 2012-08-03     |                | Janan Gane... | Boris John...   | While Bori...    |        | gemma2  | 2024-07-31... | 2024-07-31...  |
|    3 | How UK can... | https://ww... | 2Alas1Uk5w... | 2012-08-06     |                | Janan Gane... | The UK gov...   | While the ...    |        | gemma2  | 2024-07-31... | 2024-07-31...  |
|    4 | London’s E... | https://ww... | SJ0HhDUmGR... | 2012-08-13     |                | Janan Gane... | London's E...   | London's E...    |        | gemma2  | 2024-07-31... | 2024-07-31...  |
|    5 | Gifts and ... | https://ww... | wIs79MmqHB... | 2016-12-22     |                | Julian Bag... | No summary...   | No summary...    |        | gemma2  | 2024-07-31... | 2024-07-31...  |

#### Indexes:

No indexes defined.

#### Foreign Keys:

No foreign keys defined.

#### Last Modified (if available):

- Last modified row ID: 5

### Table: `people`

- **Row Count**: 32

#### Schema:

| Column | Type | Not Null | Default Value |
|--------|------|----------|---------------|
| id | INTEGER | False | None |
| name | TEXT | True | None |
| context | TEXT | False | None |
| url | TEXT | True | None |
| fingerprint | TEXT | False | None |
| article_date | TEXT | False | None |
| model | TEXT | False | None |
| created | TIMESTAMP | False | None |
| last_updated | TIMESTAMP | False | CURRENT_TIMESTAMP |

#### Data Preview (First 5 Rows):

|   id | name          | context       | url           | fingerprint   | article_date   | model   | created       | last_updated   |
|-----:|:--------------|:--------------|:--------------|:--------------|:---------------|:--------|:--------------|:---------------|
|    1 | Keir Starm... | Leader of ... | https://ww... | bMoq+elqTt... | 2023-09-22     | gemma2  | 2024-07-31... | 2024-07-31...  |
|    2 | David Lamm... | Shadow For... | https://ww... | bMoq+elqTt... | 2023-09-22     | gemma2  | 2024-07-31... | 2024-07-31...  |
|    3 | Rishi Suna... | Prime Mini... | https://ww... | bMoq+elqTt... | 2023-09-22     | gemma2  | 2024-07-31... | 2024-07-31...  |
|    4 | Boris John... | London may... | https://ww... | 5iyiADUVaR... | 2012-08-03     | gemma2  | 2024-07-31... | 2024-07-31...  |
|    5 | David Came... | Prime mini... | https://ww... | 5iyiADUVaR... | 2012-08-03     | gemma2  | 2024-07-31... | 2024-07-31...  |

#### Indexes:

No indexes defined.

#### Foreign Keys:

| Table | From Column | To Column |
|-------|-------------|-----------|
| summary | url | url |

#### Last Modified (if available):

- Last modified row ID: 32


