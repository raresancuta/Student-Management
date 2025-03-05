from Domain.entities import Student, Problema, Notare
from Domain.validari import EroareStudent, EroareProblema, EroareNotare

class EroareDepozitareStudent(EroareStudent):
    """
    Exceptie speciala in cazul in care
    apare o eroare de depozitare a unui student
    """
    def __init__(self, msg):
        self.__msg = msg
    
    def get_msg(self):
        return self.__msg
    
class EroareIDInexistent(EroareStudent):
    """
    Exceptie speciala in cazul in care nu exista
    niciun student din lista de studenti cu ID-ul 
    dat de utlizator
    """
    def __init__(self,msg):
        self.__msg = msg
    
    def get_msg(self):
        return self.__msg
    
class EroareDepozitareProblema(EroareProblema):
    """
    Eroare speciala in cazul in care apare 
    o eroare la depozitarea unei probleme 
    in lista de probleme
    """
    def __init__(self, msg):
        self.__msg = msg
    
    def get_msg(self):
        return self.__msg
    
class EroareNr_labInexistent(EroareProblema):
    """ 
    Eroare speciala in cazul in care nu exista
    nicio prolema in lista de probleme cu
    numarul de laborator specificat de utilizator
    """
    def __init__(self, msg):
        self.__msg = msg
    
    def get_msg(self):
        return self.__msg  

class EroareProblemaDejaNotata(EroareNotare):
    """
    Eroare speciala in cazul in care notarea unei probleme
    asignate unui student a fost deja facuta
    """
    def __init__(self, msg):
        self.__msg = msg
    
    def get_msg(self):
        return self.__msg    
    
