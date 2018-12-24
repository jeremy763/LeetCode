"""
Given a string, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):
    check = []
    index = 0
    for i in range(0, len(s)-1):
        if s[i] != s[i+1]:
            previous = ""
            Next = ""
            if i < len(s)/2:
                for j in range(0, i+1):
                    previous = previous + s[j]
                for k in range(i+1, i+i+2):
                    Next = Next + s[k]

                print("previous:", previous)
                print("next:", Next)
                if previous != Next:
                    pass
                else:
                    check.append(i+1)
        else:
            print("s[i]:", s[i])
            print("s[i+1]:", s[i+1])
            check.append(i)
            index = 0
    if len(check) == 0:
        check.append(len(s))
    print(check)


def online_solution(s):
    start = 0
    end = 1
    length = 0
    for i in range(0, len(s)):
        if s[i] in s[start:i]:
            if length < len(s[start:end]):
                length = len(s[start:end])
            while (s[i] in s[start:i]):
                start = start + 1
        end = i + 1

    if length < len(s[start:end]):
        length = len(s[start:end])

    return length


def main():
    s = "pwwkew"
    lengthOfLongestSubstring(s)
    result = online_solution(s)
    print(result)
main()