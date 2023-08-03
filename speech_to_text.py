# STT (Speech To Text)
import speech_recognition as sr

# 마이크로부터 음성 듣기
r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고 있어요') # 확인용(시간 gap)
    audio = r.listen(source) # 마이크로부터 음성 듣기

# 파일로부터 음성 불러오기(wav, aiff, flac 기능, mp3는 불가)
#r=sr.Recognizer()
#with sr.AudioFile('sample.wav') as source:
#    audio = r.record(source)

try:
    # 구글 API로 인식(하루 50회 제한)
    # 영어 문장
    # text = r.recognize_google(audio, language = 'en-US')
    # print(text)

    # 한국어 문장
    text = r.recognize_google(audio, langyage = 'ko')
    print(text)

except sr.UnknownValueError:
    print('인식 실패') # 음성 인식 실패한 경우

except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) # API key 오류& 네트워크 단절 
