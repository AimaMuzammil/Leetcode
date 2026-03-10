class Solution:
    def isFreqSame(self, freq1,freq2):
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        freq = [0] * 26

        for i in s1:
            freq[ord(i) - ord('a')] += 1

        windowSize = len(s1)
        for i in range(len(s2) - windowSize + 1):  
            windowIdx = 0
            idx = i
            windfreq = [0] * 26
            while windowIdx < windowSize and idx < len(s2):
                windfreq[ord(s2[idx]) - ord('a')] += 1
                windowIdx += 1
                idx += 1
            if self.isFreqSame(freq, windfreq):
                return True
        return False