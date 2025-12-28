# 1. 클래스(상자)의 이름을 정합니다. 
# 예: class LyricsManager:
class (Lyricsmanager):

    # 2. 클래스가 탄생할 때 '어떤 파일'을 관리할지 미리 알려주는 설정 단계입니다.
    # (이것을 생성자라고 불러요)
    def __init__(self, filename):
        self.filename = filename # 이제 이 상자는 self.filename을 기억합니다.