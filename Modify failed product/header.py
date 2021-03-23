header = """
Host: www.dianxiaomi.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.dianxiaomi.com/smtProduct/offline.htm?dxmState=offline&dxmOfflineState=publishFail&shopId=-1
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5
Cookie: _ati=4675260885799; dxm_i=ODEyNzMxIWFUMDRNVEkzTXpFITU0YWMyZDQ2NGI2Y2E1NWMxNDEwNjZlNGZmYmY2NWJl; dxm_t=MTYxNTc5NDM2OCFkRDB4TmpFMU56azBNelk0ITEyMDNiMjhkNDk5ZjJiZjU1YWFhODY1NDE1NWQ0ZWE3; dxm_c=QktvSnVLVEMhWXoxQ1MyOUtkVXRVUXchZTQwNzY2NjBkNzM3ODdiNGRlMGQ2ZTJiNWYwMDA5ZGY; dxm_w=YTExMzQ0ZGFjYjBiZGExZjBhYWNlM2QzNDM1OTkxNDUhZHoxaE1URXpORFJrWVdOaU1HSmtZVEZtTUdGaFkyVXpaRE0wTXpVNU9URTBOUSExZjE5NTJiM2IwMjBmMWRlYTY1YWQ4NGY4YjhmMDA4Nw; dxm_s=DYqrZDbOcbUbRooNVyAOLE5Q0yd95Cwql-0x8FEqUBg; _dxm_ad_client_id=8B5D340A3EDEA99AA87B7E1DADDBFD80D; Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1615992688,1615994620,1616046728,1616059520; JSESSIONID=D97F277876ACC6E19CC96333B792B4AE; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1616077710
"""

header_dict = {}


def handle_headers(header_str=header):
    for line in header_str.split('\n'):
        temp_list = line.split(': ', 1)
        if len(temp_list) == 2:
            key, value = temp_list
            header_dict[key] = value

        # key = key.strip("\n")
        # print(line)
    return header_dict


if __name__ == '__main__':
    handle_headers(header_str=header)

    print(header_dict)
