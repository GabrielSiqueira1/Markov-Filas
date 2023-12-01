import numpy as np
from prettytable import PrettyTable
import math

def mm1(lambd, mi):
    rho = lambd/mi
    p0 = 1 - rho
    pn = lambda n: (1 - rho)*rho**n
    l = lambd/(mi - lambd)
    lq = l * (lambd/mi)
    w = 1 / (mi - lambd)
    wq = rho / (mi - lambd)
    
    pwq_gt_0 = rho*np.exp(-mi*(1-rho)*0)
    pwq_gt_1 = rho*np.exp(-mi*(1-rho)*1)
    pwq_gt_2 = rho*np.exp(-mi*(1-rho)*2)
    pwq_gt_5 = rho*np.exp(-mi*(1-rho)*5)
    
    return p0, pn(1), pn(2), pn(5), pn(10), l, lq, w, wq, pwq_gt_0, pwq_gt_1, pwq_gt_2, pwq_gt_5
    
def mms(lambd, mi, s):
    rho = lambd/(s*mi)
    p0 = 1 / (sum([((lambd/mi) ** i) / math.factorial(i) for i in range(s)]) + (((lambd/mi) ** s) / (math.factorial(s) * (1/(1-rho)))))
    pn = lambda n: (lambd/mi)**n/math.factorial(n)*p0 if n <= s else (lambd/mi)**n/(math.factorial(s)*s**(n-s))*p0
    lq = (p0*(lambd/mi)**s*rho)/(math.factorial(s)*(1-rho)**2)
    wq = lq/lambd
    w = wq + 1/mi
    l = lq + (lambd/mi)
    
    pwq_eq_0 = sum([pn(i) for i in range(0, s)])
    pwq_gt_0 = (1 - pwq_eq_0)*np.exp(-s*mi*(1-rho)*0)
    pwq_gt_1 = (1 - pwq_eq_0)*np.exp(-s*mi*(1-rho)*1)
    pwq_gt_2 = (1 - pwq_eq_0)*np.exp(-s*mi*(1-rho)*2)
    pwq_gt_5 = (1 - pwq_eq_0)*np.exp(-s*mi*(1-rho)*5)
    
    return p0, pn(1), pn(2), pn(5), pn(10), l, lq, w, wq, pwq_gt_0, pwq_gt_1, pwq_gt_2, pwq_gt_5

def tabela(lambd, mi):
    t = PrettyTable()
    t.field_names = ["s", "P0", "P1", "P2", "P5", "P10", "L", "Lq", "W", "Wq", "P(Wq > 0)", "P(Wq > 1)", "P(Wq > 2)", "P(Wq > 5)"]

    for s in range(1, 5):
        if s == 1:
            results = mm1(lambd, mi)
        else:
            results = mms(lambd, mi, s)
        t.add_row([s] + [round(result, 4) for result in results])

    print(t)

if __name__ == "__main__":
    taxa_chegada = 0.5  
    taxa_atendimento = 1.0  

    tabela(taxa_chegada, taxa_atendimento)