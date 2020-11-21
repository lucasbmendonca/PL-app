import json
from treelib import Node, Tree
from TAPParser import TAPLexer
from utils import slurp
import ply.lex as lex
import sys

recebido = sys.argv[1].split(',')

aEnviar = []

tamanho = len(recebido)

for nome in recebido:
    a = TAPLexer()
    a.build()
    a.inputFile("./inputs/" + nome)
    a.execute()
    data = a.tree_manager.mainTree.to_json()
    aEnviar.append(data)

print(aEnviar)


# print(a.tree_manager.mainTree.show())

data = a.tree_manager.mainTree.to_json()
# print(data)

# with open('./data.json', 'w') as outfile:
#     outfile.write(data)
#     outfile.close()