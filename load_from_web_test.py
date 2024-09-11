import requests as req
import pandas as pd


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
def loadStockHistory(sName='شپنا', howLong=0):
        webUid=getStockWbId(sName)
        #7745894403636165
        linkUrl = f"https://cdn.tsetmc.com/api/ClosingPrice/GetClosingPriceDailyListCSV/{webUid}/S*Isf.%20Oil%20Ref.Co."
        urlget=req.get(linkUrl,headers=headers)
        return  urlget.text

def getStockWbId(sName='شپنا'):
        srch_key = sName
        srch_page = req.get(f'http://cdn.tsetmc.com/api/Instrument/GetInstrumentSearch/{srch_key}', headers=headers)
        srch_res = pd.DataFrame(srch_page.json()['instrumentSearch'])
        srch_res = srch_res[['lVal18AFC', 'lVal30', 'insCode', 'lastDate', 'cgrValCot']]
        return (srch_res.iloc[0, 2])

def parseFromWebCsv(textCsv):
    lines=textCsv.split('\n')
    iCols=lines[0].split(',')
    iCols[11]=iCols[11].strip('\r')
    as1=pd.DataFrame(columns=tuple(iCols))
    iLen= len(lines)
    for i in range(1,10):#change range(1,len(lines)):
        beta = (lines[i]).split(',')
        if beta !=['']:
            as1.loc[i]=beta
    return as1

symbolData = 'خودرو'
codeSymbol = 'IRO1IKCO0001'
startDate = '13940101'
endDate = '14030618'
symbCode = 'IRO1IKCO0001'

postdata={'symboldatapara':symbolData,'inscodesymbol':codeSymbol,'symbolStart':startDate,'symbolEnd':endDate,'symb':symbCode}
#postdata={'symboldatapara':'خودرو','inscodesymbol':'IRO1IKCO0001','symbolStart':'13940101','symbolEnd':'14030618','symb':'IRO1IKCO0001'}

#"https://www.fipiran.com/DataService/Exportsymbol?symboldatapara=خودرو&inscodesymbol=IRO1IKCO0001&symbolStart=13940101&symbolEnd=14030618&symb=IRO1IKCO0001"#excell
def getFromFIPIRAN(postdata):
        linkUrl = "https://www.fipiran.com/DataService/Exportsymbol"  # excell
        urlload = req.post(linkUrl, postdata)  # true
        return urlload.text

def parsFipiranData(fipTxt):
        #Please meke yor Code to parsing response Excel Response here
        pass

#test get Data from FIPIRAN
textFipiran=getFromFIPIRAN(postdata)
print(textFipiran)
parsFipiranData(textFipiran)


#test get Data from tsetmc.com
tmcTxt=loadStockHistory("خودرو")
myDataFram=parseFromWebCsv(tmcTxt)
print(myDataFram)