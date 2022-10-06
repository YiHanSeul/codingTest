def solution(n, words):
    answer = []
    speak =[]
    
    speak.append(words[0])
    for i in range(1,len(words)):
        if words[i] not in speak and words[i-1][-1]==words[i][0] and len(words[i])>1:
            speak.append(words[i])
        else :
            return [(i%n)+1,int(i/n)+1]
    if len(speak)==len(words):
        return [0,0]
    return answer

n=3
words =	["tank", "kick", "know", "wheet", "tank", "dream", "mother", "robot", "tt"]
#words=["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
#words=	["hello", "one", "even", "never", "now", "world", "draw"]
#solution(n,words)
solution(n, words)