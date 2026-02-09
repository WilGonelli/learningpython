from datetime import date # Importa a classe date do módulo datetime
from dateutil.relativedelta import relativedelta # Importa relativedelta para operações com datas (adicionar meses)
from sqlalchemy.orm import Session # Importa Session do SQLAlchemy para tipagem
from models.model import Bill as BillModel, BillInstance # Importa os modelos Bill e BillInstance
from schemas.schemas import BillBase # Importa o schema BillBase

class BillService: # Define a classe de serviço BillService
    
    def create_bill(self, bill: BillBase, db: Session): # Define o método create_bill recebendo dados da conta e sessão do banco
        # Converte o Schema (Pydantic) para Model (SQLAlchemy)
        print("teste", bill.final_date, bill.initial_date) # Imprime as datas para debug
        db_bill = BillModel( # Instancia o modelo BillModel com os dados recebidos
            name=bill.name, # Atribui o nome
            estimated_value=int(bill.estimated_value), # Atribui o valor estimado convertido para int
            initial_date=bill.initial_date, # Atribui a data inicial
            final_date=bill.final_date # Atribui a data final
        )
        
        db.add(db_bill) # Adiciona o objeto BillModel à sessão do banco
        db.commit() # Comita a transação para salvar no banco
        db.refresh(db_bill) # Atualiza o objeto com dados do banco (como ID gerado)
        
        # Cria instâncias automaticamente
        self.create_instances(db_bill, db) # Chama método para criar as instâncias mensais da conta
        
        return db_bill # Retorna o objeto BillModel criado

    def get_bills(self, db: Session, skip: int = 0, limit: int = 100): # Define método para listar contas com paginação
        return db.query(BillModel).offset(skip).limit(limit).all() # Retorna lista de contas aplicando offset e limit
    
    def create_instances(self, bill: BillModel, db: Session): # Define método auxiliar para criar instâncias mensais
        current_date = bill.initial_date # Inicializa data atual com a data inicial da conta
        
        # Garante que as datas estão no primeiro dia do mês para comparação
        start_date = date(current_date.year, current_date.month, 1) # Cria data normalizada para o dia 1 do mês inicial
        end_date = date(bill.final_date.year, bill.final_date.month, 1) # Cria data normalizada para o dia 1 do mês final
        
        while start_date <= end_date: # Loop enquanto a data atual for menor ou igual à data final
            instance = BillInstance( # Cria uma nova instância de BillInstance
                bill_id=bill.id, # Vincula ao ID da conta pai
                month_year=start_date, # Define o mês/ano de referência
                paid=False # Define como não pago inicialmente
            )
            db.add(instance) # Adiciona a instância à sessão
            start_date += relativedelta(months=1) # Avança para o próximo mês
        
        db.commit() # Comita as alterações (salva todas as instâncias)
        return # Retorna vazio
    
    def get_instances(self, db: Session, mounth_ref: date): # Define método para buscar instâncias por mês de referência
        print(mounth_ref) # Imprime o mês de referência para debug
        return db.query(BillInstance).where(BillInstance.month_year == mounth_ref).all() # Retorna todas as instâncias que coincidem com o mês fornecido