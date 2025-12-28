# 1. 클래스 이름을 정하기
class Lyricsmanager:

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
        # 안정장치 만들어 보기
        # 안전장치: index가 리스트의 범위 안에 있는지 확인한다.
        if 0 <= index < len(lines):
            del lines[index]
            with open(self.filename, "w", encoding="utf-8") as f:
                f.writelines(lines)
            print(f"{index}번 줄을 성공적으로 삭제했습니다.")
        else:
            print(f"에러: {index}번 줄은 존재하지 않습니다. (현재 총 {len(lines)}줄)")

# --- 여기서부터는 상자를 실제로 사용하는 곳 ---

# 6. 위에서 만든 클래스로 '진짜 물건(객체)'을 하나 만들기
manager = Lyricsmanager("Lyrics.txt")

# 7. 이제 점(.)을 찍어서 메서드를 실행해보기
manager.write_new("반짝반짝 작은 별")