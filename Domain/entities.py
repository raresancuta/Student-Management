class Student():
    """
    Gestioneaza informatiile unui student
    """
    def __init__(self,ID,nume,grupa):
        self.__ID = ID
        self.__nume = nume
        self.__grupa = grupa
    
    def get_ID(self):
        """
        Returneaza ID-ul unui student
        """
        return self.__ID
    
    def get_nume(self):
        """
        Returneaza numele unui student
        """
        return self.__nume
    
    def get_grupa(self):
        """
        Returneaza grupa unui student
        """
        return self.__grupa
    
    def get_student_info(self):
        """
        Returneaza informatiile unui student
        """
        return self.__ID +' '+self.__nume+' '+self.__grupa
    
    def verif_egale(self,alt_student):
        """
        Returneaza True daca 2 studenti au aceleasi informatii,
        in caz contrar returneaza False
        """
        if alt_student == None:
            return False
        else: return self.get_ID() == alt_student.get_ID() and self.get_nume() == alt_student.get_nume() and self.get_grupa() == alt_student.get_grupa()
    
    def modif_ID(self,ID):
        """
        Modifica ID-ul unui student
        """
        self.__ID = ID
    
    def modif_nume(self,nume):
        """
        Modifica numele unui student
        """
        self.__nume = nume
        
    def modif_grupa(self,grupa):
        """
        Modifica grupa unui student
        """
        self.__grupa = grupa    
    
class Problema():
    def __init__(self,nr_lab,descriere,deadline):
        self.__nr_lab = nr_lab
        self.__descriere = descriere
        self.__deadline = deadline
        
    def get_nr_lab(self):
        """
        Returneaza numarul de laborator al unei probleme
        """
        return self.__nr_lab
    
    def get_descriere(self):
        """
        Returneaza descrierea al unei probleme
        """
        return self.__descriere
    
    def get_deadline(self):
        """
        Returneaza deadline-ul unei probleme
        """
        return self.__deadline
    
    def get_problem_info(self):
        """
        Returneaza informatiile unei probleme
        """
        return self.__nr_lab + " " + self.__descriere + " " + self.__deadline
    
    def verif_egale(self,alta_problema):
        """
        Returneaza True daca 2 probleme au aceleasi informatii,
        in cazz contrar returneaza False
        """
        if alta_problema == None:
            return False
        else: return self.__nr_lab == alta_problema.get_nr_lab() and self.__descriere == alta_problema.get_descriere and self.__deadline == alta_problema.get_deadline
    
    def modif_nr_lab(self,nr_lab):
        """
        Modifica numarul de laborator asignat unei probleme
        """
        self.__nr_lab = nr_lab
        
    def modif_descriere(self,descriere):
        """
        Modifica descrierea unei probleme
        """
        self.__descriere = descriere
    
    def modif_deadline(self,deadline):
        """
        Modifica deadline-ul unei probleme
        """
        self.__deadline = deadline
        
class Notare():
    """
    Gestioneaza informatiile unei notari
    """
    def __init__(self,student,problema,nota):
        self.__student = student
        self.__problema = problema
        self.__nota = nota
        
    def getStudent(self):
        """
        Returneaza informatiile unui student
        """
        return self.__student
    
    def getProblema(self):
        """
        Returneaza informatiile unei probleme
        """
        return self.__problema
    
    def getNota(self):
        """ 
        Returneaza nota asignata unei probleme
        """
        return self.__nota
    
    def __eq__(self,ot):
        """
        Verifica daca doua notari sunt identice
        """
        if ot == None: 
            return False
        return self.__student == ot.__student and self.__problema == ot.__problema and self.__nota == ot.__problema

class TestareStudent():
    """
    Gestioneaza testarea informatiilor unui student
    """      
    def testareStudent(self):
        
        student = Student('01','Popescu Ion','1')
        assert student.get_ID() == '01'
        assert student.get_nume() == 'Popescu Ion'
        assert student.get_grupa() == '1'
        
        student = Student('02','Popovici Diana','2')
        assert student.get_ID() == '02'
        assert student.get_nume() == 'Popovici Diana'
        assert student.get_grupa() == '2'

class TestareProblema():
    """
    Gestioneaza testarea informatiilor unei probleme
    """
    def testareProblema(self):    
        problema = Problema('1','Suma a+b','12.12.2023')
        assert problema.get_nr_lab() == '1'
        assert problema.get_descriere() == 'Suma a+b'
        assert problema.get_deadline() == '12.12.2023'
        
        problema = Problema('2','Diferenta a-b','14.09.2023')
        assert problema.get_nr_lab() == '2'
        assert problema.get_descriere() == 'Diferenta a-b'
        assert problema.get_deadline() == '14.09.2023'

class TestareNota():
    """
    Gestioneaza testarea informatiilor unei notari
    """
    def testare_nota(self):
        student = Student("01","Rares","1")
        problema = Problema("1","Sum","12.12.2023")
        notare = Notare(student,problema,10)
        assert notare.getStudent() == student
        assert notare.getProblema() == problema
        assert notare.getNota() == 10