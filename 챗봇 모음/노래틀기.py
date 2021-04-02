re= '아이유 Celebrity 노래 틀어줘'
send_music=re.replace('틀어줘','')
if '노래' in send_music:
    send_music=send_music.replace('노래','')
print(send_music)