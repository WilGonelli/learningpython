from datetime import date, datetime # Importa date e datetime do módulo datetime
from pydantic import BaseModel, field_validator, model_validator # Importa BaseModel e validadores do Pydantic

# Schema base com campos comuns para ler e criar
class BillBase(BaseModel): # Define a classe BillBase herdando de BaseModel do Pydantic
    name: str # Define o campo 'name' como string
    estimated_value: int # Define o campo 'estimated_value' como inteiro
    initial_date: date # Define o campo 'initial_date' como data
    final_date: date # Define o campo 'final_date' como data

    @field_validator('initial_date', 'final_date', mode='before') # Decorador para validador de campo, executado antes da validação padrão
    def parse_month_year(cls, v): # Função validadora que recebe o valor 'v'
        if isinstance(v, str): # Verifica se o valor é uma string
            try: # Tenta executar o bloco de código
                # Tenta converter mm/yyyy para o primeiro dia do mês
                return datetime.strptime(v, "%Y-%m-%d").date() # Tenta converter string formato AAAA-MM-DD para data
            except ValueError: # Captura erro de valor se a conversão falhar
                pass # Ignora o erro e tenta o próximo formato
            try: # Tenta executar o bloco de código
                return datetime.strptime(v, "%Y-%m").date() # Tenta converter string formato AAAA-MM para data
            except ValueError: # Captura erro de valor se a conversão falhar
                raise ValueError("Formato de data inválido. Use MM/YYYY") # Levanta erro indicando formato inválido
        return v # Retorna o valor original se não for string ou após conversão
    
    @model_validator(mode="after") # Decorador para validador de modelo, executado após a validação dos campos
    def check_date_order(cls, values): # Função validadora que recebe os valores do modelo
        if values.initial_date > values.final_date: # Verifica se a data inicial é maior que a data final
            raise ValueError("A data inicial deve ser anterior à data final") # Levanta erro se a ordem das datas estiver incorreta
        return values # Retorna os valores validados

# Schema para leitura (o que a API retorna, inclui o ID do banco)
class Bill(BillBase): # Define a classe Bill herdando de BillBase
    id: int # Define o campo 'id' como inteiro

    class Config: # Classe interna para configurações do Pydantic
        from_attributes = True # Permite criar o modelo a partir de atributos de objetos (ORM mode)

# schema para criar as instancias das contas
class BillInstanceSchema(BaseModel): # Define a classe BillInstanceSchema herdando de BaseModel
    id: int # Define o campo 'id' como inteiro
    bill_id: int # Define o campo 'bill_id' como inteiro
    month_year: date # Define o campo 'month_year' como data
    paid: bool # Define o campo 'paid' como booleano
    real_value: int | None # Define o campo 'real_value' como inteiro ou None (opcional)
    paid_date: date | None # Define o campo 'paid_date' como data ou None (opcional)

    class Config: # Classe interna para configurações do Pydantic
        from_attributes = True # Permite criar o modelo a partir de atributos de objetos (ORM mode)
