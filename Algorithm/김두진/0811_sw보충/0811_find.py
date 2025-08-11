# 아스키 코드
# 대문자 A : 65 , 소문자  a: 97
# 대문자 + 32 : 소문자
char = 'C'
char = chr(ord(char) + 32)
print(char)

# 2. find 메서드
# (1) str.find() : 찾으면 발견된 인덱스 반환, 못찾으면 -1 반환
# (2) str.find('a',n)
# n번 인덱스부터 시작해서(start) 문자 'a'를 찾아라
# ex) [123]456[87] --> 87이라는 숫자를 Parsing하고싶다.

text = 'banana'
print(text.find('a')) # 1
print(text.find('a', 2)) # 3

# 3. 회문 : 거꾸로 읽어도 같은 문자열
# 거꾸로 뒤집는 방법 [::-1]