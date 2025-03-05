from Domain.entities import Student, Problema, Notare
from Service.controller import StudentController, ProblemaController, NotareController
from Domain.validari import EroareValidareStudent, EroareIntrareID
from Domain.validari import EroareValidareProblema, EroareIntrareNr_lab
from Domain.validari import EroareValidareNota
from Repository.memorie import EroareDepozitareStudent, EroareIDInexistent
from Repository.memorie import EroareDepozitareProblema, EroareNr_labInexistent
from Repository.memorie import EroareProblemaDejaNotata

class Console():
    def __init__(self,ctr_stud,ctr_problema,crt_notare):
        self.__ctr_stud = ctr_stud
        self.__ctr_problema = ctr_problema
        self.__ctr_notare = crt_notare
        
    def __print_meniu(self):
        """
        Afiseaza meniul principal
        """
        print("Meniu: ") 
        print(" lista_studenti -> Afisare Lista Studenti")
        print(" add_student -> Adaugare Student")
        print(" stergere_student -> Stergere Student")
        print(" cautare_student -> Cautare Student")
        print(" modificare_student -> Modificare Student")
        print(" lista_probleme -> Afisare Lista Probleme")
        print(" add_problema -> Adauagre Problema")
        print(" stergere_problema -> Stergere Problema")
        print(" cautare_problema -> Cautare Problema")
        print(" modificare_problema -> Modificare Problema")
        print(" add_stud_random -> Adaugare studenti random")
        print(" add_problema_random -> Adaugare problema random")
        print(" asignare_problema -> Asignare Problema")
        print(" lista_studenti_dupa_lab_dat -> Lista studenti dupa lab dat")
        print(" lista_studenti_medie_lab_sub_5 -> Lista studentilor cu media notelor de la laborator sub 5")
        print(" lista_studenti_10procent_dupa_lab_dat -> Primi 10 la suta studenti ordonati descrescator dupa nota pentru un laborator")
        
    def _print_lista_studenti(self):
        """
        Afiseaza lista de studenti
        """
        lista_studenti = self.__ctr_stud.get_studenti()
        for student in lista_studenti:
            print(student.get_student_info())

    def __ui_adaugare_student(self):
        """
        Efectueaza operatia de adaugare student
        in lista de studenti
        """
        ID = input("ID-ul studentului este : ").strip()
        nume = input("Numele studentului este : ").strip()
        grupa = input("Grupa studentului este : ").strip()
        try:
            self.__ctr_stud.creaza(ID,nume,grupa)
        except EroareValidareStudent as msg:
            print(msg)
        except EroareDepozitareStudent as msg:
            print(msg)
          
    def __ui_stergere_student(self):
        """
        Efectueaza operatia de stergere student 
        din lista de studenti
        """
        ID = input("Introduceti ID-ul studentului : ").strip()
        try:
            self.__ctr_stud.stergere(ID)
        except EroareIntrareID as msg:
            print(msg)
        except EroareIDInexistent as msg:
            print(msg)
    
    def __ui_cautare_student(self):
        """
        Efectueaza operatia de cautare student 
        din lista de studenti
        """
        ID = input("Introduceti ID-ul studentului : ").strip()
        try:
            student = self.__ctr_stud.cautare(ID)
            print(student.get_student_info())
        except EroareIDInexistent as msg:
            print(msg)
        except EroareIntrareID as msg:
            print(msg)
    
    def __ui_modificare_student(self):
        """
        Efectueaza operatia de modificare student
        din lista de studenti
        """
        ID = input("ID-ul studentului este : ").strip()
        nume = input("Numele studentului este : ").strip()
        grupa = input("Grupa studentului este : ").strip()
        try:
            self.__ctr_stud.modificare(ID,nume,grupa)
        except EroareValidareStudent as msg:
            print(msg)
        except EroareDepozitareStudent as msg:
            print(msg)
        except EroareIDInexistent as msg:
            print(msg)
            
    def _print_lista_probleme(self):
        """
        Afiseaza lista de probleme
        """
        lista_probleme = self.__ctr_problema.get_probleme()
        for problema in lista_probleme:
            print(problema.get_problem_info())
            
    def __ui_adaugare_problema(self):
        """
        Efectueaza operatia de adaugare problema
        in lista de probleme
        """
        nr_lab = input("Introdu numarul laboratorului : ").strip()
        descriere = input("Introdu descrierea problemei : ").strip()
        deadline = input("Introdu deadline-ul problemei : ").strip()
        try:
            self.__ctr_problema.creaza(nr_lab,descriere,deadline)
        except EroareValidareProblema as msg:
            print(msg)
        except EroareDepozitareProblema as msg:
            print(msg)
            
    def __ui_stergere_problema(self):
        """
        Efectueaza operatia de stergere problema
        din lista de probleme
        """
        nr_lab = input("Introduceti numarul de laborator : ").strip()
        try:
            self.__ctr_problema.stergere(nr_lab)
        except EroareIntrareNr_lab as msg:
            print(msg)
        except EroareNr_labInexistent as msg:
            print(msg)
            
    def __ui_cautare_problema(self):
        """
        Efectueaza operatia de cautare problema
        din lista de probleme
        """
        nr_lab = input("Introduceti numarul de laborator : ").strip()
        try:
            student = self.__ctr_problema.cautare(nr_lab)
            print(student.get_problem_info())
        except EroareNr_labInexistent as msg:
            print(msg)
        except EroareIntrareNr_lab as msg:
            print(msg)
    
    def __ui_modificare_problema(self):
        """
        Efectueaza operatia de modificare problema
        in lista de probleme
        """
        nr_lab = input("Introdu numarul laboratorului : ").strip()
        descriere = input("Introdu descrierea problemei : ").strip()
        deadline = input("Introdu deadline-ul problemei : ").strip()
        try:
            self.__ctr_problema.modificare(nr_lab,descriere,deadline)
        except EroareValidareProblema as msg:
            print(msg)
        except EroareDepozitareProblema as msg:
            print(msg)
    
    def __ui_adaugare_student_random(self):
        """
        Efectueaza operatia de adaugare a unor studenti cu date random
        """
        nr_stud = int(input("Cati studenti doriti sa generati ?: ").strip())
        self.__ctr_stud.adaugare_random(nr_stud)

    def __ui_adaugare_problema_random(self):
        """
        Efectueaza operatia de adaugare a unor probleme cu date random
        """
        nr_probleme = int(input("Cate probleme doriti sa generati ?: ").strip())
        self.__ctr_problema.adaugare_random(nr_probleme)
    
    def __ui_asignare_problema(self):
        """
        Efectueaza operatia de notare a unei probleme pentru un student
        """
        ID_student = input("Introduceti ID-ul studentului : ").strip()
        nr_lab = input("Introduceti numarul de laborator : ").strip()
        try:
            nota = float(input("Introduceti nota : ").strip())
        except ValueError:
            print("Nota trebuie sa contina doar cifre")
        try:
            self.__ctr_notare.asignare(ID_student,nr_lab,nota)
        except EroareIDInexistent as msg:
            print(msg)
        except EroareNr_labInexistent as msg:
            print(msg)
        except EroareValidareNota as msg:
            print(msg)
        except EroareProblemaDejaNotata as msg:
            print(msg)
            
    def __ui_lista_studenti_dupa_lab_dat(self):
        """
        Afiseaza pe ecran lista de studenti dupa un laborator dat
        intr-o ordine ceruta de program
        """
        nr_lab = input("Introduceti numarul de laborator : ").strip()
        try:
            lista_studenti = self.__ctr_notare.get_lista_studenti_si_notele_lab_dat(nr_lab)
            lista_pr = []
            for student in lista_studenti:
                id_student = student.getStudent().get_ID()
                nume_student = student.getStudent().get_nume()
                nota_student = student.getNota()
                lista_pr.append([id_student,nume_student,nota_student])
                
            if len(lista_studenti) == 0:
                print("Nu exista studenti cu laboratorulul specificat asignat")
            else :
                print("Introduceti ordinea afisarii listei : ")
                print(" alfabetic_dupa_nume -> alfabetic dupa nume ")
                print(" alfabetic_dupa_nota -> alfabetic dupa nota")
                ans = input()
                if ans == "alfabetic_dupa_nume":
                    #cu functia sort()
                    """
                    lista_studenti.sort(key = lambda note: note.getStudent().get_nume())
                    print("ID-ul, numele si nota studentului : ")
                    for note in lista_studenti:
                        student = note.getStudent()
                        nota = note.getNota()
                        print(f'{student.get_ID()} {student.get_nume()} {nota}')
                    """
                    #cu functia creata
                    lista_noua = self.__ctr_stud.sortare_dupa_2_criterii(lista_pr,1,1)
                    print("ID-ul, numele si nota studentului : ")
                    for note in lista_noua:
                        print(f'{note[0]} {note[1]} {note[2]}')
                elif ans == "alfabetic_dupa_nota":
                    #cu functia sort()
                    """
                    lista_studenti.sort(key = lambda note: note.getNota())
                    print("ID-ul, numele si nota studentului : ")
                    for note in lista_studenti:
                        student = note.getStudent()
                        nota = note.getNota()
                        print(f'{student.get_ID()} {student.get_nume()} {nota}')
                    """
                    #cu functia creata
                    lista_noua = self.__ctr_stud.sortare(lista_pr,2,2)
                    print("ID-ul, numele si nota studentului : ")
                    for note in lista_noua:
                        print(f'{note[0]} {note[1]} {note[2]}')
                else: print("Comanda invalida")
        except EroareNr_labInexistent as msg:
            print(msg)
    
    def __ui_lista_studenti_medie_lab_sub_5(self):
        """
        Afiseaza pe ecran lista de studenti cu media notelor de laborator
        sub 5
        """
        lista_studenti_restantieri = self.__ctr_notare.get_lista_studenti_media_lab_sub_5()
        if len(lista_studenti_restantieri) == 0:
            print("Nu exista studenti cu media notelor de laborator sub 5 ")
        else:
            print("Numele studentului si nota : ")
            for student in lista_studenti_restantieri:
                print(student)
    
    def __ui_lista_studenti_10procent_dupa_lab_dat(self):
        nr_lab = input("Introduceti numarul laboratorului: ")
        try:
            lista_studenti = self.__ctr_notare.get_lista_studenti_10procent_dupa_lab_dat(nr_lab)
            print("ID-ul, numele si nota studentului : ")
            for note in lista_studenti:
                student = note.getStudent()
                nota = note.getNota()
                print(f'{student.get_ID()} {student.get_nume()} {nota}')
        except EroareNr_labInexistent as msg:
            print(msg)
            
    def __ui_alta_operatie(self):
        """
        Intreaba ultizatorul daca mai doreste sa
        mai faca o operatie
        """
        while True:
            ans = input("Doriti sa mai efectuati o operatie ? (da/nu) : ").strip()
            if ans == "da":
                break
            elif ans == "nu":
                exit()
            else: print("Comanda invalida")
            
    def run_code(self):
        """
        Consola de comanda
        """
        while True:
            self.__print_meniu()
            ans = input().strip()
            if ans == "lista_studenti":
                self._print_lista_studenti()
            elif ans == "add_student":
                self.__ui_adaugare_student()
            elif ans == "stergere_student":
                self.__ui_stergere_student()
            elif ans == "cautare_student":
                self.__ui_cautare_student()
            elif ans == "modificare_student":
                self.__ui_modificare_student()
            elif ans == "lista_probleme":
                self._print_lista_probleme()
            elif ans == "add_problema":
                self.__ui_adaugare_problema()
            elif ans == "stergere_problema":
                self.__ui_stergere_problema()
            elif ans == "cautare_problema":
                self.__ui_cautare_problema()
            elif ans == "modificare_problema":
                self.__ui_modificare_problema()
            elif ans == "add_stud_random":
                self.__ui_adaugare_student_random()
            elif ans == "add_problema_random":
                self.__ui_adaugare_problema_random()
            elif ans == "asignare_problema":
                self.__ui_asignare_problema()
            elif ans == "lista_studenti_dupa_lab_dat":
                self.__ui_lista_studenti_dupa_lab_dat()
            elif ans == "lista_studenti_medie_lab_sub_5":
                self.__ui_lista_studenti_medie_lab_sub_5()
            elif ans == "lista_studenti_10procent_dupa_lab_dat":
                self.__ui_lista_studenti_10procent_dupa_lab_dat()
            else: print("Comanda invalida")
            self.__ui_alta_operatie()   
            
                
                    
                      
                    