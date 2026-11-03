def usun_w_nawiasach(s):
    status = 0
    usuniete = ''
    for znak in (s):
        if (znak not in ['(', ')']) and (status == 0):
            usuniete += znak
        elif znak == '(':
            status += 1
        elif znak == ')':
            status -= 1
    print(usuniete)

usun_w_nawiasach('Ala ((hejka) ma kota) (perskiego)!')