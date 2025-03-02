import re

def classify_token(token):
    token_types = {
        'tipo_dato': ['int', 'float', 'char', 'void', 'string'],
        'identificador': r'^[a-zA-Z_]\w*$',
        'constante': r'^(\d+(\.\d+)?|pi|y)$',
        'puntuacion': {';': 3, ',': 4},
        'parentesis': {'(': 5, ')': 6},
        'llaves': {'{': 7, '}': 8},
        'operador_asignacion': {'=': 9},
        'palabra_reservada': {'if': 9, 'while': 10, 'return': 11, 'else': 12, 'for': 13},
        'opAdicion': {'+': 14, '-': 14},
        'opMultiplicacion': {'*': 15, '/': 15, '<<': 15, '>>': 15},
        'opLogico': {'&&': 16, '||': 16},
        'opRelacional': {'<': 17, '>': 17, '>=': 17, '<=': 17, '==': 17, '!=': 17},
        'fin': {'$': 18}
    }
    
    for category, values in token_types.items():
        if isinstance(values, list) and token in values:
            return (token, 0)
        elif isinstance(values, dict) and token in values:
            return (token, values[token])
        elif isinstance(values, str) and re.match(values, token):
            return (token, 1 if category == 'identificador' else 2)
    
    return (token, 'ERROR')

def lexical_analyzer(input_string):
    tokens = re.findall(r'\w+|[{}(),;=+\-*/<>!$]|&&|\|\|', input_string)
    categorized_tokens = [classify_token(token) for token in tokens]
    
    token_count = {}
    errors = []
    
    for token, category in categorized_tokens:
        if category == 'ERROR':
            errors.append(token)
        else:
            token_count[category] = token_count.get(category, 0) + 1
    
    for token, category in categorized_tokens:
        print(f'Token: {token} \t Categoria: {category}')
    
    print('\nResumen:')
    for category, count in token_count.items():
        print(f'Categoria {category}: {count} tokens')
    
    if errors:
        print('\nErrores encontrados en los siguientes tokens:', ', '.join(errors))

# Solicitar entrada al usuario
entrada = input("Ingrese el código a analizar: ")
lexical_analyzer(entrada)
