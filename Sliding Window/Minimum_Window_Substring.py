from collections import Counter
def minimum_window_substring_naive(s, t):
    t_chars_freq = Counter(t)
    min_substring = None
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            window = s[i:j]
            valid = True
            w_chars_freq = Counter(window)
            for c in t_chars_freq:  # Every character in t is in s[i:j]
                if w_chars_freq[c] < t_chars_freq[c]:
                    valid = False
                    break
            if valid:  # s[i:j] is minimal
                if min_substring is None or len(window) < len(min_substring):
                    min_substring = window

    return min_substring


def minimum_window_substring(s, t):
    if not s or not t:
        return ''
    countT = Counter(t)
    window = {}
    have, need = 0, len(countT)
    l = 0
    res, res_length = [0,0], float('infinity')
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        if c in countT and window[c] == countT[c]:
            have += 1
        while have == need:
             if r - l + 1 < res_length:
                 res = [l, r]
                 res_length = r - l + 1
             window[s[l]] -= 1
             if s[l] in countT and window[s[l]] < countT[s[l]]:
                 have -= 1
             l += 1
    l, r = res
    return s[l:r + 1] if res_length != float('infinity') else ''





