import re
arrayBlacklistIP = []
arrayLogsIP = []
arraySelectBlacklistIP = []
i = 0

q = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

with open("4.1/blacklist.txt", "r") as fileBlacklist:
    for lineBlacklist in fileBlacklist:
        blacklistIP = re.search(q, lineBlacklist).group()
        arrayBlacklistIP.append(blacklistIP)

with open("4.1/log.txt", "r") as fileLogs:
    for lineLog in fileLogs:
        LogIP = re.search(q, lineLog).group()
        if LogIP not in arrayLogsIP:
            arrayLogsIP.append(LogIP)
        
for blacklistIP in arrayBlacklistIP:
    i = 0
    while i < len(arrayLogsIP):
        if blacklistIP == arrayLogsIP[i]:
            if blacklistIP not in arraySelectBlacklistIP:
                arraySelectBlacklistIP.append(blacklistIP)
        i += 1
        
for IP in arraySelectBlacklistIP:
    print(IP)