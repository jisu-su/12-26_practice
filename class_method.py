# 1. 클래스 이름을 정하기
class (Lyricsmanager):

    # 2. __init__으로 초기화하기
    # 클래스가 탄생할 때 '어떤 파일'을 관리할지 미리 알려주는 설정 단계
    def __init__(self, filename):
        self.filename = filename # 이제 이 상자는 self.filename을 기억한다

    # 3. create 부분. 가사를 새로 쓰는 '메서드' 만들기
    def lyrics_write(self, text):
        # 여기에 'w' 모드 코드를 넣어 보기
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(text)

    # 4. read 부분. 가사를 읽어오는 '메서드' 만들기
    def lyrics_read(self):
        # 여기에 'r' 모드 코드를 넣어 보기
        with open(self.filename, "r", encoding="utf-8") as f:
            return f.read()
        
    # 5. delete 부분. 특정 줄을 삭제하는 '메서드' 만들기
    # 몇 번째 줄을 지울지(index)를 재료로 받아야 한다.
    def lyrics_delete(self, index):
        # 1. 파일 읽기 (readlines)
        # 2. del lines[index]
        # 3. 다시 쓰기 (writelines)
        with open(self.filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            del lines[index]
            with open(self.filename, "w", encoding="utf-8") as f2:
                f2.writelines(lines)