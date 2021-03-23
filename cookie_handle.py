from sys import platform

my_cookie = """_ati=9901810195441; dxm_i=ODEyNzMxIWFUMDRNVEkzTXpFITU0YWMyZDQ2NGI2Y2E1NWMxNDEwNjZlNGZmYmY2NWJl; 
dxm_t=MTYxNDU2OTg3NSFkRDB4TmpFME5UWTVPRGMxIWIxZWJmNjY4ZWIxMGEzZDQ4MmVkN2U4NmY4NDA2ZDIz; 
dxm_c=ZTB2Q2lvaU8hWXoxbE1IWkRhVzlwVHchY2EwODZjM2ExZDhjODEyMGYyNGQxZWNkOGYzZTg1ZTA; 
dxm_w
=YTExMzQ0ZGFjYjBiZGExZjBhYWNlM2QzNDM1OTkxNDUhZHoxaE1URXpORFJrWVdOaU1HSmtZVEZtTUdGaFkyVXpaRE0wTXpVNU9URTBOUSExZjE5NTJiM2IwMjBmMWRlYTY1YWQ4NGY4YjhmMDA4Nw; dxm_s=hdoKqJn4ffLiqj1A0THLIfBX-nPf7QCMd_d9XlBwJ9M; _dxm_ad_client_id=94E71E1F11093F58E5E056975EE99E540; Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1615294479,1615440547,1615470135,1615477828; JSESSIONID=49355DEEF3A3AAFAF403FD223EBD8264; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1615484371"""

cookie_dict = {}


def handle_cookie():
    for line in my_cookie.split('; '):
        key, value = line.split('=', 1)
        key = key.strip("\n")
        cookie_dict[key] = value
        # print(key, value)
        # key, value = line.split('=', 1)
        # cookie[key] = value
    # print(cookie_dict)
    # print(cookie_dict)
    return cookie_dict


if __name__ == '__main__':
    handle_cookie()
