from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum

class ProductEnum(str, Enum):
    produto1 = "Smartphone"
    produto2 = "Laptop"
    produto3 = "Fones de Ouvido"

class Sales(BaseModel):
    """
    # Class Sales
    ## Representa uma venda realizada.

    Args:
        email (EmailStr): O e-mail do venderdor. Deve ser um endereço de e-mail válido.
        date (datetime): A data e hora em que a venda foi realizada.
        price (PositiveFloat): O preço do produto vendido. Deve ser um valor positivo.
        quantity (PositiveInt): A quantidade do produto vendida. Deve ser um inteiro positivo.
        product (ProductEnum): O produto vendido, representado por um enum.

    Exceções:
        Todos os campos são obrigatórios e devem atender aos tipos especificados.
    """
    email: EmailStr
    date: datetime
    price: PositiveFloat
    quantity: PositiveInt
    product: ProductEnum