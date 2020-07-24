import requests
import json
total = requests.get('http://qq.laohuan.art:8000/')
total_ip = json.loads(total.text)

'''
参数
Name	Type	Description
types	int	0: 高匿,1:匿名,2 透明
protocol int	0: http, 1 https, 2 http/https
count	int	数量
country	str	取值为 国内, 国外
area	str	地区
'''
r = requests.get('http://qq.laohuan.art:8000/')
ip_ports = json.loads(r.text)
print("共有【%d】个代理,已筛选[%d]个代理。" % (len(total_ip),len(ip_ports)))
print("---" * 8)
for i in ip_ports:
    print("http"+" "+str(i[0])+" "+str(i[1]))


'''
proxies={
    'http':'http://%s:%s'%(ip,port),
    'https':'http://%s:%s'%(ip,port)
}
r = requests.get('http://ip.chinaz.com/',proxies=proxies)
r.encoding='utf-8'
print r.text
'''