import requests
import xmltodict


lhUrlResult1 ='http://openapi.ebid.lh.or.kr/ebid.com.openapi.service.OpenPreprcList.dev'  # 예정가격보기 URL
lhUrlResult2 ='http://openapi.ebid.lh.or.kr/ebid.com.openapi.service.OpenTenderopenList.dev'  # 개찰결과보기 URL
serviceKey = "vBZ8RM09l8en5jiYiklJofDtmsNtwar8TeYtm8MQBii8X6rPO%2Fycyce5D%2BiMJT8IbuB5IJy4ymCtZVEeqHN7KQ%3D%3D"
g2bkeydecoding = "vBZ8RM09l8en5jiYiklJofDtmsNtwar8TeYtm8MQBii8X6rPO/ycyce5D+iMJT8IbuB5IJy4ymCtZVEeqHN7KQ=="
lhparams = {'serviceKey' : g2bkeydecoding, 'numOfRows' : '200', 'pageNo' : '1', 'openDtmStart' : '', 'openDtmEnd' : '' }

bidNtceNo = '2004496'
inputDate = '20201103'

# 2202225 용역
# 2202248 지급자재
def bidListLHResult1(inputDate,bidNtceNo):
    global lhparams

    lhparams['openDtmStart'] = inputDate
    lhparams['openDtmEnd'] = inputDate

    errStr = "LH 예정가격 구하기"
    try:
        response = requests.get(lhUrlResult1, params=lhparams)
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
            bidNum = item['bidNum']                   #공고번호
            bidnmKor = item['bidnmKor']               #공고명
            expectPrc = item['expectPrc']               #예정가격
            fdmtlAmt = item['fdmtlAmt']               #기초금액
            prcscoreExclusAmt = item['prcscoreExclusAmt']               #가격점수제외금액
            decMultprcs = []
            decMultprcs.append(int(item['decMultprc1']))               #복수예비가격1
            decMultprcs.append(int(item['decMultprc2']))               #복수예비가격2
            decMultprcs.append(int(item['decMultprc3']))               #복수예비가격3
            decMultprcs.append(int(item['decMultprc4']))               #복수예비가격4
            decMultprcs.append(int(item['decMultprc5']))               #복수예비가격5
            decMultprcs.append(int(item['decMultprc6']))               #복수예비가격6
            decMultprcs.append(int(item['decMultprc7']))               #복수예비가격7
            decMultprcs.append(int(item['decMultprc8']))               #복수예비가격8
            decMultprcs.append(int(item['decMultprc9']))               #복수예비가격9
            decMultprcs.append(int(item['decMultprc10']))               #복수예비가격10
            decMultprcs.append(int(item['decMultprc11']))               #복수예비가격11
            decMultprcs.append(int(item['decMultprc12']))               #복수예비가격12
            decMultprcs.append(int(item['decMultprc13']))               #복수예비가격13
            decMultprcs.append(int(item['decMultprc14']))               #복수예비가격14
            decMultprcs.append(int(item['decMultprc15']))               #복수예비가격15
            multprcChoicecnts = []
            multprcChoicecnts.append(int(item['multprc1Choicecnt']))     #복수예가1 선택수
            multprcChoicecnts.append(int(item['multprc2Choicecnt']))     #복수예가2 선택수
            multprcChoicecnts.append(int(item['multprc3Choicecnt']))     #복수예가3 선택수
            multprcChoicecnts.append(int(item['multprc4Choicecnt']))     #복수예가4 선택수
            multprcChoicecnts.append(int(item['multprc5Choicecnt']))     #복수예가5 선택수
            multprcChoicecnts.append(int(item['multprc6Choicecnt']))     #복수예가6 선택수
            multprcChoicecnts.append(int(item['multprc7Choicecnt']))     #복수예가7 선택수
            multprcChoicecnts.append(int(item['multprc8Choicecnt']))     #복수예가8 선택수
            multprcChoicecnts.append(int(item['multprc9Choicecnt']))     #복수예가9 선택수
            multprcChoicecnts.append(int(item['multprc10Choicecnt']))     #복수예가10 선택수
            multprcChoicecnts.append(int(item['multprc11Choicecnt']))     #복수예가11 선택수
            multprcChoicecnts.append(int(item['multprc12Choicecnt']))     #복수예가12 선택수
            multprcChoicecnts.append(int(item['multprc13Choicecnt']))     #복수예가13 선택수
            multprcChoicecnts.append(int(item['multprc14Choicecnt']))     #복수예가14 선택수
            multprcChoicecnts.append(int(item['multprc15Choicecnt']))     #복수예가15 선택수
            print("공고번호: {} 공고명: {} 기초금액: {} A값: {}".format(bidNum,bidnmKor,fdmtlAmt,prcscoreExclusAmt))
            print("예정가격 : {}".format(expectPrc))
            for index, decMultprc in enumerate(decMultprcs) :
                print("NO{0:>2} :{1: >13} ({2})".format(index,decMultprc,multprcChoicecnts[index]))



            #print("NO 1 : {1: >13} ({2}) {3}".format())


    

#    basePrice = html.select('label=contains("prcscoreExclusAmt")')
#    print(basePrice.next_sibling.next_sibling.text)

bidListLHResult1(inputDate,bidNtceNo)

#공고일반정보 > table > tbody > tr:nth-child(9) > td
#공고일반정보 > table > tbody > tr:nth-child(9) > th > label