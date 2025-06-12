# main.py
from query_runner import run_query
from display import print_results

if __name__ == "__main__":
    query = "SELECT * FROM your_table"
    results = run_query(query)
    print_results(results)