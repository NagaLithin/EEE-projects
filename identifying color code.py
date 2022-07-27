# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 21:58:47 2022

@author: lithin
"""
n=int(input("enter the no. of colors existed in the color code"))
m=["black\n","brown\n","red\n","orange\n","yellow\n","green\n","blue\n","violet\n","grey\n","white\n","gold\n","silver\n"]
print("only enter the color that exist in the above list\n", m)
color_digit={'black':'0',
                 'brown':'1',
                 'red':'2',
                 'orange':'3',
                 'yellow':'4',
                 'green':'5',
                 'blue':'6',
                 'violet':'7',
                 'grey':'8',
                 'white':'9',
                 'gold':' ',
                 'silver':' '}
multiplier={     'black':'1',
                 'brown':'10',
                 'red':'100',
                 'orange':'1k',
                 'yellow':'10k',
                 'green':'100k',
                 'blue':'1M',
                 'violet':'10M',
                 'grey':' ',
                 'white':' ',
                 'gold':'0.1',
                 'silver':'0.01'}
tolerance={    'balck':' ',
                 'brown':'+/-1%',
                 'red':'+/-2%',
                 'orange':' ',
                 'yellow':' ',
                 'green':'+/-0.5%',
                 'blue':'+/-0.25%',
                 'violet':'+/-0.1%',
                 'grey':'+/-0.05%',
                 'white':' ',
                 'gold':'+/-5%',
                 'silver':'+/- 10%',
                 'none':'+/-20%'}
temperature_coefficient={'black':'250ppm/k',
                         'brown':'100ppm/k',
                         'red':'50ppm/k',
                         'orange':'15ppm/k',
                         'yellow':'25ppm/k',
                         'green':'20ppm/k',
                         'blue':'10ppm/k',
                         'violet':'5ppm/k',
                         'grey':'1ppm/k',
                         'white':' ',
                         'gold':' ',
                         'silver':'',
                         'none':' '}
if n==3:
    a=input("enter color")
    b=input("enter color")
    c=input("enter color")
    if a in color_digit and b in color_digit and c in tolerance:
        xx= color_digit.get(a)
        yy= multiplier.get(b)
        aa=tolerance.get(c)
        print("Resistence= "+xx+ "x"+yy+" ohms" +aa)
elif n==4:
    a=input("enter color")
    b=input("enter color")
    c=input("enter color")
    d=input("enter color")
    if a in color_digit and b in color_digit and    c in multiplier and d in tolerance:
        xx= color_digit.get(a)
        yy= color_digit.get(b)
        aa=multiplier.get(c)
        bb=tolerance.get(d)
        print("Resistence= "+xx + yy+ "x"+aa+" ohms" +bb)
elif n==5:
    a=input("enter color")
    b=input("enter color")
    c=input("enter color")
    d=input("enter color")
    e=input("enter color")
    if a in color_digit and b in color_digit and c in color_digit and  d in multiplier and e in tolerance:
        xx= color_digit.get(a)
        yy= color_digit.get(b)
        zz=color_digit.get(c)
        aa=multiplier.get(d)
        bb=tolerance.get(e)
        print("Resistence= "+xx + yy+ zz+"x"+aa+" ohms" +bb)
elif n==6:
    a=input("enter color")
    b=input("enter color")
    c=input("enter color")
    d=input("enter color")
    e=input("enter color")
    f=input("enter color")
    if a in color_digit and b in color_digit and c in color_digit and  d in multiplier and e in tolerance and f in temperature_coefficient :
        xx= color_digit.get(a)
        yy= color_digit.get(b)
        zz=color_digit.get(c)
        aa=multiplier.get(d)
        bb=tolerance.get(e)
        cc=temperature_coefficient.get(f)
        print("Resistence= "+xx + yy+ zz+"x"+aa+" ohms" +bb +cc)
else:
    print("Invalid colors")