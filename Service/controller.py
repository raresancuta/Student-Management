from Domain.entities import Student
from Domain.entities import Problema
from Domain.entities import Notare
from Domain.validari import ValidareStudent
from Domain.validari import ValidareProblema
from Domain.validari import EroareValidareStudent
from Domain.validari import EroareValidareProblema
from Repository.memorie import StudentRepository
from Repository.memorie import EroareDepozitareStudent
from Repository.memorie import EroareDepozitareProblema
from Repository.memorie import ProblemeRepository
from Repository.memorie import EroareIDInexistent
import random 
import string
class StudentController():
    """
    Efectueaza operatiunile disponibile pentru gestionarea
    listei de studenti
    """
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo
        
    def get_studenti(self):
        """
        Returneaza lista de studenti din Repository
        """
        return self.__repo.lista_studenti
    
    def creaza(self, ID, nume, grupa):
        """
        Incearca adaugarea unui student nou in lista de studenti
        iar daca adaugarea nu are loc sunt aruncate exceptii
        si erorile aparute
        ID , nume, grupa - string-uri
        """
        self.__val.validare_stud(ID, nume, grupa)
        self.__repo.adauga_student(ID,nume,grupa)
        
    def stergere(self,ID):
        """
        Incearca stergerea unui student din lista de studenti
        iar daca stergerea nu are loc sunt aruncate exceptii
        si erorile aparute
        ID  - string
        """
        self.__val.validare_ID(ID)
        self.__repo.stergere_student(ID)
    
    def cautare(self,ID):
        """
        Incearca cautarea unui student din lista de studenti
        iar daca nu are loc sunt aruncate exceptii
        si erorile aparute
        ID  - string
        """
        self.__val.validare_ID(ID)
        #interativ
        #return self.__repo.cautare_student(ID)
        #recursiv
        return self.__repo.cautare_student_recursiv(0,ID)
    
    def modificare(self,ID,nume,grupa):
        """
        Incearca modificarea unui student cu un ID specificat
        de utlizator, iar daca modificarea nu a avut loc 
        sunt aruncate exceptii si erorile aparute
        ID, nume, grupa - string
        """
        self.__val.validare_stud(ID, nume, grupa)
        #iterativ
        #self.__repo.modificare_student(ID,nume,grupa)
        #recursiv
        self.__repo.modificare_student_recursiv(0,ID,nume,grupa)
    
    def adaugare_random(self,nr_stud):
        """
        Adauga un numar de studenti cu date random
        in lista de stundeti
        nr_stud - int
        """
        cate = 0
        while  cate < nr_stud:
            try:
                id_random = f'{random.randint(0,9)*100 + random.randint(0,9)*10 + random.randint(0,9)}'
                litere = string.ascii_letters
                nume_nou = ''.join(random.choice(litere) for i in range(10))
                grupa = f'{random.randint(0,10)}'
                self.__val.validare_stud(id_random,nume_nou,grupa)
                self.__repo.adauga_student(id_random,nume_nou,grupa)
                cate += 1
            except EroareDepozitareStudent:
                pass
            except EroareValidareStudent:
                pass
    
    def sortare(self,lista,criteriu,ord):
        """
        Realizeaza sortarea in ordine crescatoare a unei
        liste dupa un criteriu
        """
        len1 = len(lista)
        #quick_sort
        self.__repo.quick_sort(0,len1-1,lista,criteriu,ord)
        #gnome_sort
        #self.__repo.gnome_sort(len1,lista,criteriu,ord)
        return lista
    
    def sortare_dupa_2_criterii(self,lista,criteriu1,criteriu2,ord):
        self.sortare(lista,criteriu1,ord)
        for i in range(0,len(lista)):
            for j in range(i+1,len(lista)):
                if lista[i][criteriu1] == lista[j][criteriu1]:
                    if ord == 1:
                        if lista[i][criteriu2] > lista[j][criteriu2]:
                            aux = lista[i]
                            lista[i] = lista[j]
                            lista[j] = aux
                    else:
                        if lista[i][criteriu2] < lista[j][criteriu2]:
                            aux = lista[i]
                            lista[i] = lista[j]
                            lista[j] = aux
        return lista
    
