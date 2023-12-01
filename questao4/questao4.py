import numpy as np
from scipy.stats import poisson
from prettytable import PrettyTable
import math  # Adicionando a importação da biblioteca math

def mm1s(lam, mu, s):
    rho = lam / (s * mu)
    if rho >= 1:
        raise ValueError("A taxa de chegada (λ) deve ser menor que a taxa de atendimento (s * µ)")

    p0 = 1 / (sum([(rho ** i) / math.factorial(i) for i in range(s)]) + ((rho ** s) / (math.factorial(s) * (1 - rho))))
    pk = lambda k: (rho ** k) / (math.factorial(k) * p0)

    l = rho / (1 - rho)
    lq = (rho ** 2) / (1 - rho)
    w = 1 / (mu - lam)
    wq = rho / (mu - lam)

    pwq_gt_0 = sum([pk(i) for i in range(1, s + 1)])
    pwq_gt_1 = sum([pk(i) for i in range(2, s + 1)])
    pwq_gt_2 = sum([pk(i) for i in range(3, s + 1)])
    pwq_gt_5 = sum([pk(i) for i in range(6, s + 1)])

    return p0, pk(1), pk(2), pk(5), pk(10), l, lq, w, wq, pwq_gt_0, pwq_gt_1, pwq_gt_2, pwq_gt_5

def print_table(lam, mu):
    table = PrettyTable()
    table.field_names = ["s", "P0", "P1", "P2", "P5", "P10", "L", "Lq", "W", "Wq", "P(Wq > 0)", "P(Wq > 1)", "P(Wq > 2)", "P(Wq > 5)"]

    for s in range(1, 5):
        results = mm1s(lam, mu, s)
        table.add_row([s] + [round(result, 4) for result in results])

    print(table)

if __name__ == "__main__":
    arrival_rate = 0.5  # substitua com o valor desejado
    service_rate = 1.0  # substitua com o valor desejado

    print_table(arrival_rate, service_rate)