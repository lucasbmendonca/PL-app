from TAPParser import TAPLexer
from treelib import Node, Tree
import json
from globalstats import GlobalStats
from filesinfo import FileInfo
import sys
import os

relativePath = os.path.dirname(os.path.abspath(__file__))

#Files
received = sys.argv[1].split(',')

#Lexer
lex = TAPLexer()
lex.build()

#File global and individual info
globalStats = GlobalStats() 
globalStats.LoadFile(relativePath + "\\globalstats.json")

fileInfo = FileInfo()

for name in received:
    fullPath = relativePath + "\\inputs\\" + name
    lex.inputFile(fullPath)
    lex.execute(name)
    globalStats.UpdateStats(lex)
    fileInfo.UpdateFileInfo(globalStats, fullPath, lex)
    fileInfo.SaveToJSON(relativePath + "\\fileInfo.json")
    globalStats.SaveToFile(relativePath + "\\globalstats.json")

print(globalStats.__dict__)