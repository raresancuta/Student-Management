from Domain.entities import TestareStudent
from Domain.entities import TestareProblema
from Domain.entities import TestareNota
from Repository.memorie import VerificareStudent
from Repository.memorie import VerificareProblema
from Repository.memorie import VerificareNotare
from Repository.in_fisier import VerificareStudentInFisier,VerificareProblemaInFisier, VerificareNotareInFisier

class Teste_operatiuni_student():
    """
    Efectueaza testarea tuturor functionalitatilor
    in ceea ce priveste studentii si lista de studenti
    """
    def testare_op_stud(self):
        TestareStudent().testareStudent()
        VerificareStudent().test_adaugare_student()
        VerificareStudent().test_stergere_student()
        VerificareStudent().test_cautare_student()
        VerificareStudent().test_modificare_student()
        VerificareStudentInFisier().testare_stocare_student()
        
class Teste_operatiuni_problema():
    """
    Efectueaza testarea tuturor functionalitatilor
    in ceea ce priveste problemele si lista de probleme
    """
    def testare_op_problema(self):
        TestareProblema().testareProblema()
        VerificareProblema().test_adaugare_problema()
        VerificareProblema().test_stergere_problema()
        VerificareProblema().test_cautare_probelma()
        VerificareProblema().test_modificare_problema()
        VerificareProblemaInFisier().testare_stocare_problema()
        
class Teste_operatiuni_notare():
    """
    Efectueaza testarea tuturor functionalitatilor
    in ceea ce priveste notarile si lista de notari
    """
    def testare_op_notare(self):
        TestareNota().testare_nota()
        VerificareNotare().testare_stocare_notare()
        VerificareNotare().testare_lista_studenti_dupa_lab_asignat()
        VerificareNotare().testare_note_dupa_ID_student()
        VerificareNotare().testare_lista_studenti_media_lab_sub_5()
        VerificareNotareInFisier().testare_stocare_notare()