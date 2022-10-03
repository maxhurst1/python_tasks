statuses = { 
"Alice": "online", 
"Bob": "offline", 
"Eve": "online", 
}

def online_count(statuses):
    online = 0
    for status in statuses.values():
        if status == "online":
            online += 1
    return online
print(online_count(statuses))
