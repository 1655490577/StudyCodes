import requests


'''
通过requests上传图片文件/携程网
url；https://sinfo.ctrip.com/MyInfo/Ajax/UploadPhoto.ashx
path: /MyInfo/Ajax/UploadPhoto.ashx
headers：｛Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJeRJjyRcGdZNfPf5｝
cookies：Cookie: _abtest_userid=e0ea023b-f795-41ef-99b0-ac4e98e5193b; _ga=GA1.2.224955676.1592115120; _gid=GA1.2.320847301.1592115120; MKT_OrderClick=ASID=4897155950CNq_jP7SgOoCFQgCvAodEfEL4w6988193154159416766160662196671&AID=4897&CSID=155950&OUID=fpz&CT=1592115120308&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155950%26allianceid%3D4897%26ouid%3Dfpz%26keywordid%3D160662196671%26bd_vid%3D6988193154159416766%26ds_rl%3D1284915%26gclid%3DCNq_jP7SgOoCFQgCvAodEfEL4w%26gclsrc%3Dds&VAL={"pc_vid":"1592115117542.36opkf"}; _RF1=171.43.163.77; _RSG=FW4PC3fVU12YYWo34SdWyB; _RGUID=205e7e90-cc64-480f-bf20-9dc103ca08a2; _RDG=284f1ecb4538a1222a2f5c7d761a2dc685; MKT_CKID=1592115121449.s9i9k.1ico; MKT_CKID_LMT=1592115121451; MKT_Pagesource=PC; Union=SID=155952&AllianceID=4897&OUID=index; Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage=zh; login_uid=1C83116DFEA1FCD20C86DA620AA6EECA; login_type=0; cticket=56F639B3CDFDC64B6920ABAB0467625BD0727859F29ADE8958D9F0BCF370262D; AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojDfhukEq5UxzWBXSs+bJ+mxyYYhfXwL2bTfw5xrozj7FU9sSFNTS3zwBnn1mREe4wKyp2uYYMBLmTv7zZw+Rsoa3XHG+HGKlLS+fdRTkdQlzMImErwYFZHzbuqto/qV6Am0tMPLpAdUhaZMNkAStrm+lk0/cAXm8SVPOh63YuyYznit1SWN6HrJTHTRlSP82Lt3az3/hXyp38gU5+5mkhyxRkPraAYc04f4BP6OjbwC2NPADzkwxq4O9ReTJcmNF3pOLUXUxlXq4=; DUID=u=199B96C3714228F1FC07DDF7D260E078&v=0; IsNonUser=F; UUID=39BF7275DA5C4DE99D60E4DCBDA62D4A; IsPersonalizedLogin=F; _gat=1; __zpspc=9.1.1592115121.1592115194.2%232%7Csp0.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B%25E7%25BD%2591%7C%23; _jzqco=%7C%7C%7C%7C1592115194710%7C1.2080207817.1592115121445.1592115121445.1592115194605.1592115121445.1592115194605.0.0.0.2.2; ASP.NET_SessionSvc=MTAuMjUuMTY2LjMzfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTU4OTAwNDcwOTEzMw; ASP.NET_SessionId=5fwvgycozokqacwh2ardkufp; MyCtripDescription=UID=FD8BCEB7DDF264F86D2168864FA22C17&IsClub140=F&IsHoliday=F&CorpMileage=F; _bfa=1.1592115117542.36opkf.1.1592115117542.1592115117542.1.7; _bfs=1.7; _bfi=p1%3D100013%26p2%3D100101991%26v1%3D7%26v2%3D6
file：Content-Disposition: form-data; name="uploadFile_915"; filename="timg.jpg"
      Content-Type: image/jpeg
'''
url = 'https://sinfo.ctrip.com/MyInfo/Ajax/UploadPhoto.ashx/MyInfo/Ajax/UploadPhoto.ashx'
headers = {'Content-Type': "multipart/form-data; boundary=----WebKitFormBoundaryJeRJjyRcGdZNfPf5"}
files = {
        'uploadFile_915': ('timg.jpg', open('timg.jpg', 'rb'), 'image/jpeg')
        }
