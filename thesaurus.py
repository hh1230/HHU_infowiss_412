# -*- coding:utf-8 -*-
#File: thesaurus.py
#Project: Projektseminar Gruppe 412
#Project Member: Yuankun LUO & Jingwen Wu
#Author: Yuankun LUO 2039781
#Kommentarsprache： Deusche, Chinesische,weil alle die zwei Gruppenteilnehmen chinesen sind.
#Email: yuankun.luo@hhu.de
#Version: 2013.0.2

"""
Das Programm ist ein einfacher ThesaurusDatabank.
Ein Thesaurus wird durch eine Instance von Class Thesaurus implenmentiert.
Nach alle Operationen wird die Instance gespeichert.

这个简单的程序只用来操作一个辞典项目即可，但是为了方便，我设计了一个辞典类class Thesaurus,
每一个辞典是这个词典类的一个实例。
"""
#Benutyen pickle Modul um Datein zu speichern  运用pickle模块来储存所有数据
import pickle


#============================================================
#class Thesaurus 辞典类
#Jeder Thesaurus ist eine Instance von class Thesaurus.
#Thesaurusinstance hat einen Projektnam und eine Dict inhalts
#um alle Deksriptorsaetze zu speichern
#
#每一个辞典都是辞典类的一个实例，由于我们的程序很简单，我们只需要一个实例；
#但是为了方便起见，更好的面向对象，我们需要用这个类来保存数据。
#每一个实例有一个属性projectname来标记项目名称以及一个
#字典类型的inhalts属性来记录所有词条
#============================================================

class Thesaurus():
    
    def __init__(self, name):
        """
        Konstruktor __init__(self,name):
        wir brachen eine String name als projectname.
        alle Informationen werden in eine Dict heisst inhalts gespeichert.

        构造器函数 __init__(self，name):
        需要传入一个name字符串参数用作项目名称标记
        """
        self.projectname=name
        self.inhalts={}
    def __repr__(self):
        return "{projectname}\n{line}\n{de}\n{line}".format(projectname=self.projectname,line='*'*40,de=self.inhalts)

    def search_ds(self, bf):
        """
        Hier wird eine Funktionen definiert, die mit Suchen nach Deskriptorsatz zu tun haben.

        这里定义了搜索方法，搜索应该分两种，一种是搜索词条，如果词条搜索成功，就返回词词条；
        如果词条搜索失败，就调用关键字搜索，搜索每一个词条内的每一个子项。
        这里定义的是搜索词条方法
        """
        if isinstance(bf,str):
            try:
                if self.inhalts.has_key(bf):
                    print "{bf} wird erfolgrich gefunden!".format(bf=bf)
                    print self.inhalts[bf]
                else:
                    raise Exception()
            except:
                print "Sorry! {bf} wird nicht gefunden".format(bf=bf)

    def save_thesaurus(self,datenbank):
        """
        save_thesaurus() ist eine Funktion, um die Instance von class Thesaurus zu speichern,
        wir bentuzen pickle modul, weil pickle ist einfache und schnell.
        Alle Informationen von dieser Instance werden in einen 'datenbank' Dokument gespeichert.
        Bei Anrufen des Methodes muss noch eine Argument als dateinamen eingeben werden.
        
        我们要将这个Thesaurus辞典类的实例持久化保存，通过save_thesaurus方法。
        这是一个有参数的方法，直接新建一个根据传入的字符串参数作为数据库名称的文档把对象转化为字节码储存。
        """
        try:
            ouf=open(datenbank,'wb')
            data=self.inhalts
            pickle.dump(data,ouf)
            ouf.close()
            print "Thesaurus wird erfolgricht gespeichert!\n"
        except:
            print "Nicht erfolgreicht gesprichert!\n"

    def load_thesaurus(self, datenbank):
        """
        load_thesaurus() ist eine Funkion, die die schon in 'datenbank' gepeichert Information
        neue zu laden.

        同样用pickle模块的load()来装载已经保存的thesaurus辞典。
        """
        try:
            f=open(datenbank,'rb')
            self.inhalts=pickle.load(f)
            f.close()
            print "Thesaurus wird erfolgricht gelaedt!\n"
            print self.inhalts.keys()
        except:
            print "Wird nicht erfolgricht gelaedet!\n"
    
    



#===================================================================
#class Deskriptorsatz mit OPP-Idee
#
#基于面向对象思想定义的词条类
#===================================================================



