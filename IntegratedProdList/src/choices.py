import csv

def MEMBER_CHOICES(fileName):
    person_list = []
    with open(fileName, newline='',encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['lastName'].upper()+", "+row['firstName'].upper()
            item = tuple([name, name])
            person_list.append(item)
        return tuple(person_list)

NOD_CHOICES = (
        ('Nod Problem 1','Nod Problem 1'),
        ('Nod Problem 2','Nod Problem 2'),
        ('Nod Problem 3','Nod Problem 3'),
        ('Nod Problem 4','Nod Problem 4'),
        ('Nod Problem 5','Nod Problem 5'),
        )
ML_CHOICES = (
    ("Mission Line 1", "Mission Line 1"),
    ("Mission Line 2", "Mission Line 2"),
    ("Mission Line 3", "Mission Line 3"),
    ("Mission Line 4", "Mission Line 4"),
    ("Mission Line 5", "Mission Line 5"),
)
PRI_CHOICES = (
    ("HIGH","HIGH"),
    ("MED","MED"),
    ("LOW", "LOW")
)

STATUS_CHOICES = (
    ("WORKING","WORKING"),
    ("ON HOLD","ON HOLD"),
    ("CANCELLED","CANCELLED")
)

ORG_CHOICES = (
    ("ACN","ACN"),
    ("ACNA","ACNA"),
    ("ACNI","ACNI"),
    ("ACNL","ACNL"),
    ("ACNQ","ACNQ"),
    ("ACNS","ACNS"),
    ("ACNW","ACNW"),
)

FLIGHT_TITLE = {
    'ACN':'Group',
    'ACNA':'ACNA Flight',
    'ACNI':'ACNI Flight',
    'ACNL':'ACNL Flight',
    'ACNQ':'ACNQ Flight',
    'ACNS':'ACNS Flight',
    'ACNW':'ACNW Flight',
}