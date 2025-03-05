from UI.Console import Console
from Domain.validari import ValidareStudent, ValidareProblema, ValidareNotare
from Repository.memorie import StudentRepository, ProblemeRepository, NotareRepository
from Repository.in_fisier import StudentFisierRepository, ProblemaFisierRepository, NotareFisierRepository
from Service.controller import StudentController, ProblemaController, NotareController
from Teste.teste import Teste_operatiuni_student, Teste_operatiuni_problema, Teste_operatiuni_notare

def run():
    """
    Testeaza functionalitatea operatiunilor disponibile 
    si porneste consola de comanda
    """
    teste_stud = Teste_operatiuni_student()
    teste_stud.testare_op_stud()
    
    teste_problema = Teste_operatiuni_problema()
    teste_problema.testare_op_problema()
    
    teste_notare = Teste_operatiuni_notare()
    teste_notare.testare_op_notare()
    
    val_stud = ValidareStudent()
    #repo_stud = StudentRepository()
    repo_stud = StudentFisierRepository("studenti.txt")
    ctr_stud = StudentController(val_stud,repo_stud)
    
    val_probleme = ValidareProblema()
    #repo_probleme = ProblemeRepository()
    repo_probleme = ProblemaFisierRepository("probleme.txt")
    ctr_probleme = ProblemaController(val_probleme,repo_probleme)
    
    val_notare = ValidareNotare()
    #repo_notare = NotareRepository(repo_stud,repo_probleme)
    repo_notare= NotareFisierRepository("note.txt",repo_stud,repo_probleme)
    crt_notare = NotareController(repo_stud,repo_probleme,repo_notare,val_notare)
    
    app = Console(ctr_stud,ctr_probleme,crt_notare)
    app.run_code()

run()