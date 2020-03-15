import os,sys,time,json
from bs4 import BeautifulSoup as parse
from base64 import b64decode as wkwk
import requests as r
G = '\x1b[0;32m'
GL = '\x1b[32;1m'
B = '\x1b[0;36m'
P = '\x1b[35;1m'
BL = '\x1b[36;1m'
BD = '\x1b[34;1m'
R = '\x1b[31;1m'
W = '\x1b[37;1m'
H = '\x1b[30;1m'
Y = '\x1b[33;1m'
YL = '\x1b[1;33m'
# ---------------------- SEBUAH TOOLS YANG BERFUNGSI ----------------
# ------------------------ UNTUK MENDOWNLOAD VIDEO --------------------
# -------------------------FACEBOOK DAN INSTAGRAM. ------------------
def runntek(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10.0 / 100)

def instagram():
	url = raw_input('\nURL : ')
	xxx = raw_input('\nDownload? (y/n) ')
	if 'y' in xxx:
		bra = raw_input('Output : ')
		print('{}\n[!] Loading...'.format(R))
		save = r.get(url).text
		soup = parse(save, 'html.parser')
		love = soup.findAll('script', type='text/javascript')
		for heart in love:
			if 'window._sharedData = ' in heart.text:
				pakboi = heart.text.replace('window._sharedData = ','').replace(';','')
		pakboi = json.loads(pakboi)
		pakboi = pakboi["entry_data"]['PostPage'][0]["graphql"]['shortcode_media']["video_url"]
#		print('{}[!] Sedang Mendownload...'.format(R))
		time.sleep(7)
		pakgerl = r.get(pakboi)
		pants = open(bra, 'wb')
		pants.write(pakgerl.content)
		pants.close
		print('{}[!] Download Berhasil'.format(GL))
		time.sleep(3)
		print('{}\n[!] Salin File ke internal'.format(R))
		time.sleep(3)
		print('{}[!] Berhasil\n\n\n{}Periksa Pada Internal!!!'.format(GL,BL))
		time.sleep(2)
		os.system('cp '+bra+' /sdcard && rm -rf '+bra)


def about_program():
	os.system('clear')
	runntek(wkwk('Ck5hbWUgICAgOiAgSW5zdGFGYWNlClZlcnNpb24gOiAgMS4wCkF1dGhvciAgOiAgc0N1YnkwNwpUZWFtICAgIDogIEN5YmVyIEdob3N0IElEClRoYW5rcyAgOiAgQWxsYWggU1dULCBNYXJrIFp1Y2tlcmJlcmcsCgkgICBKdXN0YUhhY2tlcgoKSW5mbyAgICA6ICBJbnN0YUZhY2UgaXMgdG9vbCBkb3dubG9hZGluZwogICAgICAgICAgIEluc3RhZ3JhbSB2aWRlb3MgYW5kIEZhY2Vib29rCgpOb3RlICAgIDogIHBsZWFzZSBkbyBub3Qgc2VsbCBhbmQgYnV5IHRoaXMgdG9vbC4KICAgICAgICAgICB0aGlzIHRvb2wgaXMgMTAwJSBmcmVlLgogICAgICAgICAgIElmIHlvdSBmaW5kIHNvbWVvbmUgd2hvIHRyYWRlcyB0aGlzIHRvb2wKICAgICAgICAgICBwbGVhc2UgcmVwb3J0IHRvIG1lLgoKwqkgMjAyMCBzQ3VieTA3LCBDeWJlciBHaG9zdCBJbmRvbmVzaWE='))



def facebook():
     try:
	url = raw_input('\nURL : ')
        xxx = raw_input('\nDownload? (y/n) ')
        if 'y' in xxx:
		bra = raw_input('Output : ')
		print('{}\n[!] Loading...'.format(R))
	        save = r.get(url).text
#       	print save
        	sop = parse(save, "html.parser")
        	res = sop.find("script", type="application/ld+json")
	        a = json.loads(res.text)
        	b = a['contentUrl']
		time.sleep(7)
	        c = r.get(b)
	        d = open(bra, 'wb')
	        d.write(c.content)
	        d.close
	        print('{}[!] Download Berhasil'.format(GL))
                time.sleep(3)
                print('{}\n[!] Salin File ke Internal'.format(R))
                time.sleep(3)
                print('{}[!] Berhasil\n\n\n{}PERIKSA PADA INTERNAL!!!'.format(GL,BL))
                time.sleep(2)
                os.system('cp '+bra+' /sdcard && rm -rf '+bra)
     except KeyboardInterrupt:
                exit()
     except:
                print('URL TIDAK VALID')
                time.sleep(int("2"))
                os.system('python2 main.py')

def contact():
	os.system('xdg-open https://api.whatsapp.com/send?phone=6283813844572 && python2 main.py')


if __name__ == '__main__':
	os.system('clear')  
	print('''{}
  Coded By Mr.Tcg Cyber{} v1.0{}
       VIDEOS DOWNLOADER
'''.format(BL,YL,P))
	print('''

{}Perintah	Informasi
{}--------	---------{}
igvid		untuk mengunduh video instagram
fbvid		untuk mengunduh video facebook
tentang		tunjukkan tentang program ini
kontak  	Chat Whatsapp admin
update		perbarui Script ini
keluar		keluar dari script ini\n'''.format(BL,P,W))

	while True:

		nanya = raw_input('{}>> {}'.format(BL,W))
		if nanya == 'igvid':
			instagram()
		elif nanya == 'fbvid':
			facebook()
		elif nanya == 'tantang':
			about_program()
		elif 'kontak' in nanya:
			contact()
		elif 'update' in nanya:
			print('Tunggu Saja pembaruan belum tersedia')
			time.sleep(3)
			os.system('python2 main.py')
		elif nanya == 'keluar':
			exit('Bye!')
		else:
			print('{}{}: Tolol perintah tidak ditemukan'.format(R,nanya))
			pass
