from livro import Livro

def main():

    # Instanciando o livro 1
    l1 = Livro()
    l1.titulo = "O Hobbit"
    l1.autor = "J. R. R. Tolkien"
    l1.preco = 39.9
    l1.quantidade = 8

    # Instanciando o livro 2
    l2 = Livro()
    l2.titulo = "Dom Casmurro"
    l2.autor = "Machado de Assis"
    l2.preco = 29.5
    l2.quantidade = 12

    # Instanciando o livro 3
    l3 = Livro()
    l3.titulo = "1984"
    l3.autor = "George Orwell"
    l3.preco = 34.0
    l3.quantidade = 6

    # Exibindo o resumo de cada um
    print("=== RESUMO DOS LIVROS ===")

    print(f"Título: {l1.titulo} | Autor: {l1.autor} | Preço: R$ {l1.preco} | Qtd: {l1.quantidade}")
    print(f"Título: {l2.titulo} | Autor: {l2.autor} | Preço: R$ {l2.preco} | Qtd: {l2.quantidade}")
    print(f"Título: {l3.titulo} | Autor: {l3.autor} | Preço: R$ {l3.preco} | Qtd: {l3.quantidade}")

if __name__ == "__main__":
    main()
