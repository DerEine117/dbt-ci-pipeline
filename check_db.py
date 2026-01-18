import duckdb

con = duckdb.connect("dbt_project/lakehouse.duckdb")

print(con.execute("show tables").fetchall())
print(con.execute("select * from fact_sales").fetchall())
