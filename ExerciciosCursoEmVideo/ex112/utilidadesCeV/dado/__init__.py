def leiaDinheiro(msgm):
    while True:
        resp = str(input(msgm)).replace(',', '.').strip()
        if resp.replace('.', '').isnumeric():
            resp = float(resp)
            break
        else:
            print(f'\033[0;30;41mERRO!! "{resp}" não é um valor válido\033[m')
    return resp
