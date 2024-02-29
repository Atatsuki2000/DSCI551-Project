import sys
import Database

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 clear_table.py <table_name> <arg>")
        sys.exit(1)

    table_name = sys.argv[1]
    arg = sys.argv[2]

    # Call the clear_table function with the provided arguments
    Database.clear_table(table_name, arg)