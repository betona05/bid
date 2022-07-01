import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time
import requests
import json
import random
import socket
# from playsound import playsound
import xmltodict
from bs4 import BeautifulSoup as bs

isInternet = False
ipaddress=socket.gethostbyname(socket.gethostname())
if ipaddress=="127.0.0.1":
    print("You are not connected to the internet!")
    isInternet = False
else:
    print("You are connected to the internet with the IP address of "+ ipaddress )
    isInternet = True

priceRate =[ [[0.9700000000, 0.973750000],
            [0.9737500001, 0.9775000001],
            [0.9775000002, 0.9812500002],
            [0.9812500003, 0.9850000003],
            [0.9850000004, 0.9887500004],
            [0.9887500005, 0.9925000005],
            [0.9925000006, 0.9962500006],
            [0.9962500007, 1.0000000000],
            [1.0000000001, 1.0042857142],
            [1.0042857143, 1.0085714285],
            [1.0085714286, 1.0128571428],
            [1.0128571429, 1.0171428571],
            [1.0171428572, 1.0214285714],
            [1.0214285715, 1.0287142857],
            [1.0257142858, 1.0300000000]],
            [[0.9800000000, 0.9826500000],
            [0.9826600000, 0.9853100000],
            [0.9853200000, 0.9879800000],
            [0.9879900000, 0.9906500000],
            [0.9906600000, 0.9933200000],
            [0.9933300000, 0.9959900000],
            [0.9960000000, 0.9986600000],
            [0.9986700000, 1.0013300000],
            [1.0013400000, 1.0040000000],
            [1.0040100000, 1.0066700000],
            [1.0066800000, 1.0093400000],
            [1.0093500000, 1.0120100000],
            [1.0120200000, 1.0146800000],
            [1.0146900000, 1.0173400000],
            [1.0173500000, 1.0200000000]] ]
# LH 낙찰하한율 데이터 
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
form_class = uic.loadUiType("bid.ui")[0]

serviceKey = "vBZ8RM09l8en5jiYiklJofDtmsNtwar8TeYtm8MQBii8X6rPO%2Fycyce5D%2BiMJT8IbuB5IJy4ymCtZVEeqHN7KQ%3D%3D"
g2bkeydecoding = "vBZ8RM09l8en5jiYiklJofDtmsNtwar8TeYtm8MQBii8X6rPO/ycyce5D+iMJT8IbuB5IJy4ymCtZVEeqHN7KQ=="

# url1 = 조달청 입찰공고정보서비스
# url2 = 조달청 낙찰정보서비스
url1 = "http://apis.data.go.kr/1230000/BidPublicInfoService03"
url2 = "http://apis.data.go.kr/1230000/ScsbidInfoService"

baseurl = 'http://apis.data.go.kr/1230000/BidPublicInfoService03/getBidPblancListInfo'
urls = [baseurl+'Thng', baseurl+'Cnstwk',baseurl+'Servc']
urlList = ['물품','공사','용역']
urlsBsisAmount = [baseurl+'ThngBsisAmount', baseurl+'CnstwkBsisAmount',baseurl+'ServcBsisAmount']

lhUrl ='http://openapi.ebid.lh.or.kr/ebid.com.openapi.service.OpenBidInfoList.dev'


urlResult = 'http://apis.data.go.kr/1230000/ScsbidInfoService/getOpengResultListInfoOpengCompt'
urlResult2 = 'http://apis.data.go.kr/1230000/ScsbidInfoService/getOpengResultListInfo'             #  {}CnstwkPreparPcDetail'
urlResult2s = [urlResult2+'ThngPreparPcDetail', urlResult2+'CnstwkPreparPcDetail',urlResult2+'ServcPreparPcDetail']

urlA = 'http://apis.data.go.kr/1230000/BidPublicInfoService03/getBidPblancListBidPrceCalclAInfo?'

params ={'serviceKey' : g2bkeydecoding, 'numOfRows' : '10', 'pageNo' : '1', 'inqryDiv' : '2', 'bidNtceNo' : '', 'type' : 'json' }
paramsResult ={'serviceKey' : g2bkeydecoding, 'numOfRows' : '900', 'pageNo' : '1', 'bidNtceNo' : '', 'type' : 'json', 'bidNtceOrd': '00','bidClsfcNo':'0', 'rbidNo':'0' }
lhparams = {'serviceKey' : g2bkeydecoding, 'numOfRows' : '200', 'pageNo' : '1', 'tndrbidRegDtStart' : '', 'tndrbidRegDtEnd' : '' }
                                                                                                                    #   공고차수            입찰분류번호(재공고건 1)        재입찰번호                                                                                                                 
#bidNtceNo = '20220618405'
#bidNtceNo = '20220616711'
#bidNtceNo = '20220623796'
# bidNtceNo = '2202200'  #1300억짜리
#bidNtceNo = '2004496'   #비트낙찰
#bidNtceNo = '2202096'
bidNtceNo = '20220629869'




