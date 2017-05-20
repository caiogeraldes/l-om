import hk_dv, iast_dv, hk_iast, iast_hk, dv_hk, dv_iast, checktranslit


def conversor_texto(texto, tipo_entrada='IAST', tipo_saida="Devanāgarī"):
    """Recebe (str, str) ==> .txt"""
    entrada = open("%s.txt" % texto, mode='r')
    linhas = entrada.readlines()
    saida = open("%s_saida.txt" % texto, mode="x")

    if tipo_entrada == 'IAST':
        if tipo_saida == "Devanāgarī":
            for linha in linhas:
                saida.write(iast_dv.conversor(linha) + '\n')
        if tipo_saida == 'Harvard-Kyoto':
            for linha in linhas:
                saida.write(iast_hk.conversor(linha) + '\n')
    elif tipo_entrada == 'Harvard-Kyoto':
        if tipo_saida == "Devanāgarī":
            for linha in linhas:
                saida.write(hk_dv.conversor(linha) + '\n')
        elif tipo_saida == "IAST":
            for linha in linhas:
                saida.write(hk_iast.conversor(linha) + '\n')
    elif tipo_entrada == 'Devanāgarī':
        if tipo_saida == "IAST":
            for linha in linhas:
                saida.write(dv_iast.conversor(linha) + '\n')
        elif tipo_saida == "Harvard-Kyoto":
            for linha in linhas:
                saida.write(dv_hk.conversor(linha) + '\n')

if __name__ == "__main__":
    conversor_texto("textos/teste")
