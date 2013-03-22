# -*- coding:utf-8 -*-
#File: thesaurus.py
#Project: Projektseminar Gruppe 412
#Project Member: Yuankun LUO 2039781 & Jingwen Wu
#Author: Yuankun LUO
#Email: yuankun.luo@hhu.de
#Version: 

"""
Das Programm ist zuvorstandlich nur fuer ein einfache ThesaurusDatabank.
Ein Thesaurus wird durch ein Dict implenmentiert.
Nach alle Operationen wird das ganze Dict gespeichert.
我们的项目只需要保存一个辞典就行，这样我就用一个叫做thesaurus的字典类型变量来保存所有
词条，到时候直接通过pickel方法吧这个thesausurs保存起来就行。
"""
thesaurus={}

"""
Hier werden allen Methoden, die mit Suchen zu tun haben definiert.

这里定义了搜索方法，搜索应该分两种，一种是搜索词条，如果词条搜索成功，就返回词词条；
如果词条搜索失败，就调用关键字搜索，搜索每一个词条内的每一个子项。
"""

def search_ds(bf):
    if isinstance(bf,str):
        try:
            if thesaurus.has_key(bf):
                print "{bf} wird erfolgrich gefunden!".format(bf=bf)
                print thesaurus[bf]
            else:
                raise Exception()
        except:
            print "Nicht gefunden"


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
            for e in thesaurus.keys():
                if e is deskriptor:
                    raise Exception()
            self.deskriptor=deskriptor
            self.bf=bf
            self.bs=bs
            self.sb=sb
            self.ob=ob
            self.ub=ub
            self.vb=vb
            thesaurus[deskriptor]=self
            print self
        except:
            print "__init__() wird nicht erfolgrich angeruft.\nVielleicht du hast ein schon existierte Deskriptor hinzufuegt!\n "
        
    def __repr__(self):
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
    Nur Sring oder eine Stringliste durfen hinzufuegt.
   
    add_reg() 方法：
    每个reg代表每一个子类属性，添加时会检测形式参数，必须是字符串或者字符串的列表才能被添加成功。
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



                    




"""
Test Code
"""
if __name__ == '__main__':
    d1=Deskriptorsatz('Infowiss',['Bf1','Bf2'],['BS1','BS2'],['SB'],['OB1','OB2'],['UB1','UB2'],['VB2','VB1'])
    d2=Deskriptorsatz('Python',['Bf1','Bf2'],['BS1','BS2'],['SB'],['OB1','OB2'],['UB1','UB2'],['VB1','VB2'])
    t=thesaurus
    p=t['Python']
