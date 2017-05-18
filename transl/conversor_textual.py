import hk_dv, iast_dv, hk_iast, dv_iast, checktranslit

def conversor_texto(texto, modo = 'iast_dv'):
    """Recebe (str, str) ==> .txt"""
    entrada = open("%s.txt" % texto, mode='r')
    linhas = entrada.readlines()
    saida = open("%s1.txt" % texto, mode="x")

    if modo == 'iast_dv':
        for linha in linhas:
            saida.write(iast_dv.conversor(linha) + '\n')
    elif modo == 'hk_dv':
        for linha in linhas:
            saida.write(hk_dv.conversor(linha) + '\n')

if __name__ == "__main__":
    conversor_texto("textos/teste")