priceList = []
priceSelList =  [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
dismodelTitle = QStandardItemModel()
dismodel1 = QStandardItemModel()
dismodel1Str = []
dismodel2 = QStandardItemModel()
dismodel2Str = []
dismodel2Tail = QStandardItemModel()
priceNum = 0
sbidrage = 87.745  # 낙찰율
isDisplay = False
isArm = False      # 알람상태표시
ArmDate = ""       # 알람 날짜
ArmTime = ""       # 알람 시간
ArmbidNumber = ""  # 개찰 공고번호
ArmSecCount = 0
totalCountResult = 0   #개찰 토탈카운트

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        global dismodel1
        self.setupUi(self)
        self.btnReset.clicked.connect(self.runClear)              # 전체클리어
        self.btnSearch.clicked.connect(self.runSearch)            # 공고번호로 검색
        self.btnAdd.clicked.connect(self.addBtn)                  # 기초금액 산출로 복사
        self.clock()
        self.bidNum.setText(bidNtceNo)                            # 임시 공고번호 입력
        self.btnPrice1.clicked.connect(self.runPrice1)            # 복수예비가격 1번산출
        self.btnPrice1S.clicked.connect(self.runPrice1S)          # 복수예비가격 반복산출
        self.btnRunPrice1.clicked.connect(self.runBidPrice1)      # 투찰금액 1번산출
        self.checkBoxSort.stateChanged.connect(self.runSort)      # 복수예비가격 정렬
        self.checkBoxSort_2.stateChanged.connect(self.runSort2)   # 산출가격 정렬
        self.btnRunPrices.clicked.connect(self.runBidPrice1S)     # 투찰금액 복수산출
        self.btnAdd2.clicked.connect(self.addAlmBtn)              #개찰결과확인하기로 공고번호 복사
        self.btnReset_2.clicked.connect(self.runBidClear)         #산출초기화
        self.listViewBidRun.clicked.connect(self.runBidSel)       #산출값 클릭시 복수예비가격 표시하기
        self.listViewResultList.clicked.connect(self.runBidSelCom)       #개찰결과 클릭시 업체명 표시하기
        self.btnBidResultList.clicked.connect(self.runBidResultList)  #개찰결과확인하기
        self.btnSearchCom.clicked.connect(self.runSearchCom)      # 개찰 업체 검색
        self.checkBoxArm.stateChanged.connect(self.runArm)        # 개찰 알람설정하기
        self.btnBestBid.clicked.connect(self.runBestBid)          # 최적 산출 찾기


    # 모두 클리어 하기
    def runClear(self):
        global dismodel1
        global priceNum
        global priceList
        global priceSelList
        global dismodelTitle
        global dismodel2Title
        global dismodel1Str
        global dismodel2Str
        self.bidNum.setText("")
        self.txtResult1.setText("")
        self.txtResult2.setText("")
        self.txtResult3.setText("")
        self.txtResult4.setText("")
        self.txtResult5.setText("")
        self.txtResult7.setText("")
        self.txtResult8.setText("")
        self.txtResult9.setText("")
        self.txtResult10.setText("")
        self.txtResult11.setText("")
        self.txtResult2_1.setText("")
        self.txtResult2_3.setText("")
        self.txtResult12.setText("")
        self.labAresult.setText("")
        self.bidNum_2.setText("")
        self.txtResult8_2.setText("")
        self.txtBidCom.setText("")
        self.txtBidFirst.setText("")
        self.txtBidFirst_2.setText("")
        self.txtBidFirst_3.setText("")
        self.txtBidFirst_4.setText("")
        self.txtBidCom_2.setText("")
        self.txtBidCom_3.setText("")
        self.txtBidCom_4.setText("")
        self.txtResult13.setText("")
        self.txtInputDt.setText("")
        priceList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
        priceSelList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
        self.display15()
        self.txtBidEprice.setText("")
        self.txtBidPrice.setText("")
        dismodel1.clear()
        dismodel2.clear()
        dismodel1Str.clear()
        dismodel2Str.clear()
        priceNum = 0  
        dismodelTitle.clear()
        dismodel2Tail.clear()
        self.listViewBidRun.setModel(dismodel1)  # lisetView에 산출값지우기
        self.listViewResultList.setModel(dismodel2) 
        self.listViewResultListTail.setModel(dismodel2Tail)
        self.listViewBidRunTitle.setModel(dismodelTitle)  # 타이틀 지우기

    #산출초기화
    def runBidClear(self):
        global dismodel1
        global dismodel1Str
        global dismodelTitle
        global priceNum
        global isDisplay
        global priceSelList
        
        priceSelList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
        self.display15()
        dismodel1.clear()
        dismodel1Str.clear()
        self.listViewBidRun.setModel(dismodel1)  # lisetView에 산출값지우기      
        dismodelTitle.clear()
        self.listViewBidRunTitle.setModel(dismodelTitle)  # 타이틀 지우기
        isDisplay = False
        priceNum = 0  

    #산출값 클릭시 복수예비가격 표시하기
    def runBidSel(self, index):
        global dismodel1
        global priceSelList
        global sbidrage

        selitem = dismodel1.itemFromIndex(index).text()
    
        a = selitem.find('(')+1
        b = selitem.find(')')
        result = selitem[a:b].split(',')
 #       print("{} => {} => {}".format(index,selitem,result))
        aa = selitem.find('순공사적용')
        if aa != -1: self.labDisplay.setText(selitem[aa:])

        priceSelList =  [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]
        r = [ 0,0,0,0 ]
        r[0] = int(result[0])-1
        priceSelList[r[0]] = 1
        r[1] = int(result[1])-1
        priceSelList[r[1]] = 1
        r[2] = int(result[2])-1
        priceSelList[r[2]] = 1
        r[3] = int(result[3])-1
        priceSelList[r[3]] = 1
        sum = 0
        for i in range(4):
            sum += priceList[r[i]]
#            print(priceList[r[i]])
        ePrice = int(sum/4)
        ePriceStr = format(ePrice,',')
        sbidrage = float(self.txtResult2_3.text())
#        print("예정가격 : {}".format(ePriceStr))
        self.txtBidEprice.setText(ePriceStr)
     
        if(self.txtResult12.text()==''): 
            a = 0
        else :
            a = float(self.txtResult12.text().replace(',',''))        
        sbidPrice = int((ePrice-a) * (sbidrage/100)+a)        
        sbidPricestr = format(sbidPrice,',')
#        print("투찰가격 : {}".format(sbidPricestr))
        self.txtBidPrice.setText(sbidPricestr)
        self.display15()
    
    #개찰결과 클릭시 업체명 표시하기
    def runBidSelCom(self,index):
        global dismodel2

        selitem = dismodel2.itemFromIndex(index).text()
        print(selitem)
        self.txtBidCom.setText(selitem[-11:].replace(' ',''))
        self.runSearchCom()


    # 기초금액 산출로 복사
    def addBtn(self):
        self.txtResult2_1.setText(self.txtResult5.text())
        self.comboBox2_2.setCurrentIndex(self.comboBox6.currentIndex())
        self.txtResult2_3.setText(self.txtResult7.text())
    # 복수예비가격 정렬
    def runSort(self):
        global priceList
        if(len(priceList) == 0 ): return
        if(self.checkBoxSort.checkState()):
            priceList.sort()
            self.display15()
        else:
            random.shuffle(priceList)
            self.display15()
    # 산출가격 정렬
    def runSort2(self):
        global dismodel1
        global dismodel1Str

        dismodel1.clear()

        dismodel1Str.sort()
        i=1
        for line in dismodel1Str:
            line1 = "{0: >5} : {1}".format(i,line)
            i += 1
            dismodel1.appendRow(QStandardItem(line1))

        self.listViewBidRun.setModel(dismodel1)  # lisetView에 표시하기
    def runSearchCom(self):
        global dismodel2
        global dismodel2Str
        global totalCountResult

        searchTxt = self.txtBidCom.text()
        searchNum = 0
        self.txtBidCom_2.setText("")
        self.txtBidCom_3.setText("")
        self.txtBidCom_4.setText("")
        displayStr = "개찰완료 {}개회사가 투찰하였습니다.".format(totalCountResult)
        for str in dismodel2Str:
            if searchTxt in str:
                searchNum += 1
                result = str.split('|')
                self.txtBidCom_2.setText(result[0])
                self.txtBidCom_3.setText(result[3])
                self.txtBidCom_4.setText(result[1])
                if(result[0].replace(' ','')==''):
                    self.txtBidCom_2.setText(result[6])
                displayStr = displayStr+"\n {} {} {}".format(self.txtBidCom_2.text(),result[3],result[1])
        if(searchNum ==0):
            displayStr = displayStr +"\n조회내용이 없습니다."
        else: displayStr = displayStr +"\n{}건 조회 되었습니다.".format(searchNum)
        self.labDisplay.setText(displayStr)
            

    # 공고번호로 검색
    def runSearch(self):
 #       self.txtResult1.setText(self.bidNum.text())
        global isInternet
        global bidNtceNo
        global params

        self.txtResult12.setText("")
        self.txtResult13.setText("")
        self.labAresult.setText("")
        bidNtceNo = self.bidNum.text().replace(" ","")
        bidNtceNo = bidNtceNo.strip()
        params['bidNtceNo'] = bidNtceNo
        resultOK = False

        if(bidNtceNo == ''): 
            self.labDisplay.setText("조달공고번호가 없습니다.")
            self.bidNum.setPlaceholderText('조달공고번호')  
            self.bidNum.setFocusPolicy(Qt.StrongFocus)
            return
        for index, url in enumerate(urls) :
            errStr = "공고조회"
            try :
                response = requests.get(url, params=params)
                data = json.loads(response.text)
            except requests.exceptions.Timeout as errd:
                print("{} Time out {}".format(errStr,errd))
                self.labDisplay.setText("{} Time out {}".format(errStr,errd))
                return
            except requests.exceptions.ConnectionError as errc:
                print("{} 인터넷연결안됨 {}".format(errStr,errc))
                self.labDisplay.setText("{} Time out {}".format(errStr,errc))
                return
            except requests.exceptions.HTTPError as errb:
                print("{} HTTPerror{}".format(errStr,errb))
                self.labDisplay.setText("{} Time out {}".format(errStr,errb))
                return
            except requests.exceptions.RequestException as erra:
                print("{} RequestExcepion{}".format(errStr,erra))
                self.labDisplay.setText("{} Time out {}".format(errStr,erra))
                return

            header = data['response']['header']
            body = data['response']['body']
            resultMsg = header['resultMsg']
            totalCount = body['totalCount']

            if(resultMsg =='정상' and totalCount >= 1) :
                items = body['items']
                item = items[totalCount-1]
                bidNtceNo = item['bidNtceNo']
                bidNtceNm = item['bidNtceNm']
                ntceInsttNm = item['ntceInsttNm']            # 공고기관
                cntrctCnclsMthdNm = item['cntrctCnclsMthdNm']
                sucsfbidLwltRate = item['sucsfbidLwltRate']
                opengDt = item['opengDt']
                bidBeginDt = item['bidBeginDt']
                bidClseDt = item['bidClseDt']
                bidNtceDt = item['bidNtceDt']
                bidNtceUrl = item['bidNtceUrl']

                self.txtResult1.setText(bidNtceNo)
                self.txtResult2.setText(bidNtceNm)
                self.txtResult3.setText(ntceInsttNm)
                self.txtResult4.setText(cntrctCnclsMthdNm)
                self.txtResult7.setText(sucsfbidLwltRate)
                self.txtResult8.setText(opengDt)
                self.txtResult9.setText(bidBeginDt)
                self.txtResult10.setText(bidClseDt)
                self.txtResult11.setText(urlList[index])
                self.txtInputDt.setText(bidNtceDt)
                self.txtResult1_2.setText(bidNtceUrl)
                resultOK = True

        #기초금액 구하기   (조달청 , 한국토지주택공사 기초금액 구하기 분기)
                if(ntceInsttNm=='한국토지주택공사'):
                    inputDate = bidNtceDt[:10].replace('-','')
                    print("{} 공고일자{}로검색시작".format(ntceInsttNm,inputDate))      # a[:10].replace('-','')  2022-06-28 11:00:00--> 20220628변환
                    self.bidListLH2()
                else: 
                    errStr = "조달기초금액 조회"
                    try:
                        response1 = requests.get(urlsBsisAmount[index], params=params)
                        data1 = json.loads(response1.text)
                    except requests.exceptions.Timeout as errd1:
                        print("{} Time out {}".format(errStr,errd1))
                        self.labDisplay.setText("{} Time out {}".format(errStr,errd1))
                        return
                    except requests.exceptions.ConnectionError as errc1:
                        print("{} 인터넷연결안됨 {}".format(errStr,errc1))
                        self.labDisplay.setText("{} Time out {}".format(errStr,errc1))
                        return
                    except requests.exceptions.HTTPError as errb1:
                        print("{} HTTPerror{}".format(errStr,errb1))
                        self.labDisplay.setText("{} Time out {}".format(errStr,errb1))
                        return
                    except requests.exceptions.RequestException as erra1:
                        print("{} RequestExcepion{}".format(errStr,erra1))
                        self.labDisplay.setText("{} Time out {}".format(errStr,erra1))
                        return

                    header1 = data1['response']['header']
                    body1 = data1['response']['body']
                    resultMsg1 = header1['resultMsg']
                    totalCount1 = body1['totalCount']
                    if(resultMsg1 =='정상' and totalCount1 >= 1) :
                        self.labDisplay.setText("")
                        items1 = body1['items']
                        item1 = items1[totalCount1-1]
                        bssamt = item1['bssamt']
                        rsrvtnPrceRngBgnRate = item1['rsrvtnPrceRngBgnRate']
                        rsrvtnPrceRngEndRate = item1['rsrvtnPrceRngEndRate']
                        bssAmtPurcnstcst = item1['bssAmtPurcnstcst']       #순공사원가
                        bssamtStr = format(int(bssamt),',')
                        self.txtResult5.setText(bssamtStr)
                        if(bssAmtPurcnstcst == ''): bssAmtPurcnstcstStr=''
                        else : bssAmtPurcnstcstStr = format(int(bssAmtPurcnstcst),',')
                        self.txtResult13.setText(bssAmtPurcnstcstStr)
                        self.labDisplay.setText("기초금액 : {}".format(bssamtStr))
                        # print("예가범위 {} ~ {}".format(rsrvtnPrceRngBgnRate,rsrvtnPrceRngEndRate))
                        if(rsrvtnPrceRngBgnRate == '-2') : 
                            self.comboBox6.setCurrentIndex(1)
                        if(rsrvtnPrceRngBgnRate == '-3') : 
                            self.comboBox6.setCurrentIndex(0)
                    else :
                        print("기초금액 공개 안됨")
                        self.labDisplay.setText("기초금액공개 안됨 배정예산가격입니다.")
                        asignBdgtAmt = item['asignBdgtAmt']
                        self.txtResult5.setText(asignBdgtAmt)

        if(resultOK == False) : 
            print("조달공고번호를 확인해주세요.")
            self.labDisplay.setText("조달공고번호를 확인해주세요.")
            print(self.bidNum.text())
            self.bidNum.setText("")
            self.bidNum.setPlaceholderText('조달공고번호')  
            self.bidNum.setFocusPolicy(Qt.StrongFocus)
        #A 값 구하기
        if(self.txtResult11.text() !='공사' or self.txtResult3.text()=="한국토지주택공사"): return

        errStr = "A값구하기"
        try:
            response = requests.get(urlA, params=params)
            data = json.loads(response.text)
        except requests.exceptions.Timeout as errd:
            print("{} Time out {}".format(errStr,errd))
            self.labDisplay.setText("{} Time out {}".format(errStr,errd))
            return
        except requests.exceptions.ConnectionError as errc:
            print("{} 인터넷연결안됨 {}".format(errStr,errc))
            self.labDisplay.setText("{} Time out {}".format(errStr,errc))
            return
        except requests.exceptions.HTTPError as errb:
            print("{} HTTPerror{}".format(errStr,errb))
            self.labDisplay.setText("{} Time out {}".format(errStr,errb))
            return
        except requests.exceptions.RequestException as erra:
            print("{} RequestExcepion{}".format(errStr,erra))
            self.labDisplay.setText("{} Time out {}".format(errStr,erra))
            return

        header = data['response']['header']
        body = data['response']['body']
        resultMsg = header['resultMsg']
        totalCount = body['totalCount']
        if(resultMsg =='정상' and totalCount >= 1) :
            items = body['items']
            item = items[totalCount-1]
            npnInsrprm= item['npnInsrprm']                          #": "5853653",              국민연금보험료
            mrfnHealthInsrprm= item['mrfnHealthInsrprm']            #": "4546337",              국민건강보험료
            rtrfundNon= item['rtrfundNon']                          #": "2991867",              퇴직공제부금비
            odsnLngtrmrcprInsrprm= item['odsnLngtrmrcprInsrprm']    #": "557835",               노인장기요양보험료
            sftyMngcst= item['sftyMngcst']                          #": "4659910",              산업안전보건관리비
            sftyChckMngcst= item['sftyChckMngcst']                  #": "0",                    안전관리비
            qltyMngcst= item['qltyMngcst']                          #": "0",                    품질관리비

            sum = int(npnInsrprm) + int(mrfnHealthInsrprm) + int(rtrfundNon)+ int(odsnLngtrmrcprInsrprm) + int(sftyMngcst) + int(sftyChckMngcst) + int(qltyMngcst)
            sumStr = format(sum,',')
            self.txtResult12.setText(sumStr)
            lineStr = ""
            lineStr = lineStr + "국민연금보험료     {0: >10}원\n".format(format(int(npnInsrprm),','))
            lineStr = lineStr + "국민건강보험료     {0: >10}원\n".format(format(int(mrfnHealthInsrprm),','))
            lineStr = lineStr + "퇴직공제부금비     {0: >10}원\n".format(format(int(rtrfundNon),','))
            lineStr = lineStr + "노인장기요양보험료 {0: >10}원\n".format(format(int(odsnLngtrmrcprInsrprm),','))
            lineStr = lineStr + "산업안전보건관리비 {0: >10}원\n".format(format(int(sftyMngcst),','))
            lineStr = lineStr + "안전관리비        {0: >10}원\n".format(format(int(sftyChckMngcst),','))
            lineStr = lineStr + "품질관리비        {0: >10}원\n".format(format(int(qltyMngcst),','))
            self.labAresult.setText(lineStr)
    # LH 기초금액조회  API 로 가져오기 (순공사원가 없음)
    def bidListLH(self,inputDate,bidNtceNo):
        global lhparams

        lhparams['tndrbidRegDtStart'] = inputDate
        lhparams['tndrbidRegDtEnd'] = inputDate

        errStr = "LH 기초, A값구하기"
        try:
            response = requests.get(lhUrl, params=lhparams)
            data = xmltodict.parse(response.text)
        except requests.exceptions.Timeout as errd:
            print("{} Time out {}".format(errStr,errd))
            self.labDisplay.setText("{} Time out {}".format(errStr,errd))
            return
        except requests.exceptions.ConnectionError as errc:
            print("{} 인터넷연결안됨 {}".format(errStr,errc))
            self.labDisplay.setText("{} Time out {}".format(errStr,errc))
            return
        except requests.exceptions.HTTPError as errb:
            print("{} HTTPerror{}".format(errStr,errb))
            self.labDisplay.setText("{} Time out {}".format(errStr,errb))
            return
        except requests.exceptions.RequestException as erra:
            print("{} RequestExcepion{}".format(errStr,erra))
            self.labDisplay.setText("{} Time out {}".format(errStr,erra))
            return

        print(data)
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
                self.txtResult5.setText(fdmtAmtStr)
                self.txtResult12.setText(prcscoreExclusAmtStr)
                self.comboBox6.setCurrentIndex(1)

    def bidListLH2(self):
        lhUrl2 = self.txtResult1_2.text()
        if(lhUrl2 ==""): return
        response = requests.get(lhUrl2)
        html = bs(response.text,'lxml')

        for tag in html.select('label'):
            if(tag.text == "기초금액"):
                Str = tag.next_element.next_element.next_element.text
                BPriceStr = Str[:Str.find('원')]
                self.txtResult5.setText(BPriceStr)
            if(tag.text == "가격점수제외금액(A)"):
                Str = tag.next_element.next_element.next_element.text
                APriceStr = Str[:Str.find('원')]
                self.txtResult12.setText(APriceStr)                
            if(tag.text == "낙찰제외기준금액"):
                Str = tag.next_element.next_element.next_element.text
                CPriceStr = Str[:Str.find('원')]
                self.txtResult13.setText(CPriceStr)                
        self.comboBox6.setCurrentIndex(1)
        bidKindStr = self.txtResult11.text()   # 종목구분   물품/용역/공사
        if bidKindStr =="공사": 
            bidKind1 = 0
            bidKind2 = self.comboBox11_2.currentIndex()
        elif bidKindStr =="용역": 
            bidKind1 = 1
            bidKind2 = self.comboBox11_3.currentIndex()
        elif bidKindStr =="물품": 
            bidKind1 = 2
            bidKind2 = 0
        else : return
        BPrice = int(BPriceStr.replace(',',''))
        Rate=0
        for bidR in bidRate[bidKind1][bidKind2] :
            if BPrice >= bidR[1] and BPrice < bidR[2] : Rate = bidR[0]

        if(Rate !=0):
            print("낙찰하한율 : {}".format(Rate))
            self.txtResult7.setText(str(Rate))
    # 복수예비가격 1번산출
    def runPrice1(self):
        if(self.txtResult2_1.text() == ''): 
            basePrice = 0
            if(self.txtResult5.text() != ''):
                self.addBtn()
                basePrice = int(self.txtResult2_1.text().replace(',',''))
        else : basePrice = int(self.txtResult2_1.text().replace(',',''))
        bidRate = self.comboBox2_2.currentIndex()   # 0 == 3%  1 == 2%
        global priceList
        priceList.clear()
        global dismodel1

        if(basePrice>0):
            self.labDisplay.setText("")
            for i in range(0,15):
                min = priceRate[bidRate][i][0] * basePrice
                max = priceRate[bidRate][i][1] * basePrice
                price = int(min/100)*100 + int(random.random()*(max-min)/100)*100
                priceList.append(price)
            random.shuffle(priceList)
            # 15개 예가 출력하기
            self.display15()
            time.sleep(0.05)
        else:
            print("기초금액이 없습니다.")
            self.labDisplay.setText("기초금액이 없습니다.")


    # 복수예가 15개 표시하기, 선택된곳 녹색으로
    def display15(self):
        global priceList     
        global priceSelList       
        pricestr = []
        priceStyle = []
#        a="background-color: rgb(255, 255, 255)"
#        b="background-color: rgb(5, 250, 5)"
        for i in range(0,15):
            if(priceList[i]==0): pricestr.append("")
            else : pricestr.append(format(priceList[i],','))
            if(priceSelList[i] == 0): priceStyle.append("background-color: rgb(255, 255, 255)")
            else : priceStyle.append("background-color: rgb(5, 250, 5)")
        self.txtBsis1.setText(pricestr[0])
        self.txtBsis1.setStyleSheet(priceStyle[0])
        self.txtBsis1.repaint()
        self.txtBsis2.setText(pricestr[1])
        self.txtBsis2.setStyleSheet(priceStyle[1])
        self.txtBsis3.setText(pricestr[2])
        self.txtBsis3.setStyleSheet(priceStyle[2])
        self.txtBsis4.setText(pricestr[3])
        self.txtBsis4.setStyleSheet(priceStyle[3])
        self.txtBsis5.setText(pricestr[4])
        self.txtBsis5.setStyleSheet(priceStyle[4])
        self.txtBsis6.setText(pricestr[5])
        self.txtBsis6.setStyleSheet(priceStyle[5])
        self.txtBsis7.setText(pricestr[6])
        self.txtBsis7.setStyleSheet(priceStyle[6])
        self.txtBsis8.setText(pricestr[7])
        self.txtBsis8.setStyleSheet(priceStyle[7])
        self.txtBsis9.setText(pricestr[8])
        self.txtBsis9.setStyleSheet(priceStyle[8])
        self.txtBsis10.setText(pricestr[9])
        self.txtBsis10.setStyleSheet(priceStyle[9])
        self.txtBsis11.setText(pricestr[10])
        self.txtBsis11.setStyleSheet(priceStyle[10])
        self.txtBsis12.setText(pricestr[11])
        self.txtBsis12.setStyleSheet(priceStyle[11])
        self.txtBsis13.setText(pricestr[12])
        self.txtBsis13.setStyleSheet(priceStyle[12])
        self.txtBsis14.setText(pricestr[13])
        self.txtBsis14.setStyleSheet(priceStyle[13])
        self.txtBsis15.setText(pricestr[14])
        self.txtBsis15.setStyleSheet(priceStyle[14])
        pricestr.clear()
        priceStyle.clear()

    # 투찰금액 1번산출
    def runBidPrice1(self):
        global bidNtceNo
        global dismodelTitle
        global dismodel1
        global priceNum
        global priceSelList
        global sbidrage
        global isDisplay
        global dismodel1Str
        
        priceSelList = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 ]


        if(self.txtResult2_3.text()==''): return

        bidNtceNo = self.bidNum.text().replace(" ","")
        base = self.txtResult2_1.text().replace(" ","")
        base = base.replace(",","")
        if(base==''): return
        baseprice = int(base)
        bidrate =  self.comboBox2_2.currentIndex()
        sbidrage1 = float(self.txtResult2_3.text())
        bidComNum = int(self.txtComNum.text())

        priceList = []
        bidNum = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14 ]
        bidCountReset = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        emptcheck1 = self.txtBsis1.text() =='' or self.txtBsis2.text() =='' or self.txtBsis3.text() =='' or self.txtBsis4.text() =='' or self.txtBsis5.text() ==''
        emptcheck2 = self.txtBsis6.text() =='' or self.txtBsis7.text() =='' or self.txtBsis8.text() =='' or self.txtBsis9.text() =='' or self.txtBsis10.text() ==''
        emptcheck3 = self.txtBsis11.text() =='' or self.txtBsis12.text() =='' or self.txtBsis13.text() =='' or self.txtBsis14.text() =='' or self.txtBsis15.text() ==''

        if(emptcheck1 or emptcheck2 or emptcheck3): return

        if(isDisplay == False or sbidrage != sbidrage1):
            dismodelTitle.clear()
            list1 = '=============== 낙찰율({0: >7}%) ==============='.format(sbidrage1)
            dismodelTitle.appendRow(QStandardItem(list1))  #listView라인추가
            list1 = '   No.          투찰가격  추첨번호4개    (사정율)  [기초투찰율]'
            dismodelTitle.appendRow(QStandardItem(list1))  #listView라인추가
            self.listViewBidRunTitle.setModel(dismodelTitle)  # lisetView에 표시하기        
            isDisplay = True

        sbidrage = sbidrage1
        if(sbidrage<0): return
        priceList.append(int(self.txtBsis1.text().replace(',','')))
        priceList.append(int(self.txtBsis2.text().replace(',','')))
        priceList.append(int(self.txtBsis3.text().replace(',','')))
        priceList.append(int(self.txtBsis4.text().replace(',','')))
        priceList.append(int(self.txtBsis5.text().replace(',','')))
        priceList.append(int(self.txtBsis6.text().replace(',','')))
        priceList.append(int(self.txtBsis7.text().replace(',','')))        
        priceList.append(int(self.txtBsis8.text().replace(',','')))
        priceList.append(int(self.txtBsis9.text().replace(',','')))
        priceList.append(int(self.txtBsis10.text().replace(',','')))
        priceList.append(int(self.txtBsis11.text().replace(',','')))
        priceList.append(int(self.txtBsis12.text().replace(',','')))
        priceList.append(int(self.txtBsis13.text().replace(',','')))
        priceList.append(int(self.txtBsis14.text().replace(',','')))
        priceList.append(int(self.txtBsis15.text().replace(',','')))

        if(priceList[0] == 0): return
       
        priceNum += 1
        bidCount = bidCountReset
        for i in range(0,bidComNum):
            bidSel = bidNum
            random.shuffle(bidSel)
            bidCount[bidSel[0]] += 1
            bidCount[bidSel[1]] += 1

        bidSelList = []
        for i in range(0,15):
            bidSelList.append((bidCount[i],i))   # (추첨숫자,추첨번호)

        bidSelList.sort()
        bidSelList.reverse()

        sum=0
        for i in range(4):
            sum += priceList[bidSelList[i][1]]
        ePrice = int(sum/4)

        ePriceStr = format(ePrice,',')
        self.txtBidEprice.setText(ePriceStr)
        if(self.txtResult12.text()==''): 
            a = 0
        else :
            a = float(self.txtResult12.text().replace(',',''))
