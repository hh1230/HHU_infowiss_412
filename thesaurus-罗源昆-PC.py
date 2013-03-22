#File: thesaurus.py
#Author: Yuankun LUO
#Version: 

"""
Das Programm ist zuvorstandlich nur fuer ein einfache ThesaurusDatabank.
Ein Thesaurus wird durch ein Dict implenmentiert.
Nach alle Operationen wird das ganze Dict gespeichert.
"""
thesaurus={}

class Deskriptorsatz:
    """
    Deskriptorsatz ist der Baustandteil von eine Thesaurus.
    Alle Relation zwischen String werden als Eingenschaften von Deskriptorsatz
    definiert.
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
        """
        self.deskriptor=deskriptor
        self.bf=bf
        self.bs=bs
        self.sb=sb
        self.ob=ob
        self.ub=ub
        self.vb=vb
        thesaurus[deskriptor]=self
        print self
        
    def __repr__(self):
        """
        Ueberschreiben __repr__ Operator, um ein Deskriptorsatz zu zeigen
        """
        return "\n  {deskriptor}\n{line}\nBF:{bf}\nBS:{bs}\nSB:{sb}\nOB:{ob}\nUB:{ub}\nVB:{vb}\n{stars}\n".format(deskriptor=self.deskriptor, bf=self.bf, bs=self.bs,sb=self.sb,ob=self.ob,ub=self.ub,vb=self.vb, stars='='*30,line='-'*30)


    def reset_bf(self):
        try:
            self.bf=[]
            print "Der BF von {deskriptor} wird rueckgestellt.\n".format(deskriptor=self.deskriptor)
            print self
        except:
            print "Methode reset_bf ist kappt"

    def add_bf(self,newbf):
        try:
            if isinstance(newbf,list):
                self.bf.extend(newbf)
                print "Neuer BF {bf} wird erfolreich in '{deskriptor}' hinzufuegt".format(bf=newbf, deskriptor=self.deskriptor)
            if isinstance(newbf,str):
                self.bf.append(newbf)
                print "Neuer BF {bf} wird erfolreich in '{deskriptor}' hinzufuegt".format(bf=newbf, deskriptor=self.deskriptor)
            else:
                print "Bitte eine List oder ein String als Argument geben!"
            print self
        except:
            print "Methode add_bf ist kappt"
        
    def del_bf(self,bf):
        try:
            if isinstance(bf,str):
                self.bf.remove(bf)
                print "BF {bf} wurde von '{deskriptor}' erfogreich geloescht.'".format(bf=bf, deskriptor=self.deskriptor)
                print self
        except:
            print "Bittle ein String als Argument geben.\nDie schon existierte BF sind:{bf}.".format(bf=self.bf)

    def op_add(self, rel, newbg):
        """
        Es gibt kein Switch...Case in Python, deshalbt muss ich ein einbisschen lange.
        rel muss als String 'BF','BS','SB','OB','UB' order 'VB' sein!!
        """
        try:
            if isinstance(rel,str) and rel==('BF'or'BS'or'SB'or'OB'or'UB'or'VB'):
                """
                Case("bf")
                """
                if rel=='BF':
                    if isinstance(newbg,str):
                        self.bf.append(newbg)
                    elif isinstance(newbg,list):
                        self.bf.extend(newbg)
                    print self
                if rel=='BS':
                    if isinstance(newbg,str):
                        self.bs.append(newbg)
                    elif isinstance(newbg,list):
                        self.bs.extend(newbg)
                    print self
                if rel=='SB':
                    if isinstance(newbg,str):
                        self.sb.append(newbg)
                    elif isinstance(newbg,list):
                        self.sb.extend(newbg)
                    print self
                if rel=='OB':
                    if isinstance(newbg,str):
                        self.ob.append(newbg)
                    elif isinstance(newbg,list):
                        self.ob.extend(newbg)
                    print self
                if rel=='UB':
                    if isinstance(newbg,str):
                        self.ub.append(newbg)
                    elif isinstance(newbg,list):
                        self.ub.extend(newbg)
                    print self
                if rel=='VB':
                    if isinstance(newbg,str):
                        self.vb.append(newbg)
                    if isinstance(newbg,list):
                        self.vb.extend(newbg)
                    print self
            else:
                print "Methode op_add(rel,newbg)\nArgument rel ist ein String!\nNur 'BS','BF','SB','OB','UB','VB' sind zulaessig.\nBittle versuchen Sie noch mal!\nBeispile:\ninstance.op_add('OB','Neu Begriff')\n oder eine List hinzufugen:\ninstance.op_add('OB',['list'])"
                
        except:
            print "Methode op_add(rel,argument) wurde nicht erfolgreich benutzt.\nBitten lesen __doc__"

    def op_del(self,rel,bg):
        """
        Mehtode op_del(self, rel, bg):
        rel muss 'BF','BS','SB','OB','UB' oder'VB' sein.
        bg kann entweder ein String oder eine List sein.
        """
        
        





"""
Test Code
"""
if __name__ == '__main__':
    d1=Deskriptorsatz('Infowiss',['Bf1','Bf2'],['BS1','BS2'],['SB'],['OB1','OB2'],['UB1','UB2'],['VB1','VB2'])
    d2=Deskriptorsatz('Python',['Bf1','Bf2'],['BS1','BS2'],['SB'],['OB1','OB2'],['UB1','UB2'],['VB1','VB2'])
    
