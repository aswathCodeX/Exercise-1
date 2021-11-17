import math as m


def calc_discharge(b, h, n, m_bank, S, **coeff):
    A = h * (b + h * m_bank)
    P = b + 2 * h * m.sqrt((m_bank ** 2) + 1)
    Rh = A / P
    for key, value in coeff.items():
        # while coeff[key] != 0:
        if 'k_st' in coeff:
            u = value * m.sqrt(S) * (Rh ** (2 / 3))
            Q = u * A
            return Q

        elif 'D_90' in coeff:
            u = 26 / (value ** (1/6)) * m.sqrt(S) * (Rh ** (2 / 3))
            Q = u * A
            return Q

        elif 'n_m' in coeff:
            u = 1 / value * m.sqrt(S) * (Rh ** (2 / 3))
            Q = u * A
            return Q

    u = 1/n * m.sqrt(S) * (Rh ** (2 / 3))
    Q = u * A
    return Q


def interpolate_h(*args, **kwargs):
    pass


if __name__ == '__main__':
    # input parameters
    Q = 15.5  # discharge in (m3/s)
    b = 5.1  # bottom channel width (m)
    m_bank = 2.5  # bank slope
    k_st = 20  # Strickler value
    n_m = 1 / k_st  # Manning's n
    S_0 = 0.005  # channel slope

    # coeff = {'k_st': 0, 'D_90': 0, 'n_m': 0}

    print("Choose the coefficient you want to input : k_st \t n_m \t D_90", end="")
    # for key, value in coeff.items():
    #     print(str(key), end="\t")
    key = input("\n")
    value = float(input("\nEnter the value of the coeffcient %s :" %key))
    # print(*coeff.values(), sep="\t")
    # print(key, value, sep="\t")

    Q = calc_discharge(b, 1, n_m, m_bank, S_0)
    print("The calculated discharge is %0.4f m3/s" % Q)

    # cof = str(coeff_keys[key])
    Q_flex = calc_discharge(b, 1, n_m, m_bank, S_0, **{key : value})
    print("The calculated discharge after flexibilizing the function is %0.4f m3/s" % Q_flex)

    # call the solver with user-defined channel geometry and discharge
    # h_n = interpolate_h(Q, b, n_m=n_m, m_bank=m_bank, S0=S_0)
