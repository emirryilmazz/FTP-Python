from ftplib import FTP

ftp = FTP('')
ftp.connect('localhost',1026)
ftp.login("user","123456")

# giriş/çıkış yapma +
# dizindeki dosyaları listeleme +
# dizin değiştirme +
# dosya/klasör adı değiştirme +
# dosya/klasör silme +
# klasör/dosya oluşturma +
# klasör/dosya indirme
# klasör/dosya upload

def get_dir (dir_name = ''):
    if dir_name == '':
        return ftp.retrlines('LIST')
    else:
        dir_name = '/' + dir_name
        return ftp.dir(dir_name)

def change_dir (dir_name = ''):
    return ftp.cwd(dir_name)

# Directory
def mk_dir (dir_name):
    dir_name = '/' + dir_name
    return ftp.mkd(dir_name)
def rm_dir (dir_name):
    dir_name = '/' + dir_name
    return ftp.rmd(dir_name)
def rename (fromname, toname):
    return ftp.rename(fromname, toname)

def get_path ():
    return ftp.pwd()

# file
def rm_file (file_name, dir_name = ''):
    # dir_name = '/' + dir_name
    return ftp.delete(file_name)
def dosyaYukle():
    dosyaadi = 'testfile.txt' # Yüklenecek dosya adı
    ftp.storbinary('STOR '+dosyaadi, open(dosyaadi, 'rb'))
    ftp.quit()

def dosyaIndir():
    dosyaadi = 'testfile.txt' # İndirilecek dosya adı
    dosya = open(dosyaadi, 'wb')
    ftp.retrbinary('RETR ' + dosyaadi, dosya.write, 1024)
    ftp.quit()
    dosya.close()

get_dir()
print(get_path())
ftp.delete()
#dosyaIndir()
