from queryInterface.queryInterface import QueryInterface
import sys

relationTables = []

interface = QueryInterface(relationTables)
if len(sys.argv) == 2:
    script = [ line.rstrip("\n") for line in open(sys.argv[-1]) if line != "\n" ]
    interface.runScript(script)

interface.run()
