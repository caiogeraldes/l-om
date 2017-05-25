import hk_dv, iast_dv, hk_iast, iast_hk, dv_hk, dv_iast, checktranslit


def conversor_texto(texto, tipo_entrada='Iast', tipo_saida="Devanagari"):
    """Recebe (str, str) ==> .txt """
    entrada = open("%s.txt" % texto, mode='r')
    linhas = entrada.readlines()
    saida = open("%s_saida.txt" % texto, mode="x")

    while tipo_entrada is None:
        print("O tipo de entrada é %s? [S/N]" % checktranslit.checker(entrada))
        resposta = input('>>>')
        if resposta == 'S' or resposta == 's':
            tipo_entrada = checktranslit.checker(entrada)
        elif resposta == 'N' or resposta == 'n':
            tipo_entrada = input("Digite o tipo de entrada[Devanagari/Iast/Harvard-kyoto:").capitalize()

    if tipo_entrada == 'Iast':
        if tipo_saida == "Devanagari":
            for linha in linhas:
                saida.write(iast_dv.conversor(linha) + '\n')
        if tipo_saida == 'Harvard-kyoto':
            for linha in linhas:
                saida.write(iast_hk.conversor(linha) + '\n')
    elif tipo_entrada == 'Harvard-kyoto':
        if tipo_saida == "Devanagari":
            for linha in linhas:
                saida.write(hk_dv.conversor(linha) + '\n')
        elif tipo_saida == "Iast":
            for linha in linhas:
                saida.write(hk_iast.conversor(linha) + '\n')
    elif tipo_entrada == 'Devanagari':
        if tipo_saida == "Iast":
            for linha in linhas:
                saida.write(dv_iast.conversor(linha) + '\n')
        elif tipo_saida == "Harvard-kyoto":
            for linha in linhas:
                saida.write(dv_hk.conversor(linha) + '\n')
    else:
        print("Método de entrada inválido.")

if __name__ == "__main__":
    conversor_texto("textos/teste")
