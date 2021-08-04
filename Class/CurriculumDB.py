import pandas as pd
import numpy as np
import networkx as nx
import CurriculumGraph as CurriculumGraph
import pyodbc

class CurriculumDB:
    cnxn = None
    cursor = None
    edgesnumbers = []
    Lessons = []
    LessonsClasses = []
    CoursesDescriptions = None
    def __init__(self, excel_file, serverip, databasename, username, password):
        cg = CurriculumGraph.CurriculumGraph(excel_file)
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+ serverip +'; DATABASE='+ databasename +'; UID=' + username + '; PWD=' + password)
        self.cursor = self.cnxn.cursor()
        for i in cg.SheetNameEdgesList:
            self.edgesnumbers.append(int(i.replace("Edges", "")))
        Edges = cg.GetEdges()
        Edges = Edges.to_numpy()
        for i in range(0,len(Edges[:,0])):
            self.Lessons.append(Edges[i][0])
        self.LessonsClasses = cg.GetAliases()
        self.GenLessonsClasses()
        self.CoursesDescriptions = pd.read_excel(cg.excel_file, sheet_name = "CourseNamesNarratives").to_numpy()

    def GenLessonsClasses(self):
        for i in range(0,len(self.LessonsClasses[:,0])):
            self.LessonsClasses[i][1] = int(self.LessonsClasses[i][1].replace("MAT",""))
        self.LessonsClasses[0][0] = 1
        j = 0
        for i in range(1, len(self.LessonsClasses[:,0])):
            j = j + 1
            if self.LessonsClasses[i - 1][1] == self.LessonsClasses[i][1]:
                self.LessonsClasses[i][0] = j + 1  
            else:
                self.LessonsClasses[i][0] = 1
                j = 0

    def GenOpus(self):  
        for i in self.edgesnumbers:
            self.cursor.execute("INSERT INTO OPUS (id_opus, id_artifex, id_emendator, cd_opus_type, id_created, dt_created, ds_graph) VALUES (?, 1, 1, 'LITERATRONIC', 1, GETDATE(), '')", i)
        self.cnxn.commit()

    def GenPagina(self):
        Pagina = []
        for i in range(0,len(self.LessonsClasses[:,0])):
            Pagina.append([int(self.LessonsClasses[i][0]),int(self.LessonsClasses[i][1])])
        self.cursor.executemany("INSERT INTO PAGINA (id_pagina, id_opus, id_created, dt_created, am_link, ds_gui, pagina_type, pagina_cat) VALUES (?, ?, 1, GETDATE(), 0, NEWID(), NULL, NULL)",Pagina)
        self.cnxn.commit()
    def GenLinguaOpus(self):
        LinguaOpus = []
        for i in range(0,len(self.CoursesDescriptions[:,0])):
            LinguaOpus.append([self.CoursesDescriptions[i][0], self.CoursesDescriptions[i][1], self.CoursesDescriptions[i][2]])
        self.cursor.executemany("SET ANSI_WARNINGS OFF; INSERT INTO LINGUA_OPUS (id_opus, cd_lingua, ds_title, ds_tag, ds_content, in_visible, id_created, dt_created) VALUES (?, 'HISPANIA', ?, ?, '', 1, 1, GETDATE())", LinguaOpus)
        self.cursor.executemany("SET ANSI_WARNINGS OFF; INSERT INTO LINGUA_OPUS (id_opus, cd_lingua, ds_title, ds_tag, ds_content, in_visible, id_created, dt_created) VALUES (?, 'BRITANNIA', ?, ?, '', 1, 1, GETDATE())", LinguaOpus)
        self.cnxn.commit()
    
    def GenLinguaPagina(self):
        LinguaPagina = []
        Pagina = []
        for i in range(0,len(self.LessonsClasses[:,0])):
            Pagina.append([int(self.LessonsClasses[i][0]),int(self.LessonsClasses[i][1])])
        LastLesson = []
        for i in range(0, len(Pagina) - 1):
            if self.LessonsClasses[i][1] != self.LessonsClasses[i+1,1]:
                LastLesson.append([self.LessonsClasses[i][1], self.LessonsClasses[i][0]])
        LastLesson.append([self.LessonsClasses[-1][1], self.LessonsClasses[-1][0]])
        LastLessonCourse = None
        for i in range(0,len(Pagina)):
            for j in range(0,len(LastLesson)):
                if LastLesson[j][0] == int(self.LessonsClasses[i][1]):
                    LastLessonCourse = LastLesson[j][1]
            LinguaPagina.append([int(self.LessonsClasses[i][1]), int(self.LessonsClasses[i][0]), self.LessonsClasses[i][2], LastLessonCourse])
        self.cursor.executemany("INSERT INTO LINGUA_PAGINA (id_opus, id_pagina, cd_lingua, ds_title, ds_content, id_created, dt_created, id_capstone, ds_StartLesson) VALUES (?, ?, 'BRITANNIA', ?, '', 1, GETDATE(), ?, NULL)",LinguaPagina)
        self.cnxn.commit()