#            bestBid = int((float(basePlnprc) -a) * (float(self.txtResult2_3.text())/100) + a) 
        if(self.txtResult13.text()!=''):
            bssAmtPurcnstcst = int(self.txtResult13.text().replace(",",""))
            basicPrice = int(bssAmtPurcnstcst * (ePrice/baseprice) *0.98)    # 순공사원가적용금액 = 순공사원가 * (예정가격/기총금액) * 98%
            basicPriceStr = " 순공사적용 {0}".format(format(basicPrice,',')) 
            self.labDisplay.setText(basicPriceStr)
        else: basicPrice = 0
        sbidPrice = int((ePrice-a) * (sbidrage/100)+a)
        
        sbidPricestr = format(sbidPrice,',')
        self.txtBidPrice.setText(sbidPricestr)
        
        bidS1 = round((ePrice / baseprice)*100,3)
        bidS2 = round((sbidPrice / baseprice)*100,3)

        if(basicPrice!=0 and sbidPrice < basicPrice) :
            list1 = "{0: >5} : {1: >15} ({2: >2},{3: >2},{4: >2},{5: >2}) - ({6: >7}%) [{7: >7}%] 산출{8}".format(priceNum,basicPriceStr,bidSelList[0][1]+1,bidSelList[1][1]+1,bidSelList[2][1]+1,bidSelList[3][1]+1,bidS1,bidS2,sbidPricestr)
            list2 = "{0: >15} ({1: >2},{2: >2},{3: >2},{4: >2}) - ({5: >7}%) [{6: >7}%]".format(basicPriceStr,bidSelList[0][1]+1,bidSelList[1][1]+1,bidSelList[2][1]+1,bidSelList[3][1]+1,bidS1,bidS2,sbidPricestr)
        else:
            list1 = "{0: >5} : {1: >15} ({2: >2},{3: >2},{4: >2},{5: >2}) - ({6: >7}%) [{7: >7}%]".format(priceNum,sbidPricestr,bidSelList[0][1]+1,bidSelList[1][1]+1,bidSelList[2][1]+1,bidSelList[3][1]+1,bidS1,bidS2)
            list2 = "{0: >15} ({1: >2},{2: >2},{3: >2},{4: >2}) - ({5: >7}%) [{6: >7}%]".format(sbidPricestr,bidSelList[0][1]+1,bidSelList[1][1]+1,bidSelList[2][1]+1,bidSelList[3][1]+1,bidS1,bidS2)

        if(basicPrice!=0): 
            list1 = list1+ basicPriceStr
            list2 = list2+ basicPriceStr

        dismodel1Str.append(list2)
        priceSelList[bidSelList[0][1]] = 1
        priceSelList[bidSelList[1][1]] = 1
        priceSelList[bidSelList[2][1]] = 1
        priceSelList[bidSelList[3][1]] = 1
        self.display15()
        dismodel1.appendRow(QStandardItem(list1))  #listView라인추가

        self.listViewBidRun.setModel(dismodel1)  # lisetView에 표시하기
    # 최적 산출 찾기
    def runBestBid(self):
        global dismodel1
        global dismodel1Str

        if self.txtBidFirst_4.text=="": return   # 산출하지 않거나 개찰결과 예정가격 없으면 리턴

        str2 = self.txtBidFirst_4.text()    #산출최적가
        str2 = str2[str2.find('(')+1:-1].replace(',','')
        if(str2 ==""): return
        BPrice = int(str2)
        str3 = self.txtBidFirst_3.text().replace(',','')    #1순위 낙찰금액
        APrice = int(str3)
        bestStr = ""
        for dismodelData in dismodel1Str:
            str = dismodelData.replace("순공사원가",'')
            str = str[:str.find('(')]
            str = str.replace(',','')
            sBidPrice = int(str)
            if(sBidPrice >= BPrice and sBidPrice <=APrice):     # 1순위 보다작고 산출최적가보다 크면 최적산출금액
                print("최적산출금액 {}".format(dismodelData))
                bestStr = bestStr+"최적산출금액 : "+dismodelData+'\n'
        if bestStr != '':
            self.labDisplay.setText(bestStr)
        else :
            self.labDisplay.setText("최적산출금액없음")

     # 복수예비가격 반복산출
    def runPrice1S(self):
        n = int(self.txtBsisRepNum.text())
        for j in range(0,n):
            self.runPrice1()
    #개찰결과확인하기로 공고번호 복사
    def addAlmBtn(self):
        self.bidNum_2.setText(self.txtResult1.text())
        self.txtResult8_2.setText(self.txtResult8.text())
    # 개찰 알람설정하기
    def runArm(self):
        global isArm             # 알람상태표시
        global ArmDate           # 알람 날짜
        global ArmTime           # 알람 시간
        global ArmbidNumber      # 개찰 공고번호
        atime = self.txtResult8_2.text().split(' ')
        ArmDate = atime[0]
        ArmTime = atime[1]
        ArmbidNumber = self.bidNum_2.text().replace(' ','')

        if(self.checkBoxArm.checkState()):
            isArm = True
        else:
            isArm = False
        print("Alrm is {} .. {} - {} 공고번호 {}".format(isArm,ArmDate,ArmTime,ArmbidNumber))
        
