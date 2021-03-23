headers_of_mine = """Host: www.dianxiaomi.com
Connection: keep-alive
Content-Length: 2074
Pragma: no-cache
Cache-Control: no-cache
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://www.dianxiaomi.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.dianxiaomi.com/smtProduct/edit.htm?id=46483711626580494
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5
Cookie: dxm_i=ODEyNzMxIWFUMDRNVEkzTXpFITU0YWMyZDQ2NGI2Y2E1NWMxNDEwNjZlNGZmYmY2NWJl; dxm_t=MTYxNTU2MzMzNCFkRDB4TmpFMU5UWXpNek0wITRjMTAyMTQ2MDdjNmE4ZWYzMDk3ZTVhNjFhYjA3YjEy; dxm_c=ZWNxM2pnOXAhWXoxbFkzRXphbWM1Y0EhYTQ5OTE2Zjk3NDI2YzBlYmVkNDBlODliNDY5ZTlkYmQ; dxm_w=YTExMzQ0ZGFjYjBiZGExZjBhYWNlM2QzNDM1OTkxNDUhZHoxaE1URXpORFJrWVdOaU1HSmtZVEZtTUdGaFkyVXpaRE0wTXpVNU9URTBOUSExZjE5NTJiM2IwMjBmMWRlYTY1YWQ4NGY4YjhmMDA4Nw; dxm_s=mLFvo3higfsK1nhefyr_KE_fxoqzjpsSEOp6gRKe_Xs; _dxm_ad_client_id=8507D6116D6B64F5B6C0DBC01A8ED12ED; Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1615477828,1615541348,1615561229,1615615915; JSESSIONID=9E399ECB7A1895A2F58534B56FC50A14; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1615621150
"""

headers_dict = {

}


def handle_headers(header_str):
    for line in headers_of_mine.split('\n'):
        temp_list = line.split(': ', 1)
        if len(temp_list) == 2:
            key, value = temp_list
            headers_dict[key] = value

        # key = key.strip("\n")
        # print(line)
    return headers_dict


if __name__ == "__main__":
    handle_headers()
    print(headers_dict)
