import re
from queryInterface import utils
from queryInterface.command import Command

class QueryInterface:
    def __init__(self, relationTables):
        self.commands = {
            "help": Command("help", "print all of the support commands", "help [command]", self.help),
            "exit": Command("exit", "leave query interface", "", utils.emptyFn),
            "R": Command("R", "specify the name of the relation", "R, Relation-name, key-type, record-length", utils.RFn),
            "I": Command("I", "insert data, Could have multiple (key-value, record), separated by ';'", "I, Relation-name, key-value [; key-value]", utils.IFn),
            "D": Command("D", "delete record", "D, Relation-name, key-value", utils.DFn),
            "Scan": Command("Scan", "scan index file", "Scan Relation-name", utils.ScanFn),
            "q": Command("q", "single vaule index search and range query", "single value: q Relation-name key-value\nrange query: q Relation-name key-value1 key-value2", utils.qFn),
            "p": Command("p", "display data page of a relation/table", "p relation-name page-id", utils.pFn),
            "c": Command("c", "file, index statistics", "c relation-name", utils.cFn),
        }
        self.relationTables = relationTables

    def run(self):
        self.greet()
        inputStr = ""
        while(inputStr != "exit"):
            inputStr = input("query> ")
            parsedStr = re.split(r',|\s|(".+?")|(\'.+?\')', inputStr)
            parsedStr = [ s for s in parsedStr if s is not None and s is not '' ]
            if parsedStr:
                command = parsedStr[0]
                params = parsedStr[1:]
                if command not in self.commands:
                    print("The command '{}' does not support!".format(command))
                else:
                    self.commands[command].doIt(params, self.relationTables)

                print("")
            
        print("Bye")

    def greet(self):
        print("From SQL to noSQL final project")
        print("B+ tree query interface")
        print("enter 'exit' to leave, 'help' for help")

    def help(self, *params):
        if params and len(params[0]) == 1:
            command = params[0][0]
            if command not in self.commands:
                print("The command '{}' does not support!".format(command))
            else:
                print(self.commands[command])
                print("usage: \n\t{}".format(self.commands[command].usage))

        else:
            self.greet()
            print("\nsupport commands:\n")
            order = ["R", "I", "D", "Scan", "q", "p", "c"]
            for command in order:
                print(self.commands[command])