class StudentRepository():
    """
    Gestioneaza studentii din lista de studenti 
    """
    def __init__(self):
        self.lista_studenti = []
        
    def get_list_size(self):
        """
        Returneaza numarul de studenti din
        lista de studenti din memorie
        """
        return len(self.lista_studenti)
    
    def get_list(self):
        """
        Returneaza lista de studenti din memorie
        """
        return self.lista_studenti
    
    def adauga_student(self, ID, nume, grupa):
        """
        Daca nu exista niciun student cu ID-ul specificat
        se introduce studentul cu numar de ID, nume si grupa
        in lista de studenti, in caz contrar este aruncata o exceptie
        speciala pentru acest caz
        ID, nume, grupa - string
        """
        student = Student(ID, nume, grupa)
        for studenti in self.lista_studenti:
            if studenti.get_ID() == ID:
                raise EroareDepozitareStudent("Studentul exista deja in memorie")
        self.lista_studenti.append(student)
    
    def stergere_student(self,ID):
        """
        Daca exista un student cu ID-ul specificat este sters din
        lista de studenti, in caz contrar este o arucata o exceptie
        speciala pentru acest caz
        ID- string
        """
        len1 = len(self.lista_studenti)
        count = 0
        for i in range(0,len(self.lista_studenti)):
            if self.lista_studenti[i].get_ID() == ID:
                self.lista_studenti.pop(i)
                break
            else: count += 1
        if count == len1:
            raise EroareIDInexistent("ID-ul nu exista in memorie")
    
    def cautare_student(self,ID):
        """
        Daca exista un student cu ID-ul specificat este returnat,
        in caz contrar este o arucata o exceptie speciala pentru acest caz
        ID- string
        """
        for i in range(0,len(self.lista_studenti)):
            if self.lista_studenti[i].get_ID() == ID:
                return self.lista_studenti[i]
        raise EroareIDInexistent("ID-ul nu exista in memorie")
        
    def cautare_student_recursiv(self,i,ID):
        """
        Daca exista un student cu ID-ul specificat este returnat,
        in caz contrar este o arucata o exceptie speciala pentru acest caz
        ID- string
        """
        if i < len(self.lista_studenti):
            if self.lista_studenti[i].get_ID() == ID:
                return self.lista_studenti[i]
            else: self.cautare_student_recursiv(i+1,ID)
        else: raise EroareIDInexistent("ID-ul nu exista in memorie")
        
    def modificare_student(self,ID,nume,grupa):
        """
        Daca exista un student cu ID-ul specificat este modificat
        cu noile informatii ( ID, nume, grupa ), in caz contrar este
        aruncata o exceptie speciala pentru acest caz
        ID, nume, grupa - string
        """
        len1 = len(self.lista_studenti)
        count = 0
        for i in range(0,len1):
            if self.lista_studenti[i].get_ID() == ID:
                self.lista_studenti[i].modif_ID(ID)
                self.lista_studenti[i].modif_nume(nume)
                self.lista_studenti[i].modif_grupa(grupa) 
            else: count += 1
        if count == len1:
            raise EroareIDInexistent("ID-ul nu exista in memorie")
    
    def modificare_student_recursiv(self,i,ID,nume,grupa):
        """
        Daca exista un student cu ID-ul specificat este modificat
        cu noile informatii ( ID, nume, grupa ), in caz contrar este
        aruncata o exceptie speciala pentru acest caz
        ID, nume, grupa - string
        """
        if i < len(self.lista_studenti):
            if self.lista_studenti[i].get_ID() == ID:
                self.lista_studenti[i].modif_ID(ID)
                self.lista_studenti[i].modif_nume(nume)
                self.lista_studenti[i].modif_grupa(grupa) 
            else : self.modificare_student_recursiv(i+1,ID,nume,grupa)
        else : raise EroareIDInexistent("ID-ul nu exista in memorie")
    
    def quick_sort(self,st,dr,lista,criteriu,ord):
        """
        Realizeaza prin metoda divide et impera
        sortarea in ordine crescatoare a unei liste dupa un
        anumit criteriu al listei
        st,dr,criteriu - int
        lista - lista
        """
        if st < dr:
            j = self.pivot(st,dr,lista,criteriu,ord)
            self.quick_sort(st,j-1,lista,criteriu,ord)
            self.quick_sort(j+1,dr,lista,criteriu,ord)
    
    def pivot(self,st,dr,lista,criteriu,ord):
        """
        Se obtine asezarea pivotului astfel incat toate elementele
        din stanga lui sa fie mai mici ca el iar elementele din dreapta
        lui sa fie mai mari ce el
        st,dr,criteriu - int
        lista - lista
        """
        pivot = lista[dr]
        i = st - 1
        for j in range(st,dr+1):
            if ord == 1:
                if lista[j][criteriu] < pivot[criteriu]:
                    i += 1
                    aux = lista[j]
                    lista[j] = lista[i]
                    lista[i] = aux
            else: 
                if lista[j][criteriu] > pivot[criteriu]:
                    i += 1
                    aux = lista[j]
                    lista[j] = lista[i]
                    lista[i] = aux  
        aux = lista[i+1]
        lista[i+1] = lista[j]
        lista[j] = aux
        return (i+1)
    
    def gnome_sort(self,len,lista,criteriu,ord):
        """
        Realizeaza prin metoda Gnome Sort sortarea 
        in ordine crescatoare a unui sir dupa un anumit
        criteriu din sir
        len,criteriu - int
        lista - lista
        """
        index = 0
        while index < len:
            if index == 0:
                index += 1
            if ord == 1:
                if lista[index][criteriu] >= lista[index-1][criteriu]:
                    index +=1
                else:
                    aux = lista[index]
                    lista[index]= lista[index-1]
                    lista[index-1] = aux
                    index -= 1
            else: 
                if lista[index][criteriu] >= lista[index-1][criteriu]:
                    index +=1
                else:
                    aux = lista[index]
                    lista[index]= lista[index-1]
                    lista[index-1] = aux
                    index -= 1
    
