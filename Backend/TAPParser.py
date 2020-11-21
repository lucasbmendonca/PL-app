import	ply.lex as lex
from TreeManagement import TreeManagement
from treelib import Node, Tree
from utils import slurp, GetTreeLevel



class TAPLexer:
    '''
    "TAPLexer" class is used to break input text into a collection of tokens specified by a collection of regular expression rules.
    This class is composed by the following atributes:
        - self.tree_manager: contains the tree that stores, hierarchically, the tests and subtests status;
        - self.n_tests: total number of tests on the file;
        - self.n_ok_tests: total number of tests with "ok" status on the file;
        - self.n_nok_tests: total number of tests with "not ok" status on the file;
        - self.n_subtests: total number of subtests on the file;
        - self.n_ok_subtests: total number of subtests with "ok" status on the file;
        - self.n_nok_subtests: total number of subtests with "not ok" status on the file;
        - self.lexer: lexer itself.
    '''

    def __init__(self):
        self.tree_manager = TreeManagement()
        self.n_tests = 0
        self.n_ok_tests = 0
        self.n_nok_tests = 0
        self.n_subtests = 0
        self.n_ok_subtests = 0
        self.n_nok_subtests = 0
        self.lexer = None
    
    # Defining the tokens:

    tokens = ('N_TESTS', 'OK_TEST', 'NOK_TEST', 'N_SUBTESTS', 'OK_SUBTEST', 'NOK_SUBTEST', 'COMMENT')

    # A string containing ignored characters (new lines):
    t_ignore = "\n"

    # Handling errors:
    def t_error(self, t):
        t.lexer.skip(1)

    # Rule for comment token
    def t_COMMENT(self, t):
        r"-\s.*"
        t.value = t.value.replace("- ","")

    # Rule for test token; counts tests on file.
    def t_N_TESTS(self, t):
        r"[0-9]\.\.[0-9]+" 
        self.n_tests += int(t.value[3:])
        return t

    # Rule for subtest token; counts subtests on file.
    def t_N_SUBTESTS(self, t):
        r"\s[0-9]\.\.[0-9]+"
        self.n_subtests += int(t.value.strip()[3:])
        return t

    # Rule for "ok" status tests token; counts "ok" status tests on file.
    def t_OK_TEST(self, t):
        r"(ok)\s[0-9]+\s"
        self.tree_manager.CreateTestOkNode(t.value)
        self.id_aux = t.value
        self.n_ok_tests += 1
        return t

    # Rule for "ok" status subtests token; counts "ok" status subtests on file.
    def t_OK_SUBTEST(self, t):
        r"\s+(ok)\s[0-9]+\s"
        self.n_ok_subtests += 1
        self.id_aux = t.value
        self.tree_manager.CreateSubtestOkNode(t.value)
        return t

    # Rule for "not ok" status tests token; counts "not ok" status tests on file.
    def t_NOK_TEST(self, t):
        r"(not\sok)\s[0-9]+"
        self.n_nok_tests += 1
        self.id_aux = t.value
        self.tree_manager.CreateTestNotOkNode(t.value)
        return t

    # Rule for "not ok" status subtests token; counts "not ok" status subtests on file.
    def t_NOK_SUBTEST(self, t):
        r"\s+(not\sok)\s[0-9]+"
        self.n_nok_subtests += 1
        self.id_aux = t.value
        self.tree_manager.CreateSubtestNotOkNode(t.value)
        return t    
    
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Gets input file through token
    def inputFile(self, filePath):
        self.lexer.input(slurp(filePath))

    def execute(self):
        for token in iter(self.lexer.token, None):
            print(token)