cookies = {
        'Cookie': '_abtest_userid=e0ea023b-f795-41ef-99b0-ac4e98e5193b; _ga=GA1.2.224955676.1592115120; '
                  '_gid=GA1.2.320847301.1592115120; '
                  'MKT_OrderClick=ASID=4897155950CNq_jP7SgOoCFQgCvAodEfEL4w6988193154159416766160662196671&AID=4897'
                  '&CSID=155950&OUID=fpz&CT=1592115120308&CURL=https%3A%2F%2Fwww.ctrip.com%2F%3Fsid%3D155950'
                  '%26allianceid%3D4897%26ouid%3Dfpz%26keywordid%3D160662196671%26bd_vid%3D6988193154159416766'
                  '%26ds_rl%3D1284915%26gclid%3DCNq_jP7SgOoCFQgCvAodEfEL4w%26gclsrc%3Dds&VAL={'
                  '"pc_vid":"1592115117542.36opkf"}; _RF1=171.43.163.77; _RSG=FW4PC3fVU12YYWo34SdWyB; '
                  '_RGUID=205e7e90-cc64-480f-bf20-9dc103ca08a2; _RDG=284f1ecb4538a1222a2f5c7d761a2dc685; '
                  'MKT_CKID=1592115121449.s9i9k.1ico; MKT_CKID_LMT=1592115121451; MKT_Pagesource=PC; '
                  'Union=SID=155952&AllianceID=4897&OUID=index; '
                  'Session=SmartLinkCode=U155952&SmartLinkKeyWord=&SmartLinkQuary=&SmartLinkHost=&SmartLinkLanguage'
                  '=zh; login_uid=1C83116DFEA1FCD20C86DA620AA6EECA; login_type=0; '
                  'cticket=56F639B3CDFDC64B6920ABAB0467625BD0727859F29ADE8958D9F0BCF370262D; '
                  'AHeadUserInfo=VipGrade=0&VipGradeName=%C6%D5%CD%A8%BB%E1%D4%B1&UserName=&NoReadMessageCount=0; '
                  'ticket_ctrip=bJ9RlCHVwlu1ZjyusRi+ypZ7X2r4+yojDfhukEq5UxzWBXSs+bJ'
                  '+mxyYYhfXwL2bTfw5xrozj7FU9sSFNTS3zwBnn1mREe4wKyp2uYYMBLmTv7zZw+Rsoa3XHG+HGKlLS'
                  '+fdRTkdQlzMImErwYFZHzbuqto/qV6Am0tMPLpAdUhaZMNkAStrm+lk0'
                  '/cAXm8SVPOh63YuyYznit1SWN6HrJTHTRlSP82Lt3az3/hXyp38gU5'
                  '+5mkhyxRkPraAYc04f4BP6OjbwC2NPADzkwxq4O9ReTJcmNF3pOLUXUxlXq4=; '
                  'DUID=u=199B96C3714228F1FC07DDF7D260E078&v=0; IsNonUser=F; UUID=39BF7275DA5C4DE99D60E4DCBDA62D4A; '
                  'IsPersonalizedLogin=F; _gat=1; '
                  '__zpspc=9.1.1592115121.1592115194.2%232%7Csp0.baidu.com%7C%7C%7C%25E6%2590%25BA%25E7%25A8%258B'
                  '%25E7%25BD%2591%7C%23; _jzqco=%7C%7C%7C%7C1592115194710%7C1.2080207817.1592115121445.1592115121445'
                  '.1592115194605.1592115121445.1592115194605.0.0.0.2.2; '
                  'ASP.NET_SessionSvc=MTAuMjUuMTY2LjMzfDkwOTB8b3V5YW5nfGRlZmF1bHR8MTU4OTAwNDcwOTEzMw; '
                  'ASP.NET_SessionId=5fwvgycozokqacwh2ardkufp; '
                  'MyCtripDescription=UID=FD8BCEB7DDF264F86D2168864FA22C17&IsClub140=F&IsHoliday=F&CorpMileage=F; '
                  '_bfa=1.1592115117542.36opkf.1.1592115117542.1592115117542.1.7; _bfs=1.7; '
                  '_bfi=p1%3D100013%26p2%3D100101991%26v1%3D7%26v2%3D6 '
        }

req = requests.post(url=url, files=files, verify=False, cookies=cookies)
print(req.text)