class ProblemeRepository():
    """
    Gestioneaza problemele lista de probleme
    """
    def __init__(self):
        self.lista_probleme = []
    
    def get_list_size(self):
        """
        Returneaza numarul de probleme din lista de probleme
        """
        return len(self.lista_probleme)
    
    def get_list(self):
        """
        Returneaza problemele din lista de probleme
        """
        return self.lista_probleme
    
    def adauga_problema(self,nr_lab,descriere,deadline):
        """
        Daca nu exista nicio problema cu numarul de laborator specificat
        se introduce problema cu numarul de laborator, nume si grupa
        in lista de probleme, in caz contrar este aruncata o exceptie
        speciala pentru acest caz
        nr_lab, descriere, deadline - string
        """
        problema = Problema(nr_lab,descriere,deadline)
        for probleme in self.lista_probleme:
            if problema.get_nr_lab() == probleme.get_nr_lab():
                raise EroareDepozitareProblema("Problema deja exista in memorie")
        self.lista_probleme.append(problema)
    
    def stergere_problema(self,nr_lab):
        """
        Daca exista problema cu numarul de laborator specificat este stearsa
        din lista de probleme, in caz contrar este o arucata o exceptie
        speciala pentru acest caz
        nr_lab - string
        """
        len1 = len(self.lista_probleme)
        count = 0
        for i in range(0,len(self.lista_probleme)):
            if self.lista_probleme[i].get_nr_lab() == nr_lab:
                self.lista_probleme.pop(i)
            else: count += 1
        if count == len1:
            raise EroareNr_labInexistent("Numarul laboratorului nu exista in memorie")
    
    def cautare_problema(self,nr_lab):
        """
        Daca exista problema cu numarul de laborator specificat este returnata,
        in caz contrar este o arucata o exceptie speciala pentru acest caz
        nr_lab - string
        """
        len1 = len(self.lista_probleme)
        count = 0
        for i in range(0,len(self.lista_probleme)):
            if self.lista_probleme[i].get_nr_lab() == nr_lab:
                return self.lista_probleme[i]
                break
            else: count += 1
        if count == len1:
            raise EroareNr_labInexistent("Numarul laboratorului nu exista in memorie")
    
    def modificare_problema(self,nr_lab,descriere,deadline):
        """
        Daca exista problema cu numarul de laborator specificat este
        modificata cu numarul de laborator, descriere si deadline
        nr_lab, descriere , deadline - string
        """
        problema = Problema(nr_lab,descriere,deadline)
        len1 = len(self.lista_probleme)
        count = 0
        for i in range(0,len1):
            if self.lista_probleme[i].get_nr_lab() == nr_lab:
                self.lista_probleme[i].modif_nr_lab(nr_lab)
                self.lista_probleme[i].modif_descriere(descriere)
                self.lista_probleme[i].modif_deadline(deadline)
            else: count += 1
        if count == len1:
            raise EroareNr_labInexistent("Numarul laboratorului nu exista in memorie")

class NotareRepository():
    """
    Gestioneaza notele asignate unui student pentru fiecare laborator
    """
    def __init__(self,repo_studenti,repo_probleme):
        self.lista_note = []
        self.__repo_studenti = repo_studenti
        self.__repo_probleme = repo_probleme
        
    def find(self,student,problema):
        """
        Returneaza studentul,problema si nota daca studentului
        ii este asignata o problema care a fost notata
        student - Student
        problema- Problema
        """
        for nota in self.lista_note:
            if nota.getStudent() == student and nota.getProblema() == problema:
                return nota
        return None
    
    def stocare_notare(self,notare):
        """
        Stocheaza notarea unui student la o problema,
        iar daca notarea a fost facuta arunca o exceptie speciala
        pentru acest caz
        notare - Notare
        """
        if self.find(notare.getStudent(),notare.getProblema()) != None:
            raise EroareProblemaDejaNotata("Laboratorul deja a primit o nota")
        self.lista_note.append(notare)
    
    def get_lista_note(self):
        """
        Returneaza lista de note care au fost inregistrate
        """
        return self.lista_note
    
    def get_studenti_dupa_nr_lab_asignat(self,nr_lab):
        """
        Returneaza lista de sudenti care au primit un numar de laborator
        nr_lab - string
        """
        rez = []
        for nota in self.lista_note:
            if nota.getProblema().get_nr_lab() == nr_lab:
                rez.append(nota)
        return rez
    
    def get_note_dupa_ID_student(self,ID):
        """
        Returneaza lista de note a unui student cu ID-ul 
        specificat ca parametru
        ID - string 
        """
        rez = []
        for nota in self.lista_note:
            if nota.getStudent().get_ID() == ID:
                rez.append(nota)  
        return rez
    
    def get_lista_studenti_media_lab_sub_5(self):
        """
        Returneaza lista de studenti a caror medie de laboratoare
        este sub 5
        """
        studenti_restantieri = []
        lista_studenti = self.__repo_studenti.lista_studenti
        for student in lista_studenti:
            ID_student = student.get_ID()
            lista_note_student = self.get_note_dupa_ID_student(ID_student)
            medie = 0
            for note_student in lista_note_student:
                medie += note_student.getNota()
            medie = medie / len(lista_note_student)
            if medie < 5 :
                studenti_restantieri.append(f'{student.get_nume()} {medie}')
        return studenti_restantieri
    
