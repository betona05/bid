import requests
import xmltodict
from bs4 import BeautifulSoup as bs
import lxml

# 한국토지공사 공사(전기.통신.소방.문화재공사 등)
#	          90.5   2.5   85.495%    50억 ~ 100억
#                      89.25  1.25  86.745%    10억 ~ 50억
#                      89.25  1.25  86.745%     3억 ~ 10억    87.745% (종합전문공사)
#                      88.25  0.25  87.745%     8천 ~ 3억
#                      88.25  0.25  87.745%           ~8천
#용역(기술)  10억이상    79.995%
#             5억~10억   85.495%
#             2억3천~5억 86.745%
#             ~ 2억 3천  87.745%
#용역(시설이외)     72.995%    5억이상
#                  80.495%   2억3천 ~ 5억
#                  82.995%        ~ 2억3천
#용역(시설)  87.995%
#
#물품              95.5   7.5    80.495%   10억이상 제조자 한정물품
#                   95.5   7.5    80.495%    2억3천 ~ 10억
#                   91.75 3.75   84.245%           ~ 2억3천
#1. 국가를 당사자로하는 계약에 관한 법률 제4조제1항의 규정에 의한 고시금액
#공사 : 87억원,
#물품 및 용역 : 2억 3천만원


#bidRate[0][0] = (전기.통신.소방.문화재공사 등)  [1] = (종합전문공사)        ===> 0 공사   시설공사
#bidRate[1][0] = 기술 [1] = 시설이외 [2] = 시설                            ===> 1 용역    용역
#bidRate[2][0] = 물품 모두 같음                                             
bidRate = [[[[85.495,5000000000,10000000000],
          [86.745,1000000000,5000000000],
          [86.745,300000000,1000000000],
          [87.745,80000000,300000000],
          [87.745,0,80000000],],
          [[85.495,5000000000,10000000000],
          [86.745,1000000000,5000000000],
          [87.745,300000000,1000000000],
          [87.745,80000000,300000000]]],

          [[[79.995,1000000000,99999999999],
          [85.495,500000000,1000000000],
          [86.745,230000000,500000000],
          [87.745,0,230000000]],
          [[72.995,500000000,99999999999],
          [80.495,230000000,500000000],
          [82.995,0,230000000]],
          [[87,995,0,99999999999]]],

          [[[80.495,1000000000,99999999999],
          [80.495,230000000,1000000000],
          [84.245,0,230000000]]]]

bidKind2 = 0

lhUrl ='http://openapi.ebid.lh.or.kr/ebid.com.openapi.service.OpenBidInfoList.dev'
serviceKey = "vBZ8RM09l8en5jiYiklJofDtmsNtwar8TeYtm8MQBii8X6rPO%2Fycyce5D%2BiMJT8IbuB5IJy4ymCtZVEeqHN7KQ%3D%3D"
g2bkeydecoding = "vBZ8RM09l8en5jiYiklJofDtmsNtwar8TeYtm8MQBii8X6rPO/ycyce5D+iMJT8IbuB5IJy4ymCtZVEeqHN7KQ=="
lhparams = {'serviceKey' : g2bkeydecoding, 'numOfRows' : '200', 'pageNo' : '1', 'tndrbidRegDtStart' : '', 'tndrbidRegDtEnd' : '' }

bidNtceNo = '2202096'
inputDate = '20220622'
url3 = 'http://ebid.lh.or.kr/ebid.et.tp.cmd.BidctrctgdsDetailListCmd.dev?bidNum=2202248&bidDegree=00'
url2 = 'http://ebid.lh.or.kr/ebid.et.tp.cmd.BidConstructDetailListCmd.dev?bidNum=2202248&bidDegree=00'
# 2202040 시설공사
# 2202225 용역
# 2202248 지급자재
def bidListLH(inputDate,bidNtceNo):
    global lhparams

    lhparams['tndrbidRegDtStart'] = inputDate
    lhparams['tndrbidRegDtEnd'] = inputDate

    errStr = "LH 기초, A값구하기"
    try:
        response = requests.get(lhUrl, params=lhparams)
        data = xmltodict.parse(response.text)
#        data = json.dumps(dictionary)
    except requests.exceptions.Timeout as errd:
        print("{} Time out {}".format(errStr,errd))
        return
    except requests.exceptions.ConnectionError as errc:
        print("{} 인터넷연결안됨 {}".format(errStr,errc))
        return
    except requests.exceptions.HTTPError as errb:
        print("{} HTTPerror{}".format(errStr,errb))
        return
    except requests.exceptions.RequestException as erra:
        print("{} RequestExcepion{}".format(errStr,erra))
        return

    # print(data)
    header = data['response']['header']
    body = data['response']['body']
    resultCode = header['resultCode']     # 00  정상
    totalCount = body['totalCount']       # 공고일기준 데이터 갯수

    if(resultCode =='00' and int(totalCount) >= 1) :
        items = body['item']
        for item in items:
            if(item['bidNum'] != bidNtceNo) : continue
            fdmtlAmt = item['fdmtlAmt']   # 기초금액
            prcscoreExclusAmt = item['prcscoreExclusAmt']  # A값
            fdmtAmtStr = format(int(fdmtlAmt),',')
            prcscoreExclusAmtStr = format(int(prcscoreExclusAmt),',')
            print("기초금액 {} A값 {}".format(fdmtAmtStr,prcscoreExclusAmtStr))

def bidLHread(lhUrl):
    response = requests.get(lhUrl)
    html = bs(response.text,'lxml')
    #   <div id="LblockPageTitle">
    tempStr = html.find('div',{"id":"LblockPageTitle"}).find('h1').text
    bidKindStr = tempStr[tempStr.find("(")+1:-1]    # (시설공사)  =>  시설공사
    if bidKindStr =="시설공사": bidKind1 = 0
    elif bidKindStr =="용역": bidKind1 = 1
    elif bidKindStr =="물품": bidKind1 = 2
    elif bidKindStr =="지급자재": bidKind1 = 2
    else : return

    prtStr = ""
    for tag in html.select('label'):
        if(tag.text == "기초금액"):
            Str = tag.next_element.next_element.next_element.text
            BPriceStr = Str[:Str.find('원')]
            prtStr = prtStr + "기초금액 : {} \n".format(BPriceStr)
        if(tag.text == "가격점수제외금액(A)"):
            Str = tag.next_element.next_element.next_element.text
            APriceStr = Str[:Str.find('원')]
            prtStr = prtStr + "가격점수제외금액(A) : {} \n".format(APriceStr)            
        if(tag.text == "낙찰제외기준금액"):
            Str = tag.next_element.next_element.next_element.text
            CPriceStr = Str[:Str.find('원')]
            prtStr = prtStr + "낙찰제외기준금액 : {} \n".format(CPriceStr)            

    print(prtStr,bidKind1,bidKindStr)
    BPrice = int(BPriceStr.replace(',',''))

    for bidR in bidRate[bidKind1][bidKind2] :
        if BPrice >= bidR[1] and BPrice < bidR[2] : Rate = bidR[0]
    
    print("낙찰하한율 : {}".format(Rate))

    

#    basePrice = html.select('label=contains("prcscoreExclusAmt")')
#    print(basePrice.next_sibling.next_sibling.text)


bidListLH(inputDate,bidNtceNo)
bidLHread(url2)
#공고일반정보 > table > tbody > tr:nth-child(9) > td
#공고일반정보 > table > tbody > tr:nth-child(9) > th > label