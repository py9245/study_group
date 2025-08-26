import sys
sys.stdin = open("input (18).txt","r")

T = int(input())
for tc in range(1, T + 1):
    word = input()
    result = 0
    for i in range(len(word)):
        if word[i] == word[len(word)-1-i]:
            result = 1
        else :
            result = 0
    print(f"#{tc} {result}")