class VerificareStudent():
    """
    Gestioneaza testarea tuturor functionalitatilor
    in ceea ce priveste lista de studenti
    """
    def test_adaugare_student(self):
        """
        Testeaza functia de adaugre student in lista de studenti
        """
        rep = StudentRepository()
        assert len(rep.lista_studenti) == 0
        rep.adauga_student("01","Popescu Ion","1")
        assert len(rep.lista_studenti) == 1
        rep.adauga_student("02","Popovici Diana","2")
        assert len(rep.lista_studenti) == 2
        try:
            rep.adauga_student("02","Popovici Diana","2")
            assert False
        except EroareDepozitareStudent:
            pass
        
    def test_stergere_student(self):
        """
        Testeaza functia de stergere student din lista de studenti
        """
        rep = StudentRepository()
        rep.adauga_student("01","Popovici Ion","1")
        rep.stergere_student("01")
        assert len(rep.lista_studenti) == 0
        rep.adauga_student("01","Popovici Ion","1")
        rep.adauga_student("02","Popescu Daniel","2")
        rep.stergere_student("02")
        assert len(rep.lista_studenti) == 1
        try:
            rep.stergere_student("02")
            return False
        except EroareIDInexistent as msg:
            pass
        
    def test_cautare_student(self):
        """
        Testeaza functia de cautare student in lista de studenti
        """
        rep = StudentRepository()
        rep.adauga_student("01","Popovici Ion","1")
        rep.adauga_student("02","Popescu Daniel","2")
        student = rep.cautare_student("02")
        assert student.get_ID() == "02" and student.get_nume() == "Popescu Daniel" and student.get_grupa() == "2"

    def test_modificare_student(self):
        """
        Testeaza functia de modificare a unui student
        """
        rep = StudentRepository()
        rep.adauga_student("01","Popovici Ion","1")
        rep.modificare_student("01","Cosmin Ion","1")
        student = rep.cautare_student("01")
        assert student.get_ID() == "01" and student.get_nume() == "Cosmin Ion" and student.get_grupa() == "1"
        
class VerificareProblema():
    """
    Gestioneaza testarea tuturor functionalitatilor
    in ceea ce priveste lista de probleme
    """
    def test_adaugare_problema(self):
        """
        Testeaza functia de adaugre problema in lista de probleme
        """
        rep = ProblemeRepository()
        assert len(rep.lista_probleme) == 0
        rep.adauga_problema("1","Suma a+b","12.12.2023")
        assert len(rep.lista_probleme) == 1
        rep.adauga_problema("2","Diferenta a-b","23.01.2024")
        assert len(rep.lista_probleme) == 2
        try:
            rep.adauga_problema("2","Produsul a*b","23.01.2023")
            assert False
        except EroareDepozitareProblema:
            pass
        
    def test_stergere_problema(self):
        """
        Testeaza functia de stergere problema din lista de probleme
        """
        rep = ProblemeRepository()
        rep.adauga_problema("1","Suma a+b","12.12.2023")
        rep.stergere_problema("1")
        assert len(rep.lista_probleme) == 0
        rep.adauga_problema("1","Suma a+b","12.12.2023")
        rep.adauga_problema("2","Diferenta a-b","23.01.2024")
        rep.stergere_problema("2")
        assert len(rep.lista_probleme) == 1
        try:
            rep.stergere_problema("2")
            return False
        except EroareNr_labInexistent:
            pass
        
    def test_cautare_probelma(self):
        """
        Testeaza functia de cautare problema in lista de probleme
        """
        rep = ProblemeRepository()
        rep.adauga_problema("1","Suma a+b","12.12.2023")
        rep.adauga_problema("2","Diferenta a-b","23.01.2024")
        problema = rep.cautare_problema("2")
        assert problema.get_nr_lab() == "2" and problema.get_descriere() == "Diferenta a-b" and problema.get_deadline() == "23.01.2024"
    
    def test_modificare_problema(self):
        """
        Testeaza functia de modificare problema in lista de probleme
        """
        rep = ProblemeRepository()
        rep.adauga_problema("1","Suma a+b","12.12.2023")
        rep.modificare_problema("1","Diferenta a-b","12.12.2023")
        problema = rep.cautare_problema("1")
        assert problema.get_nr_lab() == "1" and problema.get_descriere() == "Diferenta a-b" and problema.get_deadline() == "12.12.2023"
        
