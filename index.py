#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
import simplejson
import re

def main():
    # headers = {
    #     'Host':"www.lagou.com",
    #     'Referer': 'https://www.lagou.com/',
    #     'Upgrade-Insecure-Requests': '1',
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    #     'Cookie': 'user_trace_token=20191120103233-a10fd437-b870-4ce9-9a8c-99acb4ecb82a; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574217154; _ga=GA1.2.240190412.1574217154; _gat=1; PRE_UTM=m_cf_cpt_baidu_pcbt; PRE_HOST=sp0.baidu.com; PRE_SITE=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZNKw_0PpN-0FNkUsaOGIwI00000AZkiNC00000IrdrOZ.THL0oUhY1x66dIjA80K85HcdnjDLnjc1g1DsgvwM0ZnquWm4PjTzPAfsnj0kPHKWn0Kd5RRLrjcknjT1PYnswbFafWKAfbm1rjDLf1NAfYwAfYnz0ADqI1YhUyPGujY1nWbYrjD4PjmvFMKzUvwGujYkP6K-5y9YIZK1rBtEILILQhk9uvqdQhPEUiq_my4bpy4MQgK9uvRETAnETvN9ThPCQh9YUysOIgwVgLPEIgFWuHdVgvPhgvPsI7qBmy-bINqsmvFY0APzm1YkP10vnf%26tpl%3Dtpl_11534_19968_16032%26l%3D1514795361%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%25258B%252589%2525E5%25258B%2525BE%2525E7%2525BD%252591%2525E3%252580%252591-%252520%2525E9%2525AB%252598%2525E8%252596%2525AA%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E5%2525AE%25259E%2525E6%252597%2525B6%2525E6%25259B%2525B4%2525E6%252596%2525B0%21%2526xp%253Did%28%252522m3294819466_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D219%26wd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%2520%25E6%258B%259B%25E8%2581%2598%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3D25017023_10_dg%26inputT%3D2384%26prefixsug%3Dlagouwang%26rsp%3D1; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpt_baidu_pcbt; LGSID=20191120103234-0272b102-0b3e-11ea-a68b-525400f775ce; LGUID=20191120103234-0272b309-0b3e-11ea-a68b-525400f775ce; _gid=GA1.2.364304413.1574217157; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e86a789d6586-0d219b01c82b87-4e480521-2073600-16e86a789d798b%22%2C%22%24device_id%22%3A%2216e86a789d6586-0d219b01c82b87-4e480521-2073600-16e86a789d798b%22%7D; sajssdk_2015_cross_new_user=1; gate_login_token=75017162d160419d4a962b2e0a253986f19c70d174b4852a; LG_LOGIN_USER_ID=0190221121acaad343273e19fb4f14aae0b02c6e4499d78c; LG_HAS_LOGIN=1; _putrc=3B239197FEEC044F; JSESSIONID=ABAAABAAADEAAFIC48CF1F0A653B1C66C4A9E48CC5307D5; login=true; unick=%E8%B0%B7%E5%A3%AB%E5%85%83; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=18; privacyPolicyPopup=false; index_location_city=%E4%B8%8A%E6%B5%B7; WEBTJ-ID=20191120103258-16e86a7ddbd456-06cdb4f2c7ef28-4e480521-2073600-16e86a7ddbe367; SEARCH_ID=e9c3f93e08bb4e65ba03605379ecded9; X_HTTP_TOKEN=614e6a1dee34c3525817124751348e8e88dcdb23dc; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1574217184; LGRID=20191120103305-14b73639-0b3e-11ea-a635-5254005c3644; TG-TRACK-CODE=search_code'
    # }
    # result = requests.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',headers=headers)
    # print result.content.decode('utf-8','ignore')
    headers = {
        'Referer':"https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%e4%bb%a3%e8%b4%ad&clk1=33f24d3000da24d0a53c319935ca7a35&upsid=33f24d3000da24d0a53c319935ca7a35",
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
        'Cookie':'miid=8365179831855765709; thw=cn; cna=/3dxE+gSvmsCAd2CV2mCrrzg; t=e5b0f1704d6f0521714639b0c935fd21; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5hmBfZQFVptEdGaF4%2FlYmS5OG8PlMBmKhId8fbVulkKIb1QgQy3DtEPjK7aNjdSgLNne7TmrrN501n83NIyOHwkCVLMKaLtEWw4uaoW%2F5Jhl2CfLIMUS6PXTN5VraUo8%2Fh0W7OQVstkvKOOtDi5OUi7EmdMhnPRHWWXjEudGkrVeQmqknHRkUGkqi2KjkePLHUHLYrvF1Q2IbBUPFgv%2FaT7itRYROlxxuy1CduTVkeLR3cwipeOokDHWo5nPec%3D; cookie2=1c2fa9120b0d82ca8af58a13e23a1a28; v=0; _tb_token_=fe753e3eb863b; _m_h5_tk=4f8f67b1ecccebd120bade3c8ad32f03_1574231227115; _m_h5_tk_enc=24559fb9ffc7d00c742b9285f91f3ea3; isg=BMLCvZs-K0kRmzA5fpalgLjcE8jkO2HLfkC20wzbfjXgX2PZ9Cf2vSXeDxuGCz5F; l=dBaDkqjPvMpKAjPKBOfZNuIR9rbOuIRb8oVzw4i5VICP9TfH5IrAWZp8AxTMCnGVn6z2R3zGvDD7BvYRsyIWnNqMhb293OIm3d6G.',
    }

    result = requests.get('https://h5api.m.taobao.com/h5/mtop.alimama.union.sem.landing.pc.items/1.0/?jsv=2.4.0&appKey=12574478&t=1574222237535&sign=f6db343235e51576f19d02fd8df1acc1&api=mtop.alimama.union.sem.landing.pc.items&v=1.0&AntiCreep=true&dataType=jsonp&type=jsonp&ecode=0&callback=mtopjsonp1&data=%7B%22keyword%22%3A%22%E4%BB%A3%E8%B4%AD%22%2C%22ppath%22%3A%22%22%2C%22loc%22%3A%22%22%2C%22minPrice%22%3A%22%22%2C%22maxPrice%22%3A%22%22%2C%22ismall%22%3A%22%22%2C%22ship%22%3A%22%22%2C%22itemAssurance%22%3A%22%22%2C%22exchange7%22%3A%22%22%2C%22custAssurance%22%3A%22%22%2C%22b%22%3A%22%22%2C%22clk1%22%3A%2233f24d3000da24d0a53c319935ca7a35%22%2C%22pvoff%22%3A%22%22%2C%22pageSize%22%3A%22100%22%2C%22page%22%3A%22%22%2C%22elemtid%22%3A%221%22%2C%22refpid%22%3A%22mm_26632258_3504122_32538762%22%2C%22pid%22%3A%22430673_1006%22%2C%22featureNames%22%3A%22spGoldMedal%2CdsrDescribe%2CdsrDescribeGap%2CdsrService%2CdsrServiceGap%2CdsrDeliver%2C%20dsrDeliverGap%22%2C%22ac%22%3A%22%2F3dxE%2BgSvmsCAd2CV2mCrrzg%22%2C%22wangwangid%22%3A%22%22%2C%22catId%22%3A%22%22%7D',headers=headers)
    
    p1 = re.compile(r'[(](.*?)[)]', re.S)
    json_result = re.findall(p1, result.content)[0]
    line = simplejson.dumps(json_result)
    with open('taobao.json','w') as fp:
        fp.write(line.encode('utf-8'))
    

if __name__ == '__main__':
    main()