# a simple tool to optimize Clash subscribe.
from flask import Flask
import requests

app = Flask(__name__)

# your subscribe url
url = "https://..."
# your subscribe proxy string, default 'Proxy'.
# if you change this, maybe you need to change the string 'Proxy' in rule0...rule4.
name_Proxy = '  name: Proxy'

rule0 = '''-
  name: Domestic
  type: select
  proxies:
    - DIRECT
    - Proxy
-
  name: Others
  type: select
  proxies:
    - Proxy
    - Domestic'''
rule1 ='''Rule:
# China Area Network
# > Microsoft
- DOMAIN-SUFFIX,microsoft.com,Domestic
- DOMAIN-SUFFIX,windows.net,Domestic
- DOMAIN-SUFFIX,sfx.ms,Domestic
- DOMAIN-SUFFIX,sharepoint.com,Domestic
- DOMAIN-KEYWORD,officecdn,Domestic
# > Blizzard
- DOMAIN-SUFFIX,blizzard.com,Domestic
- DOMAIN-SUFFIX,battle.net,Domestic
- DOMAIN,blzddist1-a.akamaihd.net,Domestic
# > Steam
- DOMAIN-SUFFIX,steampowered.com,Domestic
- DOMAIN-SUFFIX,steam-chat.com,Domestic
- DOMAIN-KEYWORD,steamcdn,Domestic
- DOMAIN-KEYWORD,steamstore,Domestic
- DOMAIN-KEYWORD,steamuserimages,Domestic
- DOMAIN-KEYWORD,steambroadcast,Domestic
# > Tencent
#USER-AGENT,MicroMessenger%20Client,Domestic
#USER-AGENT,WeChat*,Domestic
- DOMAIN-SUFFIX,qq.com,Domestic
- DOMAIN-SUFFIX,qpic.cn,Domestic
- DOMAIN-SUFFIX,tencent.com,Domestic
# > Alibaba
- DOMAIN-SUFFIX,alibaba.com,Domestic
- DOMAIN-SUFFIX,alicdn.com,Domestic
- DOMAIN-SUFFIX,amap.com,Domestic
- DOMAIN-SUFFIX,dingtalk.com,Domestic
- DOMAIN-SUFFIX,taobao.com,Domestic
- DOMAIN-SUFFIX,tmall.com,Domestic
- DOMAIN-SUFFIX,ykimg.com,Domestic
- DOMAIN-SUFFIX,youku.com,Domestic
- DOMAIN-SUFFIX,xiami.com,Domestic
- DOMAIN-SUFFIX,xiami.net,Domestic
# > NetEase
- DOMAIN-SUFFIX,163.com,Domestic
- DOMAIN-SUFFIX,126.net,Domestic
- DOMAIN-SUFFIX,163yun.com,Domestic
# > Sohu
- DOMAIN-SUFFIX,sohu.com.cn,Domestic
- DOMAIN-SUFFIX,itc.cn,Domestic
- DOMAIN-SUFFIX,sohu.com,Domestic
- DOMAIN-SUFFIX,v-56.com,Domestic
# > Sina
- DOMAIN-SUFFIX,weibo.com,Domestic
- DOMAIN-SUFFIX,weibo.cn,Domestic
# > JD
- DOMAIN-SUFFIX,jd.com,Domestic
- DOMAIN-SUFFIX,jd.hk,Domestic
- DOMAIN-SUFFIX,360buyimg.com,Domestic
# > MI
- DOMAIN-SUFFIX,duokan.com,Domestic
- DOMAIN-SUFFIX,mi-img.com,Domestic
- DOMAIN-SUFFIX,mifile.cn,Domestic
- DOMAIN-SUFFIX,xiaomi.com,Domestic
# > bilibili
- DOMAIN-SUFFIX,acgvideo.com,Domestic
- DOMAIN-SUFFIX,bilibili.com,Domestic
- DOMAIN-SUFFIX,hdslb.com,Domestic
# > iQiyi
- DOMAIN-SUFFIX,iqiyi.com,Domestic
- DOMAIN-SUFFIX,iqiyipic.com,Domestic
- DOMAIN-SUFFIX,71.am.com,Domestic
# > HunanTV
- DOMAIN-SUFFIX,hitv.com,Domestic
- DOMAIN-SUFFIX,mgtv.com,Domestic
# > Meitu
- DOMAIN-SUFFIX,meitu.com,Domestic
- DOMAIN-SUFFIX,meitudata.com,Domestic
- DOMAIN-SUFFIX,meipai.com,Domestic
# > YYeTs
- DOMAIN-SUFFIX,zmzapi.com,Domestic
- DOMAIN-SUFFIX,zimuzu.tv,Domestic
- DOMAIN-SUFFIX,zmzfile.com,Domestic
- DOMAIN-SUFFIX,zmzapi.net,Domestic
# > 蛋蛋赞
- DOMAIN-SUFFIX,baduziyuan.com,Domestic
- DOMAIN-SUFFIX,com-hs-hkdy.com,Domestic
- DOMAIN-SUFFIX,czybjz.com,Domestic
- DOMAIN-SUFFIX,dandanzan.com,Domestic
- DOMAIN-SUFFIX,fjhps.com,Domestic
- DOMAIN-SUFFIX,kuyunbo.club,Domestic
# > Baidu
- DOMAIN-SUFFIX,baidu.com,Domestic
- DOMAIN-SUFFIX,baidubcr.com,Domestic
- DOMAIN-SUFFIX,bdstatic.com,Domestic
# > ChinaNet
- DOMAIN-SUFFIX,189.cn,Domestic
- DOMAIN-SUFFIX,21cn.com,Domestic
# > ByteDance
- DOMAIN-SUFFIX,bytecdn.cn,Domestic
- DOMAIN-SUFFIX,pstatp.com,Domestic
- DOMAIN-SUFFIX,snssdk.com,Domestic
- DOMAIN-SUFFIX,toutiao.com,Domestic
# > Content Delivery Network
# > Akamai
- DOMAIN-SUFFIX,akadns.net,Domestic
# - DOMAIN-SUFFIX,akamai.net,Domestic
# - DOMAIN-SUFFIX,akamaiedge.net,Domestic
# - DOMAIN-SUFFIX,akamaihd.net,Domestic
# - DOMAIN-SUFFIX,akamaistream.net,Domestic
# - DOMAIN-SUFFIX,akamaized.net,Domestic
# > ChinaNetCenter
- DOMAIN-SUFFIX,chinanetcenter.com,Domestic
- DOMAIN-SUFFIX,wangsu.com,Domestic
# > IP Query
- DOMAIN-SUFFIX,ipip.net,Domestic
- DOMAIN-SUFFIX,ip.cn,Domestic
- DOMAIN-SUFFIX,ip.la,Domestic
- DOMAIN-SUFFIX,ip-cdn.com,Domestic
- DOMAIN-SUFFIX,ipv6-test.com,Domestic
- DOMAIN-SUFFIX,test-ipv6.com,Domestic
- DOMAIN-SUFFIX,whatismyip.com,Domestic
- DOMAIN,ip.bjango.com,Domestic
# > Other
- DOMAIN-SUFFIX,40017.cn,Domestic
- DOMAIN-SUFFIX,broadcasthe.net,Domestic
- DOMAIN-SUFFIX,cailianpress.com,Domestic
- DOMAIN-SUFFIX,chdbits.co,Domestic
- DOMAIN-SUFFIX,chushou.tv,Domestic
- DOMAIN-SUFFIX,cmbchina.com,Domestic
- DOMAIN-SUFFIX,cmbimg.com,Domestic
- DOMAIN-SUFFIX,cmct.tv,Domestic
- DOMAIN-SUFFIX,cmvideo.cn,Domestic
- DOMAIN-SUFFIX,cnlang.org,Domestic
- DOMAIN-SUFFIX,doubanio.com,Domestic
- DOMAIN-SUFFIX,douyu.com,Domestic
- DOMAIN-SUFFIX,douyucdn.cn,Domestic
- DOMAIN-SUFFIX,dxycdn.com,Domestic
- DOMAIN-SUFFIX,hicloud.com,Domestic
- DOMAIN-SUFFIX,hdchina.org,Domestic
- DOMAIN-SUFFIX,hdcmct.org,Domestic
- DOMAIN-SUFFIX,ithome.com,Domestic
- DOMAIN-SUFFIX,kkmh.com,Domestic
- DOMAIN-SUFFIX,ksosoft.com,Domestic
- DOMAIN-SUFFIX,maoyun.tv,Domestic
- DOMAIN-SUFFIX,meituan.net,Domestic
- DOMAIN-SUFFIX,mobike.com,Domestic
- DOMAIN-SUFFIX,mubu.com,Domestic
- DOMAIN-SUFFIX,myzaker.com,Domestic
- DOMAIN-SUFFIX,ourbits.club,Domestic
- DOMAIN-SUFFIX,passthepopcorn.me,Domestic
- DOMAIN-SUFFIX,paypal.com,Domestic
- DOMAIN-SUFFIX,paypalobjects.com,Domestic
- DOMAIN-SUFFIX,privatehd.to,Domestic
- DOMAIN-SUFFIX,redacted.ch,Domestic
- DOMAIN-SUFFIX,ruguoapp.com,Domestic
- DOMAIN-SUFFIX,smzdm.com,Domestic
- DOMAIN-SUFFIX,sogou.com,Domestic
- DOMAIN-SUFFIX,teamviewer.com,Domestic
- DOMAIN-SUFFIX,totheglory.im,Domestic
- DOMAIN-SUFFIX,tp.m-team.cc,Domestic
- DOMAIN-SUFFIX,udacity.com,Domestic
- DOMAIN-SUFFIX,xmcdn.com,Domestic
- DOMAIN-SUFFIX,yangkeduo.com,Domestic
- DOMAIN-SUFFIX,zhihu.com,Domestic
- DOMAIN-SUFFIX,zhimg.com,Domestic
#USER-AGENT,NeteaseMusic*,Domestic
#USER-AGENT,%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90*,Domestic

# > SJTU
- DOMAIN-SUFFIX,sjtu.edu.cn,Domestic

# > Personal
- DOMAIN-SUFFIX,yukisaki.io,Domestic
- DOMAIN-SUFFIX,sjtuacm.com,Domestic

# (DNS Cache Pollution Protection)
# > Google
- DOMAIN-SUFFIX,appspot.com,Proxy
- DOMAIN-SUFFIX,blogger.com,Proxy
- DOMAIN-SUFFIX,getoutline.org,Proxy
- DOMAIN-SUFFIX,gvt0.com,Proxy
- DOMAIN-SUFFIX,gvt1.com,Proxy
- DOMAIN-SUFFIX,gvt3.com,Proxy
- DOMAIN-SUFFIX,xn--ngstr-lra8j.com,Proxy
- DOMAIN-KEYWORD,google,Proxy
- DOMAIN-KEYWORD,blogspot,Proxy
# > Facebook
- DOMAIN-SUFFIX,cdninstagram.com,Proxy
- DOMAIN-SUFFIX,fb.com,Proxy
- DOMAIN-SUFFIX,fb.me,Proxy
- DOMAIN-SUFFIX,fbaddins.com,Proxy
- DOMAIN-SUFFIX,fbcdn.net,Proxy
- DOMAIN-SUFFIX,fbsbx.com,Proxy
- DOMAIN-SUFFIX,fbworkmail.com,Proxy
- DOMAIN-SUFFIX,instagram.com,Proxy
- DOMAIN-SUFFIX,m.me,Proxy
- DOMAIN-SUFFIX,messenger.com,Proxy
- DOMAIN-SUFFIX,oculus.com,Proxy
- DOMAIN-SUFFIX,oculuscdn.com,Proxy
- DOMAIN-SUFFIX,rocksdb.org,Proxy
- DOMAIN-SUFFIX,whatsapp.com,Proxy
- DOMAIN-SUFFIX,whatsapp.net,Proxy
- DOMAIN-KEYWORD,facebook,Proxy
# > Twitter
- DOMAIN-SUFFIX,pscp.tv,Proxy
- DOMAIN-SUFFIX,periscope.tv,Proxy
- DOMAIN-SUFFIX,t.co,Proxy
- DOMAIN-SUFFIX,twimg.co,Proxy
- DOMAIN-SUFFIX,twimg.com,Proxy
- DOMAIN-SUFFIX,twitpic.com,Proxy
- DOMAIN-SUFFIX,vine.co,Proxy
- DOMAIN-KEYWORD,twitter,Proxy
# > Telegram
- DOMAIN-SUFFIX,t.me,Proxy
- DOMAIN-SUFFIX,tdesktop.com,Proxy
- DOMAIN-SUFFIX,telegra.ph,Proxy
- DOMAIN-SUFFIX,telegram.me,Proxy
- DOMAIN-SUFFIX,telegram.org,Proxy
# > Line
- DOMAIN-SUFFIX,line.me,Proxy
- DOMAIN-SUFFIX,line-apps.com,Proxy
- DOMAIN-SUFFIX,line-scdn.net,Proxy
- DOMAIN-SUFFIX,naver.jp,Proxy
# > Other
- DOMAIN-SUFFIX,4shared.com,Proxy
- DOMAIN-SUFFIX,881903.com,Proxy
- DOMAIN-SUFFIX,abc.net.au,Proxy
- DOMAIN-SUFFIX,abebooks.com,Proxy
- DOMAIN-SUFFIX,amazon.co.jp,Proxy
- DOMAIN-SUFFIX,apigee.com,Proxy
- DOMAIN-SUFFIX,apk-dl.com,Proxy
- DOMAIN-SUFFIX,apkmirror.com,Proxy
- DOMAIN-SUFFIX,apkmonk.com,Proxy
- DOMAIN-SUFFIX,apkpure.com,Proxy
- DOMAIN-SUFFIX,aptoide.com,Proxy
- DOMAIN-SUFFIX,archive.is,Proxy
- DOMAIN-SUFFIX,archive.org,Proxy
- DOMAIN-SUFFIX,arte.tv,Proxy
- DOMAIN-SUFFIX,ask.com,Proxy
- DOMAIN-SUFFIX,avgle.com,Proxy
- DOMAIN-SUFFIX,badoo.com,Proxy
- DOMAIN-SUFFIX,bandwagonhost.com,Proxy
- DOMAIN-SUFFIX,bbc.com,Proxy
- DOMAIN-SUFFIX,behance.net,Proxy
- DOMAIN-SUFFIX,bibox.com,Proxy
- DOMAIN-SUFFIX,biggo.com.tw,Proxy
- DOMAIN-SUFFIX,binance.com,Proxy
- DOMAIN-SUFFIX,bitcointalk.org,Proxy
- DOMAIN-SUFFIX,bitfinex.com,Proxy
- DOMAIN-SUFFIX,bitmex.com,Proxy
- DOMAIN-SUFFIX,bit-z.com,Proxy
- DOMAIN-SUFFIX,bloglovin.com,Proxy
- DOMAIN-SUFFIX,bloomberg.cn,Proxy
- DOMAIN-SUFFIX,bloomberg.com,Proxy
- DOMAIN-SUFFIX,book.com.tw,Proxy
- DOMAIN-SUFFIX,booklive.jp,Proxy
- DOMAIN-SUFFIX,books.com.tw,Proxy
- DOMAIN-SUFFIX,box.com,Proxy
- DOMAIN-SUFFIX,brookings.edu,Proxy
- DOMAIN-SUFFIX,businessinsider.com,Proxy
- DOMAIN-SUFFIX,bwh1.net,Proxy
- DOMAIN-SUFFIX,castbox.fm,Proxy
- DOMAIN-SUFFIX,cbc.ca,Proxy
- DOMAIN-SUFFIX,cdw.com,Proxy
- DOMAIN-SUFFIX,change.org,Proxy
- DOMAIN-SUFFIX,ck101.com,Proxy
- DOMAIN-SUFFIX,clarionproject.org,Proxy
- DOMAIN-SUFFIX,clyp.it,Proxy
- DOMAIN-SUFFIX,cna.com.tw,Proxy
- DOMAIN-SUFFIX,comparitech.com,Proxy
- DOMAIN-SUFFIX,conoha.jp,Proxy
- DOMAIN-SUFFIX,crucial.com,Proxy
- DOMAIN-SUFFIX,cts.com.tw,Proxy
- DOMAIN-SUFFIX,cw.com.tw,Proxy
- DOMAIN-SUFFIX,cyberctm.com,Proxy
- DOMAIN-SUFFIX,dailymotion.com,Proxy
- DOMAIN-SUFFIX,dailyview.tw,Proxy
- DOMAIN-SUFFIX,daum.net,Proxy
- DOMAIN-SUFFIX,daumcdn.net,Proxy
- DOMAIN-SUFFIX,dcard.tw,Proxy
- DOMAIN-SUFFIX,deepdiscount.com,Proxy
- DOMAIN-SUFFIX,deezer.com,Proxy
- DOMAIN-SUFFIX,depositphotos.com,Proxy
- DOMAIN-SUFFIX,disconnect.me,Proxy
- DOMAIN-SUFFIX,discordapp.com,Proxy
- DOMAIN-SUFFIX,discordapp.net,Proxy
- DOMAIN-SUFFIX,disqus.com,Proxy
- DOMAIN-SUFFIX,dns2go.com,Proxy
- DOMAIN-SUFFIX,dropbox.com,Proxy
- DOMAIN-SUFFIX,dropboxusercontent.com,Proxy
- DOMAIN-SUFFIX,duckduckgo.com,Proxy
- DOMAIN-SUFFIX,dw.com,Proxy
- DOMAIN-SUFFIX,dynu.com,Proxy
- DOMAIN-SUFFIX,earthcam.com,Proxy
- DOMAIN-SUFFIX,ebookservice.tw,Proxy
- DOMAIN-SUFFIX,economist.com,Proxy
- DOMAIN-SUFFIX,edgecastcdn.net,Proxy
- DOMAIN-SUFFIX,edu,Proxy
- DOMAIN-SUFFIX,elpais.com,Proxy
- DOMAIN-SUFFIX,enanyang.my,Proxy
- DOMAIN-SUFFIX,euronews.com,Proxy
- DOMAIN-SUFFIX,feedly.com,Proxy
- DOMAIN-SUFFIX,files.wordpress.com,Proxy
- DOMAIN-SUFFIX,flickr.com,Proxy
- DOMAIN-SUFFIX,flitto.com,Proxy
- DOMAIN-SUFFIX,foreignpolicy.com,Proxy
- DOMAIN-SUFFIX,friday.tw,Proxy
- DOMAIN-SUFFIX,gate.io,Proxy
- DOMAIN-SUFFIX,getlantern.org,Proxy
- DOMAIN-SUFFIX,getsync.com,Proxy
- DOMAIN-SUFFIX,globalvoices.org,Proxy
- DOMAIN-SUFFIX,goo.ne.jp,Proxy
- DOMAIN-SUFFIX,goodreads.com,Proxy
- DOMAIN-SUFFIX,gov.tw,Proxy
- DOMAIN-SUFFIX,gumroad.com,Proxy
- DOMAIN-SUFFIX,hbg.com,Proxy
- DOMAIN-SUFFIX,hightail.com,Proxy
- DOMAIN-SUFFIX,hk01.com,Proxy
- DOMAIN-SUFFIX,hkbf.org,Proxy
- DOMAIN-SUFFIX,hkbookcity.com,Proxy
- DOMAIN-SUFFIX,hkej.com,Proxy
- DOMAIN-SUFFIX,hket.com,Proxy
- DOMAIN-SUFFIX,hkgolden.com,Proxy
- DOMAIN-SUFFIX,hootsuite.com,Proxy
- DOMAIN-SUFFIX,hudson.org,Proxy
- DOMAIN-SUFFIX,huobi.pro,Proxy
- DOMAIN-SUFFIX,initiummall.com,Proxy
- DOMAIN-SUFFIX,ipfs.io,Proxy
- DOMAIN-SUFFIX,issuu.com,Proxy
- DOMAIN-SUFFIX,japantimes.co.jp,Proxy
- DOMAIN-SUFFIX,jiji.com,Proxy
- DOMAIN-SUFFIX,jinx.com,Proxy
- DOMAIN-SUFFIX,jkforum.net,Proxy
- DOMAIN-SUFFIX,joinmastodon.org,Proxy
- DOMAIN-SUFFIX,kakao.com,Proxy
- DOMAIN-SUFFIX,lihkg.com,Proxy
- DOMAIN-SUFFIX,live.com,Proxy
- DOMAIN-SUFFIX,mail.ru,Proxy
- DOMAIN-SUFFIX,matters.news,Proxy
- DOMAIN-SUFFIX,medium.com,Proxy
- DOMAIN-SUFFIX,mega.nz,Proxy
- DOMAIN-SUFFIX,mil,Proxy
- DOMAIN-SUFFIX,mobile01.com,Proxy
- DOMAIN-SUFFIX,naver.com,Proxy
- DOMAIN-SUFFIX,nikkei.com,Proxy
- DOMAIN-SUFFIX,nofile.io,Proxy
- DOMAIN-SUFFIX,now.com,Proxy
- DOMAIN-SUFFIX,nyt.com,Proxy
- DOMAIN-SUFFIX,nytchina.com,Proxy
- DOMAIN-SUFFIX,nytcn.me,Proxy
- DOMAIN-SUFFIX,nytco.com,Proxy
- DOMAIN-SUFFIX,nytimes.com,Proxy
- DOMAIN-SUFFIX,nytimg.com,Proxy
- DOMAIN-SUFFIX,nytlog.com,Proxy
- DOMAIN-SUFFIX,nytstyle.com,Proxy
- DOMAIN-SUFFIX,ok.ru,Proxy
- DOMAIN-SUFFIX,okex.com,Proxy
- DOMAIN-SUFFIX,pcloud.com,Proxy
- DOMAIN-SUFFIX,pinimg.com,Proxy
- DOMAIN-SUFFIX,pixiv.net,Proxy
- DOMAIN-SUFFIX,pornhub.com,Proxy
- DOMAIN-SUFFIX,pureapk.com,Proxy
- DOMAIN-SUFFIX,quora.com,Proxy
- DOMAIN-SUFFIX,quoracdn.net,Proxy
- DOMAIN-SUFFIX,rakuten.co.jp,Proxy
- DOMAIN-SUFFIX,reddit.com,Proxy
- DOMAIN-SUFFIX,redditmedia.com,Proxy
- DOMAIN-SUFFIX,resilio.com,Proxy
- DOMAIN-SUFFIX,reuters.com,Proxy
- DOMAIN-SUFFIX,scmp.com,Proxy
- DOMAIN-SUFFIX,scribd.com,Proxy
- DOMAIN-SUFFIX,seatguru.com,Proxy
- DOMAIN-SUFFIX,shadowsocks.org,Proxy
- DOMAIN-SUFFIX,slideshare.net,Proxy
- DOMAIN-SUFFIX,soundcloud.com,Proxy
- DOMAIN-SUFFIX,startpage.com,Proxy
- DOMAIN-SUFFIX,steamcommunity.com,Proxy
- DOMAIN-SUFFIX,steemit.com,Proxy
- DOMAIN-SUFFIX,t66y.com,Proxy
- DOMAIN-SUFFIX,teco-hk.org,Proxy
- DOMAIN-SUFFIX,teco-mo.org,Proxy
- DOMAIN-SUFFIX,teddysun.com,Proxy
- DOMAIN-SUFFIX,theinitium.com,Proxy
- DOMAIN-SUFFIX,tineye.com,Proxy
- DOMAIN-SUFFIX,torproject.org,Proxy
- DOMAIN-SUFFIX,tumblr.com,Proxy
- DOMAIN-SUFFIX,turbobit.net,Proxy
- DOMAIN-SUFFIX,twitch.tv,Proxy
- DOMAIN-SUFFIX,udn.com,Proxy
- DOMAIN-SUFFIX,unseen.is,Proxy
- DOMAIN-SUFFIX,upmedia.mg,Proxy
- DOMAIN-SUFFIX,uptodown.com,Proxy
- DOMAIN-SUFFIX,ustream.tv,Proxy
- DOMAIN-SUFFIX,uwants.com,Proxy
- DOMAIN-SUFFIX,v2ray.com,Proxy
- DOMAIN-SUFFIX,viber.com,Proxy
- DOMAIN-SUFFIX,videopress.com,Proxy
- DOMAIN-SUFFIX,vimeo.com,Proxy
- DOMAIN-SUFFIX,voxer.com,Proxy
- DOMAIN-SUFFIX,vzw.com,Proxy
- DOMAIN-SUFFIX,w3schools.com,Proxy
- DOMAIN-SUFFIX,wattpad.com,Proxy
- DOMAIN-SUFFIX,whoer.net,Proxy
- DOMAIN-SUFFIX,wikimapia.org,Proxy
- DOMAIN-SUFFIX,wikipedia.org,Proxy
- DOMAIN-SUFFIX,wire.com,Proxy
- DOMAIN-SUFFIX,worldcat.org,Proxy
- DOMAIN-SUFFIX,wsj.com,Proxy
- DOMAIN-SUFFIX,wsj.net,Proxy
- DOMAIN-SUFFIX,xboxlive.com,Proxy
- DOMAIN-SUFFIX,xvideos.com,Proxy
- DOMAIN-SUFFIX,yahoo.com,Proxy
- DOMAIN-SUFFIX,yesasia.com,Proxy
- DOMAIN-SUFFIX,yes-news.com,Proxy
- DOMAIN-SUFFIX,yomiuri.co.jp,Proxy
- DOMAIN-SUFFIX,you-get.org,Proxy
- DOMAIN-SUFFIX,zb.com,Proxy
- DOMAIN-SUFFIX,zello.com,Proxy
- DOMAIN-SUFFIX,zeronet.io,Proxy
- DOMAIN,cdn-images.mailchimp.com,Proxy
- DOMAIN,id.heroku.com,Proxy
- DOMAIN-KEYWORD,github,Proxy
- DOMAIN-KEYWORD,jav,Proxy
- DOMAIN-KEYWORD,pinterest,Proxy
- DOMAIN-KEYWORD,porn,Proxy
- DOMAIN-KEYWORD,wikileaks,Proxy'''