class Deskriptorsatz:
    """
    Deskriptorsatz ist der Baustandteil von eine Thesaurus.
    Alle Relation zwischen String werden als Eingenschaften von Deskriptorsatz
    definiert.
    我们定义一个词条类来定义每一个词条，因为题目要求必须用到面向对象。
    """
    def __init__(self, deskriptor, bf=[], bs=[], sb=[], ob=[], ub=[], vb=[]):
        """
        Konstructor von Klasse Deskriptorsatz, um eine Instance von Deskriptorsatz zu bauen.
        Eine Instance von Deskriptorsatz wird direct in dict thesaurus hinzufuegt,
        durch die Befehlen thesaurus[deskriptor]=self.
        Jede Instance ist ein Objekt. Sie hat Properties:
        deskriptor, bf, bs, sb, ob, ub und vb.
        Mann kan direckt durch Konstruktor ein Instance mit vorllstandigen Informationen bauen,
        oder nur ein Instance mit deskriptor machen. Weiter mit methode Z.B op_add(rel, newbg) machen.


        这里是词条类 class Deskriptorsatz 的构造器。 形式参数列表解释如下：
        deskriptor 也就是这个词条的名称；
        bf， bs, sb, ob, ub, vb 的参数初始默认值是一个空列表类型。
        在构造之前会先检测这个词条是否已经在thesaurus中出现，
        如果出现会抛出错误，告诉构造不成功。
        我们用构造器来做添加词条的工具。
        在构造器完成后会打印这个已经构造好的词条。
        """
        try:
            for e in t1.inhalts.keys():
                if e is deskriptor:
                    raise Exception()
            self.deskriptor=deskriptor
            self.bf=bf
            self.bs=bs
            self.sb=sb
            self.ob=ob
            self.ub=ub
            self.vb=vb
            t1.inhalts[deskriptor]=self
            print self
        except:
            print "__init__() wird nicht erfolgrich angeruft.\nVielleicht du hast ein schon existierte Deskriptor hinzufuegt!\n "
        
    def __repr__(self):
        """
        @override __repr__ funktion, um die print Funktion zu definieren wir folgende Stil:
        @重载的运算符 __repr__ 会将print函数的格式改变，打印下列样式：
                  Infowiss
            ------------------------------
            BF:['Bf1', 'Bf2']
            BS:['BS1', 'BS2']
            SB:['SB']
            OB:['OB1', 'OB2']
            UB:['UB1', 'UB2']
            VB:['VB2', 'VB1']
            ==============================
        """
        return "\n  {deskriptor}\n{line}\nBF:{bf}\nBS:{bs}\nSB:{sb}\nOB:{ob}\nUB:{ub}\nVB:{vb}\n{stars}\n".format(deskriptor=self.deskriptor, bf=self.bf, bs=self.bs,sb=self.sb,ob=self.ob,ub=self.ub,vb=self.vb, stars='='*30,line='-'*30)

    """
    Hier werden alle reset_reg() methode definiert.
    rest_reg() methoden machen alle Properties von Deskriptor leer.
        
    这里定义一个reset_rel()方法，用作把每一个词条的各项子类清空。
    """
    def reset_all(self):
        self.bf = [];
        self.bs = [];
        self.sb = [];
        self.ob = [];
        self.ub = [];
        self.vb = [];
        print self;
    
    def reset_bf(self):
        try:
            self.bf=[]
            print "Der BF von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
        except:
            print "Methode reset_bf ist kappt"

    def reset_bs(self):
        try:
            self.bs=[]
            print "Der BS von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
        except:
            print "Methode reset_bf ist kappt"

    def reset_sb(self):
        try:
            self.sb=[]
            print "Der SB von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
        except:
            print "Methode reset_bf ist kappt"

    def reset_ob(self):
        try:
            self.ob=[]
            print "Der OB von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
        except:
            print "Methode reset_bf ist kappt"

    def reset_ub(self):
        try:
            self.ub=[]
            print "Der UB von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
        except:
            print "Methode reset_bf ist kappt"

    def reset_vb(self):
        try:
            self.vb=[]
            print "Der VB von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
        except:
            print "Methode reset_bf ist kappt"


    """
    Hier werde alle add_reg() methode definiert.
    reg kann als bf, bs ... benennen.
    Nur Sring oder eine Liste von String(s) durfen hinzufuegt.
   
    add_reg() 方法：
    每个reg代表每一个子项，用小写字母表示，比如bs，bf...
    添加时会检测形式参数，必须是字符串或者字符串的列表才能被添加成功。
    添加成功打印一个更新后的词条。
    """

    def add_bf(self,newbf):
        pass
                    
            



    """
    Hier werden alle del_reg() methode definiert.
    Um jedes Item unter verschiedenen Properties zu loeschen.
    Wenn man eine Properties oder ganz Deskriptor leer machen,
    dann benutzen rest_reg() methoden.

    这里定义一些删除字条字项的方法，因为我们用字典来保存子项的每一个属性，如果是删除子项里面的一个字符串，
    则需要传入字符串作为形式参数。如果是想清空子项，或者完全清空，将调用reset_reg()方法。
    """
    def del_bf(self,bf):
        try:
            if isinstance(bf,str):
                self.bf.remove(bf)
                print "BF {bf} wurde von '{deskriptor}' erfogreich geloescht.'".format(bf=bf, deskriptor=self.deskriptor)
                print self
        except:
            print "Bittle ein String als Argument geben.\nDie schon existierte BF sind:{bf}.".format(bf=self.bf)



                    


#===================================================================
#Test Code
#
#测试用代码
#===================================================================


if __name__ == '__main__':
    t1=Thesaurus('Project412')
    t1.load_thesaurus('t1_data.dat')
    '''
    d1=Deskriptorsatz('Infowiss',['Bf1','Bf2'],['BS1','BS2'],['SB'],['OB1','OB2'],['UB1','UB2'],['VB2','VB1'])
    d2=Deskriptorsatz('Python',['Bf1','Bf2'],['BS1','BS2'],['SB'],['OB1','OB2'],['UB1','UB2'],['VB1','VB2'])
    '''

