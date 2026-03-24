# with open('4/4.1/log.txt', 'r', encoding='utf-8') as file:
#     lines=file.readlines()

# 4.1.7.1
# user_actions = {}

# for line in lines:
#     parts = line.split()
#     user = None
#     for part in parts:
#         if part.startswith('USER:'):
#             user = part.replace('USER:', '')
#             break
    
#     if user:
#         user_actions[user] = user_actions.get(user, 0) + 1

# if user_actions:
#     max_actions = 0
#     most_active_user = None
    
#     for user, count in user_actions.items():
#         if count > max_actions:
#             max_actions = count
#             most_active_user = user
    
#     print(f"\n🎯 Самый активный пользователь: '{most_active_user}'")
#     print(f"   Количество действий: {max_actions}")

# 4.1.7.2
# errors_dict = {}

# for line in lines:
#     if 'STATUS:FAILED' in line or 'ERROR' in line:
#         parts = line.split()
#         user = None
#         for part in parts:
#             if part.startswith('USER:'):
#                 user = part.replace('USER:', '')
#                 break
        
#         if user:
#             errors_dict[user] = errors_dict.get(user, 0) + 1

# errors_list = []
# for user, count in errors_dict.items():
#     errors_list.append([user, count])

# errors_list = sorted(errors_list, key=lambda x: x[1], reverse=True)

# print(f"\n🎯 Пользователь с наибольшим числом ошибок: '{errors_list[0][0]}'")
# print(f"   Количество ошибок: {errors_list[0][1]}")
 
# 4.1.8
# hour_activity={}

# for line in lines:
#     time_str=line[12:20]
#     hour=int(time_str.split(':')[0])
#     hour_activity[hour]=hour_activity.get(hour,0)+1
# activity_list=[]
# for hour,count in hour_activity.items():
#     activity_list.append([hour,count])

# activity_list = sorted(activity_list, key=lambda x: x[0])

# print('Активность по часам:')
# for hour, count in activity_list:
#     bar='█'*count
#     print(f"{hour:02d}" + bar)

# 4.1.6
# download_by_day={}

# for line in lines:
#     if 'ACTION:DOWNLOAD' in line:
#         date=line[1:11]
#         download_by_day[date]=download_by_day.get(date,0)+1

# dates=[]
# for date in download_by_day.keys():
#     dates.append(date)
# dates.sort()

# previous_count=None
# previous_date=None
# for date in dates:
#     current_count=download_by_day[date]
#     if previous_count is not None:
#         if previous_count>0 and current_count>previous_count*2:
#             print('В ' + date + ' было более чем в 2 раза скачиваний чем в предыдущую дату (' + str(previous_count) + '), а именно ' + str(current_count))
#     previous_count=current_count
#     previous_date=date

# 4.1.5
# target='alex_ivanov'
# action_count={}
# target_str='USER:'+target

# for line in lines:
#     if target_str in line:
#         parts = line.split()
#         action=None
#         for part in parts:
#             if part.startswith('ACTION:'):
#                 action = part.replace('ACTION:','')
#                 break 
#         if not action:
#             continue
#         else:
#             action_count[action]=action_count.get(action,0)+1
# max_count=0
# action_target=None
# for action,count in action_count.items():
#     if count>max_count:
#         max_count=count
#         action_target=action

# print('Пользователь ' + target + ' чаще всего выполнял '+ action_target + '. Всего '+ str(max_count)+ ' раз')

# 4.1.4
# with open('4/4.1/blacklist.txt', 'r', encoding='utf-8') as blacklist:
#     blackips=blacklist.readlines()

# blackip=[]
# for line in blackips:
#     line=line.strip()
#     if not line:
#         continue
#     blackip.append(line)

# for line in lines:
#     parts = line.split()
#     ip=None
#     for part in parts:
#         if part.startswith('IP:'):
#             ip = part.replace('IP:','')
#             break 
#         if not ip:
#             continue 
#     if ip in blackip:
#         print("Попытка действий с IP из черного списка:")
#         print(line)

# 4.1.3
# login_by_ip={}
# for line in lines:
#     if 'ACTION:LOGIN' in line and 'STATUS:SUCCESS' in line:
#         parts = line.split()
#         ip=None
#         for part in parts:
#             if part.startswith('IP:'):
#                 ip = part.replace('IP:','')
#                 break 
#             if not ip:
#                 continue 
#         time_str=line[12:17]
        
#         if ip not in login_by_ip:
#             login_by_ip[ip]=[]
#         login_by_ip[ip].append(time_str)
# for ip, times in login_by_ip.items():
#     times.sort()

#     minute_count = {}

#     for time_str in times:
#         minute_count[time_str]=minute_count.get(time_str,0)+1
    
#     for minute, count in minute_count.items():
#         if count>=20:
#             print('C IP: ' + ip + ' было ' + str(count) + ' входов в минуту')

# 4.1.2
# failed_count={}
# found_ips=set()

# for line in lines:
#     line=line.strip()
#     if not line:
#         continue
    
#     4.1.2
#     parts = line.split()
#     ip=None
#     for part in parts:
#             if part.startswith('IP:'):
#                 ip = part.replace('IP:','')
#                 break 
#     if not ip:
#          continue
    
#     if 'ACTION:LOGIN' in line:
#          if 'STATUS:FAILED' in line:
#               failed_count[ip]=failed_count.get(ip, 0)+1
#               if failed_count[ip]>=10 and ip not in found_ips:
#                    print ('C IP ' + ip + ' было ' + str(failed_count[ip]) + ' неудачных входов подряд')
#                    found_ips.add(ip)
         
#          if 'STATUS:SUCCESS' in line:
#               if ip in failed_count:
#                    failed_count[ip]=0




    # 4.1.1 
    # if 'ACTION:LOGIN' in line and 'STATUS:SUCCESS' in line:
    #     time_str= line[12:20]
    #     hour=int(time_str.split(':')[0])

    #     parts=line.split()
    #     user=None
    #     for part in parts:
    #         if part.startswith('USER:'):
    #             user = part.replace('USER:','')
    #             break

    #     if hour<8 or hour>16:
    #         print('Пользователь '+user+' вошел в неположенное время: ' + time_str)