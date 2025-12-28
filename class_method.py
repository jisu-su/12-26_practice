# 1. 클래스 이름을 정하기
class (Lyricsmanager):

    # 2. __init__으로 초기화하기
    # 클래스가 탄생할 때 '어떤 파일'을 관리할지 미리 알려주는 설정 단계
    def __init__(self, filename):
        self.filename = filename # 이제 이 상자는 self.filename을 기억한다

    # 3. create. 가사를 새로 쓰는 '메서드' 만들기
    def lyrics_write(self, text):
        # 여기에 'w' 모드 코드를 넣어 보기
        pass with open(self.filename, "w", encoding="utf-8") as f:
            f.write("반짝반짝 작은 별")
            f.write("\n아름답게 비추네")