import sqlite3
import pandas as pd
import os
import argparse

def generate_markdown_report(db_path, output_file=None):
    try:
        # Determine default output file if not specified
        if not output_file:
            base_name = os.path.splitext(os.path.basename(db_path))[0]
            output_file = f"{base_name}_report.md"

        # Connect to SQLite database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Fetch tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        tables = [table[0] for table in tables]
        
        # Initialize markdown content
        markdown = f"# SQLite Database Report: `{db_path}`\n\n"
        markdown += "## Summary\n\n"
        markdown += f"- **Number of Tables**: {len(tables)}\n\n"
        
        # Process each table
        for table in tables:
            markdown += f"### Table: `{table}`\n\n"
            
            # Row count
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            row_count = cursor.fetchone()[0]
            markdown += f"- **Row Count**: {row_count}\n\n"
            
            # Schema
            markdown += f"#### Schema:\n\n"
            cursor.execute(f"PRAGMA table_info({table});")
            schema = cursor.fetchall()
            schema_md = "| Column | Type | Not Null | Default Value |\n|--------|------|----------|---------------|\n"
            for col in schema:
                schema_md += f"| {col[1]} | {col[2]} | {bool(col[3])} | {col[4] if col[4] else 'None'} |\n"
            markdown += schema_md + "\n"
            
            # Data preview
            if row_count > 0:
                markdown += f"#### Data Preview (First 5 Rows):\n\n"
                query = f"SELECT * FROM {table} LIMIT 5"
                df = pd.read_sql_query(query, conn)
                # Truncate text if > 10 chars
                df = df.map(lambda x: str(x)[:10] + "..." if isinstance(x, str) and len(x) > 10 else x)
                markdown += df.to_markdown(index=False) + "\n\n"
            else:
                markdown += "#### Data Preview: Table is empty\n\n"
            
            # Indexes
            markdown += f"#### Indexes:\n\n"
            cursor.execute(f"PRAGMA index_list({table});")
            indexes = cursor.fetchall()
            if indexes:
                index_md = "| Index Name | Unique |\n|------------|--------|\n"
                for idx in indexes:
                    index_md += f"| {idx[1]} | {bool(idx[2])} |\n"
                markdown += index_md + "\n"
            else:
                markdown += "No indexes defined.\n\n"

            # Foreign Keys
            markdown += f"#### Foreign Keys:\n\n"
            cursor.execute(f"PRAGMA foreign_key_list({table});")
            foreign_keys = cursor.fetchall()
            if foreign_keys:
                fk_md = "| Table | From Column | To Column |\n|-------|-------------|-----------|\n"
                for fk in foreign_keys:
                    fk_md += f"| {fk[2]} | {fk[3]} | {fk[4]} |\n"
                markdown += fk_md + "\n"
            else:
                markdown += "No foreign keys defined.\n\n"
            
            # Last Modification Time (if available)
            markdown += f"#### Last Modified (if available):\n\n"
            cursor.execute(f"SELECT MAX(rowid) FROM {table}")
            result = cursor.fetchone()
            if result and result[0]:
                markdown += f"- Last modified row ID: {result[0]}\n\n"
            else:
                markdown += "No modification timestamp available.\n\n"

        # Write to file
        with open(output_file, "w") as f:
            f.write(markdown)
        
        print(f"Markdown report generated: {output_file}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Markdown report for an SQLite database.")
    parser.add_argument("db_path", help="Path to the SQLite database file.")
    parser.add_argument("--output", help="Output Markdown file (optional).")
    args = parser.parse_args()

    generate_markdown_report(args.db_path, args.output)
