import shlex
from queryInterface import utils
from queryInterface.command import Command
from storageFile.relationTable import RelationTable

class QueryInterface:
    def __init__(self, relationTables):
        self.commands = {
            "help": Command("help", "print all of the support commands", "help [command]", self.help),
            "exit": Command("exit", "leave query interface", "", utils.emptyFn),
            "R": Command("R", "specify the name of the relation", "R, Relation-name, key-type, record-length", utils.emptyFn),
            "I": Command("I", "insert data, Could have multiple (key-value, record), separated by ';'", "I, Relation-name, key-value [; key-value]", utils.emptyFn),
            "D": Command("D", "delete record", "D, Relation-name, key-value", utils.emptyFn),
            "Scan": Command("Scan", "scan index file", "Scan Relation-name", utils.emptyFn),
            "q": Command("q", "single vaule index search and range query", "single value: q Relation-name key-value\nrange query: q Relation-name key-value1 key-value2", utils.emptyFn),
            "p": Command("p", "display data page of a relation/table", "p relation-name page-id", utils.emptyFn),
            "c": Command("c", "file, index statistics", "c relation-name", utils.emptyFn),
        }
        self.relationTables = relationTables

    def run(self):
        self.greet()
        inputStr = ""
        while(inputStr != "exit"):
            inputStr = input("query> ")
            parsedStr = shlex.split(inputStr)
            command = parsedStr[0][:-1] if parsedStr[0][-1] == "," else parsedStr[0]
            params = parsedStr[1:]
            if command not in self.commands:
                print("The command '{}' does not support!".format(command))
            else:
                self.commands[command].doIt(params)
            
        print("Bye")

    def greet(self):
        print("From SQL to noSQL final project")
        print("B+ tree query interface")
        print("enter 'exit' to leave, 'help' for help")

    def help(self, params):
        if params and len(params) == 1:
            if params[0] not in self.commands:
                print("The command '{}' does not support!".format(params[0]))
            else:
                print(self.commands[params[0]])
                print("usage: \n\t{}".format(self.commands[params[0]].usage))

        else:
            self.greet()
            print("\nsupport commands:\n")
            order = ["R", "I", "D", "Scan", "q", "p", "c"]
            for command in order:
                print(self.commands[command])

        print("")