class ProblemaController():
    """
    Efectueaza operatiunile disponibile pentru gestionarea
    listei de probleme
    """
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo
    
    def get_probleme(self):
        """
        Returneaza lista de probleme din Repository
        """
        return self.__repo.lista_probleme
    
    def creaza(self, nr_lab, descriere, deadline):
        """
        Incearca adaugarea unei probleme in lista de probleme
        iar daca adaugarea nu are loc sunt aruncate exceptii
        si erorile aparute
        nr_lab , descriere, deadline - string-uri
        """
        self.__val.validare_problema(nr_lab, descriere, deadline)
        self.__repo.adauga_problema(nr_lab, descriere, deadline)
        
    def stergere(self,nr_lab):
        """
        Incearca stergerea unei probleme din lista de probleme
        iar daca stergerea nu are loc sunt aruncate exceptii
        si erorile aparute
        nr_lab  - string
        """
        self.__val.validare_nr_lab(nr_lab)
        self.__repo.stergere_problema(nr_lab)
    
    def cautare(self,nr_lab):
        """
        Incearca cautare unei probleme din lista de probleme
        iar daca cautarea nu are loc sunt aruncate exceptii
        si erorile aparute
        nr_lab  - string
        """
        self.__val.validare_nr_lab(nr_lab)
        return self.__repo.cautare_problema(nr_lab)
    
    def modificare(self,nr_lab,descriere,deadline):
        """
        Incearca modificarea unei probleme cu numarul de 
        laborator asignat specificat de utilizator, iar daca
        modificarea nu a avut loc sunt aruncate exceptii si
        erorile corespunzatoare
        """
        self.__val.validare_problema(nr_lab, descriere, deadline)
        self.__repo.modificare_problema(nr_lab, descriere, deadline)
        
    def adaugare_random(self,nr_probleme):
        """
        Adauga un numar de probleme cu date random in
        lista de probleme
        """
        cate = 0
        while cate < nr_probleme:
            nr_lab = f'{random.randint(1,30)}'
            litere = string.ascii_letters
            descriere = ''.join(random.choice(litere) for i in range(10))
            deadline = f'{random.randint(1,9)}{random.randint(0,9)}.{random.randint(0,1)}{random.randint(0,9)}.{random.randint(2023,2024)}'
            try:
                self.__val.validare_problema(nr_lab,descriere,deadline)
                self.__repo.adauga_problema(nr_lab,descriere,deadline)
                cate += 1
            except EroareValidareProblema:
                pass
            except EroareDepozitareProblema:
                pass
                
class NotareController():
    """
    Efectueaza operatiunile disponibile pentru gestionarea
    listei de notari
    """
    def __init__(self,repo_stud,repo_probl,repo_notare,val_notare):
        self.__repo_stud = repo_stud
        self.__repo_probl = repo_probl
        self.__repo_notare = repo_notare
        self.__val_nota = val_notare
        
    def asignare(self,ID,nr_lab,nota):
        """
        Incearca asignarea unei note de laborator unui student
        ID, nr_lab - string
        nota - int
        """
        student = self.__repo_stud.cautare_student(ID)
        problema = self.__repo_probl.cautare_problema(nr_lab)
        self.__val_nota.validare_nota(nota)
        self.__repo_notare.stocare_notare(Notare(student,problema,nota))
    
    def get_lista_studenti_si_notele_lab_dat(self,nr_lab):
        """
        Returneaza lista de studenti si notele aferente laboratoarelor
        dupa un numar de laborator dat
        nr_lab - string
        """
        problema = self.__repo_probl.cautare_problema(nr_lab)
        lista_studenti_si_note = self.__repo_notare.get_studenti_dupa_nr_lab_asignat(nr_lab)
        return lista_studenti_si_note

    def get_lista_studenti_media_lab_sub_5(self):
        """
        Returneaza lista de studenti a caror medie de laboratoare
        este sub 5
        """
        return self.__repo_notare.get_lista_studenti_media_lab_sub_5()
        
    def get_lista_studenti_10procent_dupa_lab_dat(self,nr_lab):
        lista_studenti_10_procent = []
        problema = self.__repo_probl.cautare_problema(nr_lab)
        lista_studenti = self.__repo_notare.get_studenti_dupa_nr_lab_asignat(nr_lab)
        lista_pr = []
        for student in lista_studenti:
                id_student = student.getStudent().get_ID()
                nume_student = student.getStudent().get_nume()
                nota_student = student.getNota()
                lista_pr.append([id_student,nume_student,nota_student])      
        lista_studenti.sort(key = lambda note: (-note.getNota(),note.getStudent().get_nume()))
        _10_procent = 0.5 * len(lista_studenti)
        cate = 0
        for student in lista_studenti:
            if cate < _10_procent:
                lista_studenti_10_procent.append(student)
                cate += 1
        return lista_studenti_10_procent
            
            
    
    