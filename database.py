import psycopg2
from psycopg2 import sql
from contract import Sales
import streamlit as st
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Configuração do banco de dados PostgreSQL
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Função para salvar os dados validados no PostgreSQL
def save_sale(sale: Sales):
    """
    # save_sale 
    ## Salva uma venda no banco de dados.

    Args:
        sale (Sales): A instância da classe Sales a ser salva. Todos os campos devem ser preenchidos
                       corretamente de acordo com as restrições definidas na classe Sales.

    Raises:
        DatabaseError: Se ocorrer um erro ao tentar salvar a venda no banco de dados.
        ValidationError: Se a venda não atender às regras de validação definidas.

    Examples:
        ```python
        sale = Sales(email="exemplo@dominio.com", date=datetime.now(), price=29.99, quantity=1, product=ProductEnum.PRODUTO_A)
        save_sale(sale)
        ```
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        
        # Inserção dos dados na tabela de vendas
        insert_query = sql.SQL(
            "INSERT INTO sales (email, date, price, quantity, product) VALUES (%s, %s, %s, %s, %s)"
        )
        cursor.execute(insert_query, (
            sale.email,
            sale.date,
            sale.price,
            sale.quantity,
            sale.product.value
        ))
        conn.commit()
        cursor.close()
        conn.close()
        st.success("Venda salvos com sucesso no banco de dados!")
    except Exception as e:
        st.error(f"Erro ao salvar no banco de dados: {e}")