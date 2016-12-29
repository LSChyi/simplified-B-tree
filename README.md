# simplified B+ tree
This is a final project of the NTU course EE 5178: database system, from sql to nosql

You can use this project to simulate how a B+ tree handle data, check the database statistics, B+ tree index status, record status, etc.

# Run
This project is using python3, so to run the query interface:

	pyton3 run.py
	
# Query Interface
The query interface has following commands:  

* R: specify the name of the relation
* I: insert data, Could have multiple (key-value, record), separated by ';'
* D: delete record
* Scan: scan index file
* q: single vaule index search and range query
* p: display data page of a relation/table
* c: file, index statistics