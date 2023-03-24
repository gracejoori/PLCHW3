import re

class Token:
    def __init__(self, token_type, token_value):
        self.token_type = token_type
        self.token_value = token_value

    def __str__(self):
        return f"({self.token_type}, {self.token_value})"

def tokenize(input_string):
    # Define regular expressions for each token type
    patterns = [
        ('ADD_OP', r'\+'),
        ('SUB_OP', r'-'),
        ('MUL_OP', r'\*'),
        ('DIV_OP', r'/'),
        ('MOD_OP', r'%'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('ASSIGN_OP', r'='),
        ('EQ_OP', r'=='),
        ('LT_OP', r'<'),
        ('LTE_OP', r'<='),
        ('GT_OP', r'>'),
        ('GTE_OP', r'>='),
        ('AND_OP', r'&&'),
        ('OR_OP', r'\|\|'),
        ('ID', r'[a-zA-Z_]\w*'),
        ('FLOAT_LIT', r'\d+\.\d+'),
        ('INT_LIT', r'\d+')
    ]
    
    # Combine regular expressions into a single pattern
    combined_pattern = '|'.join('(?P<%s>%s)' % pair for pair in patterns)
    
    # Tokenize input string
    tokens = []
    for match in re.finditer(combined_pattern, input_string):
        for token_type, token_value in match.groupdict().items():
            if token_value is not None:
                tokens.append(Token(token_type, token_value))
    
    return tokens

def parse_file(file_path):
    with open(file_path, 'r') as file:
        input_string = file.read()
        tokens = tokenize(input_string)
        return tokens
      
if __name__ == '__main__':
    # Parse the input file and get the tokens
    tokens = parse_file('input.txt')

    # Print the recognized tokens
    for token in tokens:
        print(token)
