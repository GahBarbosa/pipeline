from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum

class ProductEnum(str, Enum):
    produto1 = "Smartphone"
    produto2 = "Laptop"
    produto3 = "Fones de Ouvido"

class Sales(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        produto (PositiveInt): nome do produto
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto
    """
    email: EmailStr
    date: datetime
    price: PositiveFloat
    quantity: PositiveInt
    product: ProductEnum