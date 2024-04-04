import sys
import Database

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 clear_table.py <database_name> <table_name>")
        sys.exit(1)

    database_name = sys.argv[1]
    table_name = sys.argv[2]

    # Call the clear_table function with the provided arguments
    Database.clear_table(database_name, table_name)