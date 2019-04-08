from pylab import *
from matplotlib import rc

import os.path as path
import sys
from scipy import interpolate
from pandas import read_excel as read
rc('text', usetex=True)
rc('text.latex', preamble=[r'\usepackage[russian]{babel}',
                         r'\usepackage{amsmath}',
                        r'\usepackage{amssymb}'])


rc('font', family='serif')

rec = path.abspath('..'+'\\rec\\rec.xlsx')
sheet_name='Лист1'
df=read(rec, sheet_name=sheet_name)

figure(sheet_name)
x=array(df['x, мм'])
y=log(array(df['А, мВ']))

g = polyfit(x[8:-1],y[8:-1],1)
print(g[0])
f=poly1d(g)
t=linspace(x[0],x[-1],1000)
plot(t,f(t),label='аппроксимация',color='darkblue')

plot(x[8:-1],y[8:-1],'r.',label='эксперимент')
t=linspace(x[0],x[-1],len(x))
plot(t[0:8],f(t[0:8]),'r.',label='_nolabel_' )
ylabel(r'$\ln{U},\text{ у.е.}$',fontsize=16)
xlabel(r'$x, \text{мм}$',fontsize=16)
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
legend()
savefig(path.abspath('..'+'\\fig\\1.pdf'))

show()