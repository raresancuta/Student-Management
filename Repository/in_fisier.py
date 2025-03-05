from Domain.entities import Student, Problema, Notare
from Repository.memorie import StudentRepository, ProblemeRepository, NotareRepository

class StudentFisierRepository(StudentRepository):
    def __init__(self,file):
        StudentRepository.__init__(self)
        self.__file = file
        self.__incarca_din_fisier()
        
    def __incarca_din_fisier(self):
        """
        Incarca din fisier lista de studenti in memorie
        """
        try:
            f = open(self.__file,"r")
        except IOError:
            return
        with open(self.__file,"r") as fisier:
            line = fisier.readline().strip()
            while line != "":
                info = line.split(",")
                StudentRepository.adauga_student(self,info[0],info[1],info[2])
                line = fisier.readline().strip()
    
    def adauga_student(self,ID,nume,grupa):
        """
        Adauga un student in memorie si in fisier
        """
        StudentRepository.adauga_student(self,ID,nume,grupa)
        self.stocare_in_fisier()
        
    def stergere_student(self, ID):
        """
        Sterge un student din memorie si din fisier
        """
        StudentRepository.stergere_student(self,ID)
        self.stocare_in_fisier()
    
    def modificare_student(self, ID, nume, grupa):
        """
        Modifica un student din memorie si din fisier
        """
        StudentRepository.modificare_student(self,ID, nume, grupa)
        self.stocare_in_fisier()
    
    def stocare_in_fisier(self):
        """
        Stocheaza din memorie lista de studenti in fisier
        """
        lista_studenti = StudentRepository.get_list(self)
        ok = 0
        for student in lista_studenti:
            ID = student.get_ID()
            nume = student.get_nume()
            grupa = student.get_grupa()
            if ok == 0:
                with open(self.__file,"w") as fisier:
                    fisier.write(f'{ID},{nume},{grupa}\n')
                ok = 1
            else:
                with open(self.__file,"a") as fisier:
                    fisier.write(f'{ID},{nume},{grupa}\n')

class ProblemaFisierRepository(ProblemeRepository):
    def __init__(self,file):
        ProblemeRepository.__init__(self)
        self.__file = file
        self.__incarca_din_fisier()
    
    def __incarca_din_fisier(self):
        """
        Incarca din fisier lista de probleme in memorie
        """
        try:
            f = open(self.__file,"r")
        except IOError:
            return 
        with open(self.__file,"r") as fisier:
            line = fisier.readline().strip()
            while line != "":
                problema = line.split(";")
                ProblemeRepository.adauga_problema(self,problema[0],problema[1],problema[2])
                line = fisier.readline().strip()
    
    def adauga_problema(self,nr_lab,descriere,deadline):
        """
        Adauga o problema in memorie si in fisier
        """
        ProblemeRepository.adauga_problema(self,nr_lab,descriere,deadline)
        self.stocare_in_fisier()
    
    def stergere_problema(self,nr_lab):
        """
        Sterge o problema din memorie si din fisier
        """
        ProblemeRepository.stergere_problema(self,nr_lab)
        self.stocare_in_fisier()
    
    def modificare_problema(self,nr_lab,descriere,deadline):
        """
        Modifica o problema din memorie si din fisier
        """
        ProblemeRepository.modificare_problema(self,nr_lab,descriere,deadline)
        self.stocare_in_fisier()
    
    def stocare_in_fisier(self):
        """
        Stocheaza lista de probleme din memorie in fisier
        """
        lista_probleme = ProblemeRepository.get_list(self)
        ok = 0
        for problema in lista_probleme:
            nr_lab = problema.get_nr_lab()
            descriere = problema.get_descriere()
            deadline = problema.get_deadline()
            if ok == 0:
                with open(self.__file,"w") as fisier:
                    fisier.write(f'{nr_lab};{descriere};{deadline}\n')
                ok = 1
            else:
                with open(self.__file,"a") as fisier:
                    fisier.write(f'{nr_lab};{descriere};{deadline}\n')

class NotareFisierRepository(NotareRepository):
    def __init__(self,file,repo_stud,repo_probleme):
        NotareRepository.__init__(self,repo_stud,repo_probleme)
        self.__file = file
        self.__repo_studenti = repo_stud
        self.__repo_probleme = repo_probleme
        self.__incarca_din_fisier()
        
    def __incarca_din_fisier(self):
        """
        Incarca lista de notari din fisier in memorie
        """
        try:
            f = open(self.__file,"r")
        except IOError:
            return
        with open(self.__file,"r") as fisier:
            line = fisier.readline().strip()
            while line != "":
                notare = line.split(";")
                student = self.__repo_studenti.cautare_student(notare[0])
                problema = self.__repo_probleme.cautare_problema(notare[1])
                notare = Notare(student,problema,int(notare[2]))
                NotareRepository.stocare_notare(self,notare)
                line = fisier.readline().strip()
    
    def stocare_notare(self,notare):
        """
        Stocheaza o notare in memorie si in fisier
        """
        NotareRepository.stocare_notare(self,notare)
        self.stocare_in_fisier()
    
    def stocare_in_fisier(self):
        """
        Stocheaza lista de notari din memorie in fisier
        """
        lista_note = NotareRepository.get_lista_note(self)
        ok = 0
        for notare in lista_note:
            ID_student = notare.getStudent().get_ID()
            nr_lab = notare.getProblema().get_nr_lab()
            nota = notare.getNota()
            if ok == 0:
                with open(self.__file,"w") as fisier: 
                    fisier.write(f'{ID_student};{nr_lab};{nota}\n')
                ok = 1
            else:
                with open(self.__file,"a") as fisier: 
                    fisier.write(f'{ID_student};{nr_lab};{nota}\n')
    
class VerificareStudentInFisier():
   def testare_stocare_student(self):
       """
       Verifica daca un student este stocat in fisier
       """
       fisier = "teststudent.txt"
       f = open(fisier,"w")
       repo = StudentFisierRepository(fisier)
       repo.adauga_student("01","rares","1")
       repo2 = StudentFisierRepository(fisier)
       assert repo2.get_list_size() == 1
       assert repo2.cautare_student("01").get_ID() == "01"
       f.close()
       
class VerificareProblemaInFisier():
   def testare_stocare_problema(self):
       """
       Verifica daca o problema este stocata in fisier
       """
       fisier = "testproblema.txt"
       f = open(fisier,"w")
       repo = ProblemaFisierRepository(fisier)
       repo.adauga_problema("1","suma","12.12.2023")
       repo2 = ProblemaFisierRepository(fisier)
       assert repo2.get_list_size() == 1
       assert repo2.cautare_problema("1").get_nr_lab() == "1"
       f.close()
       
class VerificareNotareInFisier():
    def testare_stocare_notare(self):
        """
        Verifica daca o notare este stocata in fisier
        """
        fisier = "testnotare.txt"
        repo_stud = StudentFisierRepository("teststudent.txt")
        repo_prob = ProblemaFisierRepository("testproblema.txt")
        repo = NotareFisierRepository(fisier,repo_stud,repo_prob)
        student = repo_stud.cautare_student("01")
        problema = repo_prob.cautare_problema("1")
        notare = Notare(student,problema,10)
        repo.stocare_notare(notare)
        repo2 = NotareFisierRepository(fisier,repo_stud,repo_prob)
        lista_note =  repo2.get_note_dupa_ID_student("01")
        assert len(lista_note) == 1
        assert lista_note[0].getNota() == 10
        f = open(fisier,"w")
        f.close()
    

   