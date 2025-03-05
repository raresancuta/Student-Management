from Domain.entities import Student, Problema, Notare

class EroareStudent(Exception):
    """
    Eroare speciala in ceea ce priveste gestionarea unui student
    """
    pass

class EroareProblema(Exception):
    """
    Eroare speciala in ceea ce priveste gestionarea unei probleme
    """
    pass

class EroareNotare(Exception):
    """
    Eroare speciala in ceea ce priveste gestionarea unei notari
    """
    pass

class EroareValidareStudent(EroareStudent):
    """
    Eroare speciala in cazul in care datele unui 
    student sunt invalide
    """
    def __init__(self,msg):
        self.__msg = msg
        
    def get_msg(self):
        return self.__msg
    
class EroareIntrareID(EroareStudent):
    """
    Eroare speciala in cazul in care ID-ul specificat
    de utilizator este invalid
    """
    def __init__(self,msg):
        self.__msg = msg
        
    def get_msg(self):
        return self.__msg

class EroareValidareProblema(EroareProblema):
    """
    Eroare speciala in cazul in care datele unei probleme
    sunt invalide
    """
    def __init__(self,msg):
        self.__msg = msg
        
    def get_msg(self):
        return self.__msg

class EroareIntrareNr_lab(EroareProblema):
    """
    Eroare speciala in cazul in care numarul de
    laborator introdus de utilizator este invalid
    """
    def __init__(self,msg):
        self.__msg = msg
        
    def get_msg(self):
        return self.__msg

class EroareValidareNota(EroareNotare):
    """
    Eroare speciala in cazul in care nota unui laborator
    introdusa de utilizator este invalida
    """
    def __init__(self,msg):
        self.__msg = msg
        
    def get_msg(self):
        return self.__msg

class ValidareStudent():
    def validare_stud(self,ID,nume,grupa):
        """
        Returneaza lista erorilor de validare ale unui student
        cu ID-ul, numele si grupa introduse de utlizator
        ID, nume, grupa - string
        """
        erori = []
        if ID == "":
            erori.append("ID-ul nu poate fi gol")
        if nume == "":
            erori.append("Numele nu poate fi gol")
        if grupa == "":
            erori.append("Grupa nu poate fi goala")
        try:
            ID = int(ID)
        except ValueError :
            erori.append("ID-ul introdus nu este corect")
        nume = nume
        for litera in nume:
            if (litera >= 'a' and litera <= 'z') or (litera >='A' and litera <='Z') or litera == ' ':
                pass
            else: 
                erori.append("Numele nu poate contine alte caractere in afara de litere")
                break
        try:
            Grupa = int(grupa)
        except ValueError :
            erori.append("Grupa introdusa nu este corecta")
        if len(erori) > 0:
            raise EroareValidareStudent(erori)
        
    def validare_ID(self,ID):
        """
        Returneaza lista erorilor de validare ale
        unui ID introdus de utilizator
        ID - string
        """
        erori = []
        if ID == "":
            erori.append("ID-ul nu poate fi gol")
        try:
            ID = int(ID)
        except ValueError :
            erori.append("ID-ul introdus nu este corect")
        if len(erori) > 0:
            raise EroareIntrareID(erori) 

class ValidareProblema():
    def validare_problema(self,nr_lab,descriere,deadline):
        """
        Returneaza lista de erori de validare ale unei probleme
        cu numarul de laborator, descriere si deadline introduuse
        de utilizator
        nr_lab, descriere ,deadline - string
        """
        erori = []
        if nr_lab == "":
            erori.append("Numarul de laborator nu poate fi gol")
        if descriere == "":
            erori.append("Descrierea nu poate fi goala")
        if deadline == "":
            erori.append("Deadline-ul nu poate fi gol")
        try:
            nr_lab = int(nr_lab)
        except ValueError:
            erori.append("Numarul de laborator introdus este incorect")
        data = deadline
        if (data[2] == '.' and data[5] == '.') or (data[2] == '/' and data[5] == '/'):
            try:
                zi = int(data[0])*10+int(data[1])
                luna = int(data[3])*10+int(data[4])
                an = int(data[6])*1000 + int(data[7])*100 + int(data[8])*10+ int(data[9])
                if zi > 31:
                    erori.append("Ziua deadline-ului este invalida")
                if luna > 12 or luna == 0:
                    erori.append("Luna deadline-ului este invalida")
                if an < 2023 or an > 2025: 
                    erori.append("Anul introdus este invalid")
            except ValueError:
                erori.append("Data introdusa ca deadline este invalida")
        else: erori.append("Deadline-ul este o data invalida")
        if len(erori) > 0:
            raise EroareValidareProblema(erori)
        
    def validare_nr_lab(self,nr_lab):
        """
        Returneza erorile de validare ale unui
        numar de laborator introdus de utilizator
        nr_lab - string
        """
        erori = []
        if nr_lab == "":
            erori.append("Numarul de laborator nu poate fi gol")
        try:
            nr_lab = int(nr_lab)
        except ValueError :
            erori.append("Numarul de laborator introdus nu este corect")
        if len(erori) > 0:
            raise EroareIntrareNr_lab(erori) 

class ValidareNotare():
    def validare_nota(self,nota):
        """
        Returneaza erorile de validare a unei 
        note introduse de catre utilizator
        nota - int
        """
        erori = []
        if nota < 1 or nota > 10:
            erori.append("Nota trebuie sa fie intre 1 si 10")
        if len(erori) > 0:
            raise EroareValidareNota(erori)