class VerificareNotare():
    """
    Gestioneaza testarea tuturor functionalitatilor
    in ceea ce priveste lista de notari
    """
    def testare_stocare_notare(self):
        """
        Testeaza stocarea unei notari in lista de notari
        """
        rep = NotareRepository(StudentRepository(),ProblemeRepository())
        student = Student("01","Rares","1")
        problema = Problema("1","Suma","12.12.2023")
        notare = Notare(student,problema,10)
        rep.stocare_notare(notare)
        lista_note = rep.get_lista_note()
        assert len(lista_note) == 1 
    
    def testare_lista_studenti_dupa_lab_asignat(self):
        """
        Testeaza functionalitatea de filtrare a listei de studenti
        care au primit un anumit numar de laborator
        """
        student1 = Student("01","Popescu Ion","1")
        student2 = Student("02","Popovici Diana","1")
        problema1 = Problema("1","Suma","12.12.2023")
        problema2 = Problema("2","Dif","12.12.2023")
        rep_notare = NotareRepository(StudentRepository(),ProblemeRepository())
        rep_notare.stocare_notare(Notare(student1,problema1,8))
        rep_notare.stocare_notare(Notare(student2,problema1,10))
        lista_studenti = rep_notare.get_studenti_dupa_nr_lab_asignat("1")
        assert len(lista_studenti) == 2
        
    def testare_note_dupa_ID_student(self):
        """
        Testeaza functionalitatea de filtrare a listei de note
        dupa un student
        """
        student1 = Student("01","Popescu Ion","1")
        student2 = Student("02","Popovici Diana","1")
        problema1 = Problema("1","Suma","12.12.2023")
        problema2 = Problema("2","Dif","12.12.2023")
        rep_notare = NotareRepository(StudentRepository(),ProblemeRepository())
        rep_notare.stocare_notare(Notare(student1,problema1,8))
        rep_notare.stocare_notare(Notare(student1,problema2,10))
        lista_note = rep_notare.get_note_dupa_ID_student("01")
        assert len(lista_note) == 2
    
    def testare_lista_studenti_media_lab_sub_5(self):
        rep_stud = StudentRepository()
        rep_prob = ProblemeRepository()
        rep_stud.adauga_student("01","Popescu Ion","1")
        rep_stud.adauga_student("02","Popovici Diana","1")
        student1 = Student("01","Popescu Ion","1")
        student2 = Student("02","Popovici Diana","1")
        problema1 = Problema("1","Suma","12.12.2023")
        problema2 = Problema("2","Dif","12.12.2023")
        rep_notare = NotareRepository(rep_stud,rep_prob)
        rep_notare.stocare_notare(Notare(student1,problema1,4))
        rep_notare.stocare_notare(Notare(student1,problema2,5))
        rep_notare.stocare_notare(Notare(student2,problema1,7))
        rep_notare.stocare_notare(Notare(student2,problema2,4))
        lista_studenti_restantieri = rep_notare.get_lista_studenti_media_lab_sub_5()
        assert lista_studenti_restantieri[0] == "Popescu Ion 4.5" and len(lista_studenti_restantieri) == 1
        