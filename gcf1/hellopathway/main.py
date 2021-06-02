def hello_Pathway(requests):
    requests_args = requests.args
    
    if requests_args and "name" in requests_args:
        name = requests_args['name']
    else:
        name = "Mordzia nie udało się"
    return f" Elo {name}"