rule2 = '''# (Region-Restricted Access Denied)
- DOMAIN-SUFFIX,apartmentratings.com,Proxy
- DOMAIN-SUFFIX,apartments.com,Proxy
- DOMAIN-SUFFIX,bankmobilevibe.com,Proxy
- DOMAIN-SUFFIX,booktopia.com.au,Proxy
- DOMAIN-SUFFIX,centauro.com.br,Proxy
- DOMAIN-SUFFIX,clearsurance.com,Proxy
- DOMAIN-SUFFIX,costco.com,Proxy
- DOMAIN-SUFFIX,crackle.com,Proxy
- DOMAIN-SUFFIX,depositphotos.cn,Proxy
- DOMAIN-SUFFIX,dish.com,Proxy
- DOMAIN-SUFFIX,dmm.co.jp,Proxy
- DOMAIN-SUFFIX,dmm.com,Proxy
- DOMAIN-SUFFIX,dnvod.tv,Proxy
- DOMAIN-SUFFIX,esurance.com,Proxy
- DOMAIN-SUFFIX,extmatrix.com,Proxy
- DOMAIN-SUFFIX,fastpic.ru,Proxy
- DOMAIN-SUFFIX,flipboard.com,Proxy
- DOMAIN-SUFFIX,fnac.be,Proxy
- DOMAIN-SUFFIX,fnac.com,Proxy
- DOMAIN-SUFFIX,funkyimg.com,Proxy
- DOMAIN-SUFFIX,fxnetworks.com,Proxy
- DOMAIN-SUFFIX,gettyimages.com,Proxy
- DOMAIN-SUFFIX,jcpenney.com,Proxy
- DOMAIN-SUFFIX,kknews.cc,Proxy
- DOMAIN-SUFFIX,nationwide.com,Proxy
- DOMAIN-SUFFIX,nbc.com,Proxy
- DOMAIN-SUFFIX,nordstrom.com,Proxy
- DOMAIN-SUFFIX,nordstromimage.com,Proxy
- DOMAIN-SUFFIX,nordstromrack.com,Proxy
- DOMAIN-SUFFIX,read01.com,Proxy
- DOMAIN-SUFFIX,superpages.com,Proxy
- DOMAIN-SUFFIX,target.com,Proxy
- DOMAIN-SUFFIX,thinkgeek.com,Proxy
- DOMAIN-SUFFIX,tracfone.com,Proxy
- DOMAIN-SUFFIX,uploader.jp,Proxy
- DOMAIN-SUFFIX,vevo.com,Proxy
- DOMAIN-SUFFIX,viu.tv,Proxy
- DOMAIN-SUFFIX,vk.com,Proxy
- DOMAIN-SUFFIX,vsco.co,Proxy
- DOMAIN-SUFFIX,xfinity.com,Proxy
- DOMAIN-SUFFIX,zattoo.com,Proxy
- DOMAIN,abc.com,Proxy
- DOMAIN,abc.go.com,Proxy
- DOMAIN,abc.net.au,Proxy
- DOMAIN,wego.here.com,Proxy
#USER-AGENT,Roam*,Proxy

# (The Most Popular Sites)
# > Apple
# > Apple URL Shortener
- DOMAIN-SUFFIX,appsto.re,Proxy
# > TestFlight
- DOMAIN,beta.itunes.apple.com,Proxy
# > iBooks Store download
- DOMAIN,books.itunes.apple.com,Proxy
# > iTunes Store Moveis Trailers
- DOMAIN,hls.itunes.apple.com,Proxy
# App Store Preview
- DOMAIN,itunes.apple.com,Proxy
# > Spotlight
- DOMAIN,api-glb-sea.smoot.apple.com,Proxy
# > Dictionary
- DOMAIN,lookup-api.apple.com,Proxy
#PROCESS-NAME,LookupViewService,Proxy
# > Google
- DOMAIN-SUFFIX,abc.xyz,Proxy
- DOMAIN-SUFFIX,android.com,Proxy
- DOMAIN-SUFFIX,androidify.com,Proxy
- DOMAIN-SUFFIX,dialogflow.com,Proxy
- DOMAIN-SUFFIX,autodraw.com,Proxy
- DOMAIN-SUFFIX,capitalg.com,Proxy
- DOMAIN-SUFFIX,certificate-transparency.org,Proxy
- DOMAIN-SUFFIX,chrome.com,Proxy
- DOMAIN-SUFFIX,chromeexperiments.com,Proxy
- DOMAIN-SUFFIX,chromestatus.com,Proxy
- DOMAIN-SUFFIX,chromium.org,Proxy
- DOMAIN-SUFFIX,creativelab5.com,Proxy
- DOMAIN-SUFFIX,debug.com,Proxy
- DOMAIN-SUFFIX,deepmind.com,Proxy
- DOMAIN-SUFFIX,firebaseio.com,Proxy
- DOMAIN-SUFFIX,getmdl.io,Proxy
- DOMAIN-SUFFIX,ggpht.com,Proxy
- DOMAIN-SUFFIX,gmail.com,Proxy
- DOMAIN-SUFFIX,gmodules.com,Proxy
- DOMAIN-SUFFIX,godoc.org,Proxy
- DOMAIN-SUFFIX,golang.org,Proxy
- DOMAIN-SUFFIX,gstatic.com,Proxy
- DOMAIN-SUFFIX,gv.com,Proxy
- DOMAIN-SUFFIX,gwtproject.org,Proxy
- DOMAIN-SUFFIX,itasoftware.com,Proxy
- DOMAIN-SUFFIX,madewithcode.com,Proxy
- DOMAIN-SUFFIX,material.io,Proxy
- DOMAIN-SUFFIX,polymer-project.org,Proxy
- DOMAIN-SUFFIX,admin.recaptcha.net,Proxy
- DOMAIN-SUFFIX,recaptcha.net,Proxy
- DOMAIN-SUFFIX,shattered.io,Proxy
- DOMAIN-SUFFIX,synergyse.com,Proxy
- DOMAIN-SUFFIX,tensorflow.org,Proxy
- DOMAIN-SUFFIX,tiltbrush.com,Proxy
- DOMAIN-SUFFIX,waveprotocol.org,Proxy
- DOMAIN-SUFFIX,waymo.com,Proxy
- DOMAIN-SUFFIX,webmproject.org,Proxy
- DOMAIN-SUFFIX,webrtc.org,Proxy
- DOMAIN-SUFFIX,whatbrowser.org,Proxy
- DOMAIN-SUFFIX,widevine.com,Proxy
- DOMAIN-SUFFIX,x.company,Proxy
- DOMAIN-SUFFIX,youtu.be,Proxy
- DOMAIN-SUFFIX,yt.be,Proxy
- DOMAIN-SUFFIX,ytimg.com,Proxy
# > Steam
- DOMAIN,media.steampowered.com,Proxy
- DOMAIN,store.steampowered.com,Proxy
# > Other
- DOMAIN-SUFFIX,0rz.tw,Proxy
- DOMAIN-SUFFIX,4bluestones.biz,Proxy
- DOMAIN-SUFFIX,9bis.net,Proxy
- DOMAIN-SUFFIX,allconnected.co,Proxy
- DOMAIN-SUFFIX,amazonaws.com,Proxy
- DOMAIN-SUFFIX,aol.com,Proxy
- DOMAIN-SUFFIX,bcc.com.tw,Proxy
- DOMAIN-SUFFIX,bit.ly,Proxy
- DOMAIN-SUFFIX,bitshare.com,Proxy
- DOMAIN-SUFFIX,blog.jp,Proxy
- DOMAIN-SUFFIX,blogimg.jp,Proxy
- DOMAIN-SUFFIX,blogtd.org,Proxy
- DOMAIN-SUFFIX,broadcast.co.nz,Proxy
- DOMAIN-SUFFIX,camfrog.com,Proxy
- DOMAIN-SUFFIX,cfos.de,Proxy
- DOMAIN-SUFFIX,citypopulation.de,Proxy
- DOMAIN-SUFFIX,cloudfront.net,Proxy
- DOMAIN-SUFFIX,ctitv.com.tw,Proxy
- DOMAIN-SUFFIX,cuhk.edu.hk,Proxy
- DOMAIN-SUFFIX,cusu.hk,Proxy
- DOMAIN-SUFFIX,discuss.com.hk,Proxy
- DOMAIN-SUFFIX,dropboxapi.com,Proxy
- DOMAIN-SUFFIX,edditstatic.com,Proxy
- DOMAIN-SUFFIX,flickriver.com,Proxy
- DOMAIN-SUFFIX,focustaiwan.tw,Proxy
- DOMAIN-SUFFIX,free.fr,Proxy
- DOMAIN-SUFFIX,ftchinese.com,Proxy
- DOMAIN-SUFFIX,gigacircle.com,Proxy
- DOMAIN-SUFFIX,gov,Proxy
- DOMAIN-SUFFIX,hk-pub.com,Proxy
- DOMAIN-SUFFIX,hosting.co.uk,Proxy
- DOMAIN-SUFFIX,hwcdn.net,Proxy
- DOMAIN-SUFFIX,jtvnw.net,Proxy
- DOMAIN-SUFFIX,linksalpha.com,Proxy
- DOMAIN-SUFFIX,manyvids.com,Proxy
- DOMAIN-SUFFIX,myactimes.com,Proxy
- DOMAIN-SUFFIX,newsblur.com,Proxy
- DOMAIN-SUFFIX,now.im,Proxy
- DOMAIN-SUFFIX,redditlist.com,Proxy
- DOMAIN-SUFFIX,signal.org,Proxy
- DOMAIN-SUFFIX,sparknotes.com,Proxy
- DOMAIN-SUFFIX,streetvoice.com,Proxy
- DOMAIN-SUFFIX,ttvnw.net,Proxy
- DOMAIN-SUFFIX,tv.com,Proxy
- DOMAIN-SUFFIX,twitchcdn.net,Proxy
- DOMAIN-SUFFIX,typepad.com,Proxy
- DOMAIN-SUFFIX,udnbkk.com,Proxy
- DOMAIN-SUFFIX,whispersystems.org,Proxy
- DOMAIN-SUFFIX,wikia.com,Proxy
- DOMAIN-SUFFIX,wn.com,Proxy
- DOMAIN-SUFFIX,wolframalpha.com,Proxy
- DOMAIN-SUFFIX,x-art.com,Proxy
- DOMAIN-SUFFIX,yimg.com,Proxy

- DOMAIN-KEYWORD,dlercloud,Proxy
- DOMAIN-SUFFIX,dler.cloud,Proxy'''

rule3 = '''# Local Area Network
- DOMAIN-KEYWORD,announce,DIRECT
- DOMAIN-KEYWORD,torrent,DIRECT
- DOMAIN-KEYWORD,tracker,DIRECT
- DOMAIN-SUFFIX,smtp,DIRECT
- DOMAIN-SUFFIX,local,DIRECT
- IP-CIDR,192.168.0.0/16,DIRECT
- IP-CIDR,10.0.0.0/8,DIRECT
- IP-CIDR,172.16.0.0/12,DIRECT
- IP-CIDR,127.0.0.0/8,DIRECT
- IP-CIDR,100.64.0.0/10,DIRECT
# GeoIP China
- GEOIP,CN,Domestic

- MATCH,Others'''

@app.route('/')
def work():
    ls = requests.get(url).text.split('\n')
    ret = ''
    for i in range(0, len(ls)):
        if ls[i] == '-' and ls[i + 1] != name_Proxy:
            break
        ret += ls[i]
        ret += '\n'
    ret += rule0
    ret += '\n'
    ret += rule1
    ret += '\n'
    ret += rule2
    ret += '\n'
    ret += rule3
    ret += '\n'
    return ret


if __name__ == '__main__':
    app.run()
