
import time
import webbrowser


total_break = 2
break_count = 0
print("program started on"+time.ctime())
while (break_count< total_break):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=euCqAq6BRa4&list=RDMMeuCqAq6BRa4")
    break_count=break_count+1
