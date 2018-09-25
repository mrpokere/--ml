# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 19:49:46 2018

@author: 2271057973
"""
import matplotlib.pyplot as plt
import numpy as np

def zuixia_o(data):
    x=[i[0] for i in data]
    y=[i[1] for i in data]
    def xh_e(x):
        return sum(x)
    def yh_e(y):
        return sum(y)
    def xyh_e(x,y):
        return sum([i*j for i,j in zip(x,y)]) 
    def xpingfan_g(x):
        return sum([i**2 for i in x])    
    n=len(x)
    b=(n*xyh_e(x,y)-xh_e(x)*yh_e(y))/(n*xpingfan_g(x)-xh_e(x)**2)
    a=(yh_e(y)*xpingfan_g(x)-xyh_e(x,y)*xh_e(x))/(n*xpingfan_g(x)-xh_e(x)**2)
    return a,b
def huat_u(b,a,data):
    x=[i[0] for i in data ]
    y=[i[1] for i in data ]
    plt.scatter(x, y)
    plt.plot(x,b*np.array(x)+a,'g-')
    plt.show()
data=[[1,2651],[2,1943],[3,1494],[4,1087],[5,765],[6,538],[7,484],[8,290],[9,226],[10,204]]

a,b=zuixia_o(data)
huat_u(b,a,data)
