#        playfile = "action.mp3"
#        winsound.PlaySound(playfile, winsound.SND_FILENAME)
    # 1초마다 시간 갱신
    def clock(self):
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.getDateTime)
    #1초마다 시간 표기하기
    def getDateTime(self):
        global ArmDate   # 2022-06-23
        global ArmTime   #  11:00:00
        global isArm
        global ArmSecCount


        self.time = QTime.currentTime()
        self.date = QDate.currentDate()
        cTime = self.time.toString('hh:mm:ss')
        self.txtDate.setText(self.date.toString(Qt.DefaultLocaleLongDate))
        self.txtTime.setText(cTime)

        if isArm :
            cDate = self.date.toString('yyyy-MM-dd')
            formatData1 = time.strptime(cDate,"%Y-%m-%d")
            formatData2 = time.strptime(ArmDate,"%Y-%m-%d")

            cTimes = cTime.split(':')
            ArmTimes = ArmTime.split(':')
#            if(formatData1 >= formatData2 and int(ArmTimes[0])>=int(cTimes[0]) and int(ArmTimes[1])>=int(cTimes[1]) and int(ArmTimes[2])=int(cTimes[2]))       #지난공고면? 개찰결과 확인후 리턴

            if formatData1 >= formatData2:   # 같은날자이거나 지났으면
                if(int(ArmTimes[0])<=int(cTimes[0]) and int(ArmTimes[1])<=int(cTimes[1]) and int(ArmTimes[2])<=int(cTimes[2])):
                    if(ArmSecCount % 5 == 0):    # 5초마다 재실행
                        print("Arm.......... run......{}번 조회".format(int(ArmSecCount/5)+1))
                        self.runBidResultList()      # 개찰결과 확인하기
                        if(ArmSecCount ==0):
                            print("=====배달의민족주문 소리남")
                           # playsound('noti4.wav')
                    ArmSecCount += 1


    # 투찰금액 복수산출
    def runBidPrice1S(self):
        n = int(self.txtBsisRepNum_2.text())
        y = int(self.txtBsisRepNum_3.text())

        for j in range(1,n+1):
            if y!=0 :
                if j%y == 0 :
                    self.runPrice1()
            self.runBidPrice1()
    #개찰결과확인하기
    def runBidResultList(self):
        global paramsResult
        global params
        global dismodel2
        global dismodel2Tail
        global dismodel2Str
        global totalCountResult
        global isArm
        global ArmSecCount

        if(self.txtResult1.text() !='' and self.bidNum_2.text()==''):
            self.addAlmBtn()

        if(self.txtResult5.text() !='' and self.txtResult2_1.text()==''):
            self.addBtn()
        
        bidNtceNo = self.bidNum_2.text().replace(" ","")
        bidNtceNo = bidNtceNo.strip()
        paramsResult['bidNtceNo'] = bidNtceNo


        bidClsfcNo = 0
        paramsResult['bidClsfcNo'] = str(bidClsfcNo)

        if(bidNtceNo == ''): 
            self.labDisplay.setText("개찰알립공고번호가 없습니다.")
            self.bidNum_2.setPlaceholderText('조달공고번호')  
            self.bidNum_2.setFocusPolicy(Qt.StrongFocus)
            return
        startPage = 1
        dismodel2.clear()
        dismodel2Tail.clear()
        self.listViewResultList.setModel(dismodel2)  # lisetView에 표시하기

        wloop = True
        bidCount = 0
        while wloop:
            paramsResult['pageNo'] = str(startPage)
            errStr = "개찰조회"
            try:
                response = requests.get(urlResult, params=paramsResult)
                print(response.text)
                data = json.loads(response.text)
            except requests.exceptions.Timeout as errd:
                print("{} Time out {}".format(errStr,errd))
                self.labDisplay.setText("{} Time out {}".format(errStr,errd))
                return
            except requests.exceptions.ConnectionError as errc:
                print("{} 인터넷연결안됨 {}".format(errStr,errc))
                self.labDisplay.setText("{} Time out {}".format(errStr,errc))
                return
            except requests.exceptions.HTTPError as errb:
                print("{} HTTPerror{}".format(errStr,errb))
                self.labDisplay.setText("{} Time out {}".format(errStr,errb))
                return
            except requests.exceptions.RequestException as erra:
                print("{} RequestExcepion{}".format(errStr,erra))
                self.labDisplay.setText("{} Time out {}".format(errStr,erra))
                return

            header = data['response']['header']
            resultMsg = header['resultMsg']
            if(resultMsg!='정상'): return
            body = data['response']['body']
            totalCount = body['totalCount']

            if(resultMsg =='정상' and totalCount == 0) :
                if(bidClsfcNo==0): 
                    bidClsfcNo += 1
                    paramsResult['bidClsfcNo'] = str(bidClsfcNo)
                    continue
                if(bidClsfcNo ==1):
                    self.labDisplay.setText("개찰이되지 않았습니다.")
                    return
                return

            if(resultMsg =='정상' and totalCount >= 1) :
                items = body['items']
                for item in items :
                    bidCount += 1
    #                opengRsltDivNm = item['opengRsltDivNm']             #": "개찰완료",
                    bidNtceNo = item['bidNtceNo']                       #": "20220616711", 공고번호
    #                bidNtceOrd = item['bidNtceOrd']                     #": "00",    공고차수
    #                bidClsfcNo = item['bidClsfcNo']                     #": "0",     입찰분류번호
    #                rbidNo = item['rbidNo']                             #": "0",     재입찰회수
                    opengRank = item['opengRank']                       #": "1",     개찰등수
                    prcbdrBizno = item['prcbdrBizno']                   #": "1078166020",   사업자번호
                    prcbdrNm = item['prcbdrNm']                         #": "한산시피에스 주식회사",   회사이름
                    prcbdrCeoNm = item['prcbdrCeoNm']                   #": "이기웅",          대표자이름
                    bidprcAmt = item['bidprcAmt']                       #": "246918320",      투찰금액
                    bidprcrt = item['bidprcrt']                         #": "88.565",         투찰율
                    rmrk = item['rmrk']                                 #": "",               예가초과. 낙찰하한선 미달
    #                cnsttyAccotBidAmtUrl = item['cnsttyAccotBidAmtUrl'] #": "",    ?
                    drwtNo1 = item['drwtNo1']                           #": " 05",           선택번호
                    drwtNo2 = item['drwtNo2']                           #": " 02",
