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


