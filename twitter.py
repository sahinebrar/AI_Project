from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import re
import json
import sys
import zipfile as zf

reload(sys)
sys.setdefaultencoding('utf-8')
ckey= 'jhfbZCC9qVVC63zxEzL0ZWr6s'
csecret= 'SMxNXNssCjTg1FlkmwenZU8qRB4L2Bhp1YpELxQXFQ3KRDoTc5'
atoken= '941382106453770240-Xlx8u9bjxHAWV8ilD0sqJeCWrvGYxpq'
asecret= '3zX7mtsnEUczWakeIBY1tkap8l4W3oQaJvvPQ94SHJtM6'

hashtag = raw_input("Hangi hashtag altindaki verileri almak istiyorsunuz? \n")
type(hashtag)
print 'Tweet ler aliniyor ve csv dosyasina yaziliyor..'
class listener(StreamListener):
    def on_data(self, raw_data):
        try:

            saveFile = open('twitterData.sh','a')
            j= json.loads(raw_data)
            words = str(j['text']).split(" ")

            for word in words:  # Second Example
                word = ''.join([i if ord(i) < 128 else ' ' for i in word])

                word = re.sub(r'^https?:\/\/.*[\r\n]*', '', word, flags=re.MULTILINE)
                print word
                saveFile.write(word)
                saveFile.write('\n')
            saveFile.close()

            with zf.ZipFile('text8.zip', 'w') as myzip:
                myzip.write('twitterData.sh')
            return True

        except BaseException, e:
            print 'failed on_data',str(e)
            #time.sleep(5)


    def on_error(self, status_code):
        print status_code

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=[hashtag])
