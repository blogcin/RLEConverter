class RLEConverter(object):

    def __init__(self, s):
        self.s = s

    def convert(self):
        if len(self.s) < 2:
            print("올바르지 않은 문자열입니다.")
            return ""
        else:
            count = 1
            previous_word = ''
            result = ""
            for character in self.s:
                # 현재 가르키는 단어가 이전의 단어와 같지 않을 때
                if character != previous_word:
                    # 이전의 단어가 존재 할때
                    if previous_word:
                        # 이전단어가 존재하지만 이전의 단어와 현재 가르키는 단어가 같지 않아 카운트가 1일때
                        if count == 1:
                            # 결과에 이전 단어를 추가
                            result += previous_word

                        # count가 1이 아닐 때, 즉 이전 단어와 현재 단어가 다르지만 이전에 같았으므로 카운트 추가
                        else:
                            # 결과에 형식을 맞춰 추가
                            result += ("*" + str(count) + previous_word)
                    count = 1
                    previous_word = character
                else:
                    count += 1
            else:
                # 카운트가 1일때
                if count == 1:
                    # 결과에 단어 추가
                    result += character
                else:
                    # 결과에 형식을 맞춰 추가
                    result += ("*" + str(count) + character)
            return result

if __name__ == "__main__":
    s = input()
    rleConverter = RLEConverter(s)
    print(rleConverter.convert())

