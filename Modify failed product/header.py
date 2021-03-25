import json

get_item_edit_page_header = """
GET /smtProduct/edit.htm?id=46483711666092196 HTTP/1.1
Host: www.dianxiaomi.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.dianxiaomi.com/smtProduct/index.htm
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5
Cookie: _ati=4675260885799; _dxm_ad_client_id=8B5D340A3EDEA99AA87B7E1DADDBFD80D; Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1616517887,1616555481,1616569637,1616612174; dxm_i=ODEyNzMxIWFUMDRNVEkzTXpFITU0YWMyZDQ2NGI2Y2E1NWMxNDEwNjZlNGZmYmY2NWJl; dxm_t=MTYxNjY1OTQzNyFkRDB4TmpFMk5qVTVORE0zITE3ZjBjNzNkYjk5MTM2NmY2NDEwZmY3NjQyMjYzNjA2; dxm_c=VGJzZlpJYWUhWXoxVVluTm1Xa2xoWlEhOTViNWUyMmUzZmQwYTk4ODcwYzIwM2RkZTc5Y2IxZmE; dxm_w=YTExMzQ0ZGFjYjBiZGExZjBhYWNlM2QzNDM1OTkxNDUhZHoxaE1URXpORFJrWVdOaU1HSmtZVEZtTUdGaFkyVXpaRE0wTXpVNU9URTBOUSExZjE5NTJiM2IwMjBmMWRlYTY1YWQ4NGY4YjhmMDA4Nw; dxm_s=SP7ekHq14TKduCy03I0W2sgUEAv4L13imRyQYAcqCIg; JSESSIONID=03210C6813A397DBED3F5BC02AF63295; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1616659450
"""

save_or_publish_header = """
POST /smtProduct/add.json HTTP/1.1
Host: www.dianxiaomi.com
Connection: keep-alive
Content-Length: 18383
Pragma: no-cache
Cache-Control: no-cache
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://www.dianxiaomi.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.dianxiaomi.com/smtProduct/edit.htm?id=46483711664692054
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5
Cookie: _ati=4675260885799; dxm_i=ODEyNzMxIWFUMDRNVEkzTXpFITU0YWMyZDQ2NGI2Y2E1NWMxNDEwNjZlNGZmYmY2NWJl; dxm_t=MTYxNTc5NDM2OCFkRDB4TmpFMU56azBNelk0ITEyMDNiMjhkNDk5ZjJiZjU1YWFhODY1NDE1NWQ0ZWE3; dxm_c=QktvSnVLVEMhWXoxQ1MyOUtkVXRVUXchZTQwNzY2NjBkNzM3ODdiNGRlMGQ2ZTJiNWYwMDA5ZGY; dxm_w=YTExMzQ0ZGFjYjBiZGExZjBhYWNlM2QzNDM1OTkxNDUhZHoxaE1URXpORFJrWVdOaU1HSmtZVEZtTUdGaFkyVXpaRE0wTXpVNU9URTBOUSExZjE5NTJiM2IwMjBmMWRlYTY1YWQ4NGY4YjhmMDA4Nw; dxm_s=DYqrZDbOcbUbRooNVyAOLE5Q0yd95Cwql-0x8FEqUBg; _dxm_ad_client_id=8B5D340A3EDEA99AA87B7E1DADDBFD80D; Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1616391705,1616517887,1616555481,1616569637; JSESSIONID=5307751D87159D48209EBDAB7643F1F6; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1616570095
"""

get_product_list_header = """
Host: www.dianxiaomi.com
Connection: keep-alive
Content-Length: 83
Pragma: no-cache
Cache-Control: no-cache
Accept: text/html, */*; q=0.01
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://www.dianxiaomi.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://www.dianxiaomi.com/smtProduct/index.htm
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5
Cookie: _ati=4675260885799; dxm_i=ODEyNzMxIWFUMDRNVEkzTXpFITU0YWMyZDQ2NGI2Y2E1NWMxNDEwNjZlNGZmYmY2NWJl; dxm_t=MTYxNTc5NDM2OCFkRDB4TmpFMU56azBNelk0ITEyMDNiMjhkNDk5ZjJiZjU1YWFhODY1NDE1NWQ0ZWE3; dxm_c=QktvSnVLVEMhWXoxQ1MyOUtkVXRVUXchZTQwNzY2NjBkNzM3ODdiNGRlMGQ2ZTJiNWYwMDA5ZGY; dxm_w=YTExMzQ0ZGFjYjBiZGExZjBhYWNlM2QzNDM1OTkxNDUhZHoxaE1URXpORFJrWVdOaU1HSmtZVEZtTUdGaFkyVXpaRE0wTXpVNU9URTBOUSExZjE5NTJiM2IwMjBmMWRlYTY1YWQ4NGY4YjhmMDA4Nw; dxm_s=DYqrZDbOcbUbRooNVyAOLE5Q0yd95Cwql-0x8FEqUBg; _dxm_ad_client_id=8B5D340A3EDEA99AA87B7E1DADDBFD80D; Hm_lvt_f8001a3f3d9bf5923f780580eb550c0b=1616391705,1616517887,1616555481,1616569637; Hm_lpvt_f8001a3f3d9bf5923f780580eb550c0b=1616600217; JSESSIONID=D02F0A7081EED010C7810883AC797EFB
"""


def handle_headers(header_str):
    internal_dict={}
    for line in header_str.split('\n'):
        temp_list = line.split(': ', 1)
        if len(temp_list) == 2:
            key, value = temp_list
            internal_dict[key] = value

        # key = key.strip("\n")
        # print(line)
    return internal_dict


if __name__ == '__main__':
    tem = json.dumps(indent=2, obj=handle_headers())
    print(tem)
    print(handle_headers())
