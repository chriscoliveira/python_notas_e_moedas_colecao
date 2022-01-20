import requests
cont = 0

with open('links.txt', 'w') as arquivo_saida:

    lista = [10, 11, 12, 13, 14, 16, 23, 34, 43, 46, 50, 56, 64, 111, 112, 114, 115, 116, 118, 131, 132, 134, 135, 136, 138, 146, 147, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166, 167, 168, 169, 170, 172, 173,
             174, 176, 178, 179, 180, 181, 182, 183, 185, 186, 187, 189, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 207, 208, 209, 210, 211, 213, 214, 215, 217, 218, 219, 220, 221, 223, 235, 239]

    for i in lista:
        arquivo_saida.write(
            f"UPDATE Colecao set imagem1='https://firebasestorage.googleapis.com/v0/b/minha-colecao-a01d5.appspot.com/o/imagens%2FBrasil_C{i}_anverso.jpg?alt=media&token=532b9ae4-1ebb-4492-9d37-0e5fd3442d70' where pais='Brasil' and krause='C {i}';\n")
        arquivo_saida.write(
            f"UPDATE Colecao set imagem2='https://firebasestorage.googleapis.com/v0/b/minha-colecao-a01d5.appspot.com/o/imagens%2FBrasil_C{i}_reverso.jpg?alt=media&token=532b9ae4-1ebb-4492-9d37-0e5fd3442d70' where pais='Brasil' and krause='C {i}';\n")
