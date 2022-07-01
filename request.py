import requests
headers = {'User-Agent': 'Mozilla/5.0'} 
timeout = 5

def get_stock(symbol):
      url = 'https://ac.finance.naver.com/ac?q=%s&q_enc=euc-kr&t_koreng=1&st=111&r_lt=111' % symbol
      return requests.post(url,headers=headers, timeout=timeout)
if __name__ == '__main__':
      r = get_stock("ACTC")
      print(r.status_code)
      print(r.headers)
      print("\n==========TEXT")
      print("text - %s " % r.text[:100]) #UTF-8로 인코딩된 문자열
      print("type - %s " % type(r.text))
      print("\n==========CONTENT")
      print("type - %s" %  type(r.content))
      print("content -  %s" % r.content[:100])      
      print("\n==========JSON")
      print("type - %s" %  type(r.json()))
      print("text - %s " % r.json()['query'])
      print("\n==========EnCoding")
      print("encoding - %s" %r.encoding)
      r.encoding = 'ISO-8859-1'
      print("\nencoding - %s" %r.encoding)