#                    bidprcDt = item['bidprcDt']                         #": "2022-06-20 08:45:07"
                    bidprcAmtStr = format(int(bidprcAmt),',')
                    resultStr = "{0: >3} : {1: >15} {2} {3} {4} {5} {6}".format(opengRank,bidprcAmtStr,bidprcrt,prcbdrNm,prcbdrCeoNm,prcbdrBizno,rmrk)
                    resultStr1 = "{0: >3}|{1: >15}|{2}|{3}|{4}|{5}|{6}".format(opengRank,bidprcAmtStr,bidprcrt,prcbdrNm,prcbdrCeoNm,prcbdrBizno,rmrk)
                    dismodel2.appendRow(QStandardItem(resultStr))  #listView라인추가
                    dismodel2Str.append(resultStr1)

                    if(opengRank == '1'): 
                        self.txtBidFirst.setText(prcbdrNm)
                        self.txtBidFirst_2.setText(prcbdrCeoNm)
                        self.txtBidFirst_3.setText(bidprcAmtStr)
                    if(bidCount >= totalCount): 
                        wloop = False
                self.labDisplay.setText(" - 개찰확인중 {}/{} -".format(bidCount,totalCount))
                self.labDisplay.repaint()
            startPage += 1
        self.listViewResultList.setModel(dismodel2)  # lisetView에 표시하기
        self.labDisplay.setText("개찰완료 {}개회사가 투찰하였습니다.".format(totalCount))
