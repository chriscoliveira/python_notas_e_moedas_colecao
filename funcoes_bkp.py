import sqlite3


class Colecao:

    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, pais, ano, krause, valor, moeda, tipo, qualidade, material, diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2):
        sql = "INSERT INTO colecao (pais,ano,krause,valor,moeda,tipo,qualidade,material,diametro,detalhe,anverso,reverso,valor_venda,datacadastro,imagem1,imagem2) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        self.cursor.execute(sql, (pais, ano, krause, valor, moeda, tipo, qualidade, material,
                            diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2))
        self.conn.commit()

    def editar(self, id, pais, ano, krause, valor, moeda, tipo, qualidade, material, diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2):
        sql = "UPDATE colecao SET pais=?,ano=?,krause=?,valor=?,moeda=?,tipo=?,qualidade=?,material=?,diametro=?,detalhe=?,anverso=?,reverso=?,valor_venda=?,datacadastro=?,imagem1=?,imagem2=? WHERE id=?"
        self.cursor.execute(sql, (pais, ano, krause, valor, moeda, tipo, qualidade, material,
                            diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2, id))
        self.conn.commit()

    def remover(self, id):
        sql = "DELETE FROM colecao WHERE id=?"
        self.cursor.execute(sql, (id,))
        self.conn.commit()

    def listar_tudo(self):
        sql = "SELECT * FROM colecao"
        self.cursor.execute(sql)
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, termo):

        sql = "SELECT * FROM colecao WHERE pais LIKE ? OR ano LIKE ? OR valor LIKE ? OR moeda LIKE ? OR qualidade LIKE ? OR material LIKE ? OR anverso LIKE ? OR reverso LIKE ? "
        termo = f'%{termo}%'
        self.cursor.execute(
            sql, (termo, termo, termo, termo, termo, termo, termo, termo))

        for linha in self.cursor.fetchall():
            id = linha[0]
            pais = linha[1]
            ano = linha[2]
            krause = linha[3]
            valor = linha[4]
            moeda = linha[5]
            tipo = linha[6]
            qualidade = linha[7]
            material = linha[8]
            diametro = linha[9]
            detalhe = linha[10]
            anverso = linha[11]
            reverso = linha[12]
            valor_venda = linha[13]
            datacadastro = linha[14]
            imagem1 = linha[15]
            imagem2 = linha[16]

            print(f'>id: {id}\n>pais: {pais}\n>ano: {ano}\n>krause: {krause}\n>valor: {valor}\n>moeda: {moeda}\n>tipo: {tipo}\n>qualidade: {qualidade}\n>material: {material}\n>diametro: {diametro}\n>detalhe: {detalhe}\n>anverso: {anverso}\n>reverso: {reverso}\n>valor_venda: {valor_venda}\n>datacadastro: {datacadastro}\n>imagem1: {imagem1}\n>imagem2: {imagem2}\n')

    def criartabela(self):
        sql = 'CREATE TABLE IF NOT EXISTS "Colecao" ( "id" INTEGER NOT NULL, "pais" TEXT NOT NULL, "ano" TEXT NOT NULL, "krause" TEXT, "valor" TEXT NOT NULL, "moeda" TEXT NOT NULL, "tipo" TEXT NOT NULL, "qualidade" TEXT NOT NULL, "material" TEXT NOT NULL, "diametro" TEXT NOT NULL, "detalhe" TEXT, "anverso" TEXT, "reverso" TEXT, "valor_venda" TEXT, "datacadastro" TEXT, "imagem1" TEXT, "imagem2" TEXT, PRIMARY KEY("id" AUTOINCREMENT));'
        self.cursor.execute(sql)

    def importarTXT(self):
        with open('bancoMoedas.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                self.cursor.execute(linha)
                self.conn.commit()

    def fechar(self):
        self.conn.close()
        self.cursor.close()


if __name__ == "__main__":
    colecao = Colecao("colecao.db")
    colecao.criartabela()

    # colecao.inserir('Brasil', '2022', '1', '1', 'Real', 'Moeda', 'Comum', 'Madeira',
    #                '1', 'Madeira', 'Madeira', 'Madeira', 'Madeira', '1', '1', '1')
    # colecao.remover(1644)
    while True:
        print('1 - Inserir\n2 - Editar\n3 - Remover\n4 - Listar Tudo\n5 - Buscar\n6 - Sair')
        opcao = int(input('Digite a opção: '))
        if opcao == 1:
            pais = input('Digite o país: ')
            ano = input('Digite o ano: ')
            krause = input('Digite o krause: ')
            valor = input('Digite o valor: ')
            moeda = input('Digite a moeda: ')
            tipo = input('Digite o tipo: ')
            qualidade = input('Digite a qualidade: ')
            material = input('Digite o material: ')
            diametro = input('Digite o diametro: ')
            detalhe = input('Digite o detalhe: ')
            anverso = input('Digite o anverso: ')
            reverso = input('Digite o reverso: ')
            valor_venda = input('Digite o valor de venda: ')
            datacadastro = input('Digite a data de cadastro: ')
            imagem1 = input('Digite a imagem 1: ')
            imagem2 = input('Digite a imagem 2: ')
            colecao.inserir(pais, ano, krause, valor, moeda, tipo, qualidade, material,
                            diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2)
        elif opcao == 2:
            id = int(input('Digite o id: '))
            pais = input('Digite o país: ')
            ano = input('Digite o ano: ')
            krause = input('Digite o krause: ')
            valor = input('Digite o valor: ')
            moeda = input('Digite a moeda: ')
            tipo = input('Digite o tipo: ')
            qualidade = input('Digite a qualidade: ')
            material = input('Digite o material: ')
            diametro = input('Digite o diametro: ')
            detalhe = input('Digite o detalhe: ')
            anverso = input('Digite o anverso: ')
            reverso = input('Digite o reverso: ')
            valor_venda = input('Digite o valor de venda: ')
            datacadastro = input('Digite a data de cadastro: ')
            imagem1 = input('Digite a imagem 1: ')
            imagem2 = input('Digite a imagem 2: ')
            colecao.editar(id, pais, ano, krause, valor, moeda, tipo, qualidade, material,
                           diametro, detalhe, anverso, reverso, valor_venda, datacadastro, imagem1, imagem2)
        elif opcao == 3:
            id = int(input('Digite o id: '))
            colecao.remover(id)
        elif opcao == 4:
            colecao.listar_tudo()
        elif opcao == 5:
            termo = input('Digite o termo a ser localizado: ')
            colecao.buscar(termo)
        elif opcao == 6:
            break
