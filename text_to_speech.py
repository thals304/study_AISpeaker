# TTS (Text To Speech)
from gtts import gTTS
from playsound import playsound
'''1. 어떤 글자를 음성으로 바꿀지 text 정의 
   2. gTTS를 이용해 text를 음성으로 바꿔주고 
   3.mp3 파일 형태로 저장'''
# 영어 문장(en)
#text = 'Can I help you?' # text 정의
#file_name = 'sample.mp3' # mp3 파일 이름 정의
#tts_en = gTTS(text=text, lang='en') # 영어를 인식해서 text를 음성으로 바꿔주는 결과 받기
#tts_en.save(file_name) # save 메소드로 경로 저장

# 한국어 문장(ko)
#text = "오늘 날씨가 좋네요"
#file_name = 'sample.mp3'
#tts_ko = gTTS(text=text,lang='ko')
#tts_ko.save(file_name)
#playsound(file_name) # playsound 사용해서 바로 .mp3 파일 재생

# 긴 문장(파일에서 불러와서 처리)
'''text 파일 만들어서 음성 변환할 내용 집어 넣고
그대로 읽어와서 playsound를 통해 재생되도록 or mp3로 저장'''
with open('sample.txt','r', encoding='utf8') as f: # r:불러오기 한글: utf8 
    text = f.read() #파일에 있는 모든 내용을 불러와 저장
file_name = 'sample.mp3'    
tts_ko = gTTS(text=text,lang='ko')
tts_ko.save(file_name)
playsound(file_name)