#        playsound("noti1.wav")
        totalCountResult = totalCount
        self.labDisplay.repaint()

        # 예가 구해오기
        bidNtceNo = self.bidNum_2.text().replace(" ","")
        bidNtceNo = bidNtceNo.strip()
        params['bidNtceNo'] = bidNtceNo
        params['numOfRows'] = '15'              # 15개 예가 한번에 가져오기
        for index,url in enumerate(urlResult2s):

            response = requests.get(url, params=params)
            data = json.loads(response.text)
            header = data['response']['header']
            body = data['response']['body']
            resultMsg = header['resultMsg']
            totalCount = body['totalCount']
            basePrice = 0  #기초금액
            basePlnprc = 0  #예정가격
            baseBidPrice = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            baseBidPriceSelNum = [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            bestPrice = [ 0,0,0,0 ]
            startBidRunTime = ""
            bestN = 0
            strline = ""
            if(resultMsg =='정상' and totalCount == 0): continue
            if(resultMsg =='정상' and totalCount >= 1) :
                items = body['items']
                for item in items:
    #                bidNtceNo = item['bidNtceNo']                                   # ": "20220616711",      공고번호
    #                bidNtceOrd = item['bidNtceOrd']                                 #": "00",
    #                bidClsfcNo = item['bidClsfcNo']                                 #": "0",
    #                rbidNo = item['rbidNo']                                         #": "0",
    #                bidNtceNm = item['bidNtceNm']                                   #": "동두천 자연휴양림 세미나실 건립 통신공사",   공고명
                    plnprc = item['plnprc']                                         #": "278797700",        예정가격
                    bssamt = item['bssamt']                                         #": "282762000",        기초금액
    #                totRsrvtnPrceNum = item['totRsrvtnPrceNum']                     #": "15",            15개
                    compnoRsrvtnPrceSno = item['compnoRsrvtnPrceSno']               #": "10",            추첨번호 10
                    bsisPlnprc = item['bsisPlnprc']                                 #": "280960900",     복수예가
                    drwtYn = item['drwtYn']                                         #": "N",            선택여부 Y -> 선택됨
                    drwtNum = item['drwtNum']                                       #": "216",           추첨횟수
    #                bidwinrSlctnAplBssCntnts = item['bidwinrSlctnAplBssCntnts']     #": "행정자치부 기준",  낙찰자선정기준
                    rlOpengDt = item['rlOpengDt']                                   #": "2022-06-20 11:12:22",  실제개찰일시
    #                bssamtBssUpNum = item['bssamtBssUpNum']                         #": "7",                기초금액기준상위갯수
    #                compnoRsrvtnPrceMkngDt = item['compnoRsrvtnPrceMkngDt']         #": "2022-06-20 11:06:42",
    #                inptDt = item['inptDt']                                         #": "2022-06-20 11:12:22",  개찰입력시간
    #                PrearngPrcePurcnstcst = item['PrearngPrcePurcnstcst']           #": ""
                    startBidRunTime = rlOpengDt
                    basePrice = bssamt
                    basePlnprc = plnprc
                    if(drwtYn=='Y'):
                        bestPrice[bestN] = int(compnoRsrvtnPrceSno)    # best추첨번호 4개
                        bestN += 1
                        selectStr = '[O]'
                    else: selectStr = '[X]'
                    i = int(compnoRsrvtnPrceSno)-1
                    baseBidPrice[i] = int(bsisPlnprc)
                    baseBidPriceSelNum[i] = int(drwtNum)
                    strline = strline + "No{0: >2} : {1: >13} ({2}) {3}  ".format(i+1,format(baseBidPrice[i],','),drwtNum, selectStr)
                    if((i+1)%2 == 0 or i+1 ==15): 
                        print(strline)
                        dismodel2Tail.appendRow(QStandardItem(strline))  #listView라인추가
                        strline = ""
                strline = "예정가격 {0} 기초금액 {1} 추첨된번호{2},{3},{4},{5}".format(format(int(basePlnprc),','), format(int(basePrice),','), bestPrice[0], bestPrice[1], bestPrice[2],bestPrice[3])
                dismodel2Tail.appendRow(QStandardItem(strline))  #listView라인추가
                strline = "==== 개찰일시 :  {0}  ====".format(startBidRunTime)
                dismodel2Tail.appendRow(QStandardItem(strline))  #listView라인추가            
                print("예정가격 {0} 기초금액 {1} 추첨된번호{2},{3},{4},{5}개찰일시 {6}".format(basePlnprc, basePrice, bestPrice[0], bestPrice[1], bestPrice[2],bestPrice[3], startBidRunTime))
                self.listViewResultListTail.setModel(dismodel2Tail)  # lisetView에 표시하기
                if (self.txtResult12.text().replace(',','') == ''): a=0
                else : a = float(self.txtResult12.text().replace(',',''))
                bestBid = int((float(basePlnprc) -a) * (float(self.txtResult2_3.text())/100) + a) 
                strline = "{0}({1})".format(format(int(basePlnprc),','), format(bestBid,','))
                self.txtBidFirst_4.setText(strline)
                isArm = False
                ArmSecCount = 0


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.bidNum.setFocus()
    myWindow.show()
    sys.exit(app.exec_()) 