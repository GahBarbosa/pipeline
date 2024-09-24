import streamlit as st  
from contract import Sales
from datetime import datetime, time
from pydantic import ValidationError 
from database import save_sale

def main():
  st.title("Sistema de CRM")
  email = st.text_input("Email do Vendedor")
  date = st.date_input("Data da Compra", datetime.now())
  hour = st.time_input("Hora da Compra")
  price = st.number_input("Valor da Venda", min_value=0.0, format="%.2f")
  quantity = st.number_input("Quantidade de Produtos", min_value=1, step=1)
  product = st.selectbox("Produto",["Smartphone", "Laptop", "Fones de Ouvido"])
  
  if st.button("Salvar"):
    try:

      date_hour = datetime.combine(date,hour)

      sale = Sales(
        email=email,
        date=date_hour,
        price=price,
        quantity=quantity,
        product=product
      )
      st.write(sale)
      save_sale(sale)
      
    except ValidationError as e:
      st.error(f"Erro na validação dos dados: {e}")
    except Exception as e:
      st.error(f"Erro ao salvar os dados: {e}")


if __name__=="__main__":
  main()