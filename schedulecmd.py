import sched, time, datetime, threading, sys
import subprocess

def processing(a):
    subprocess.call( ["python3", "sch.py"] )
    
def schedule():
    s = sched.scheduler(time.time, time.sleep)
    set_time = datetime.datetime.strptime('2018/08/22,06:57', '%Y/%m/%d,%H:%M')  # イベントの開始日時
    add_date = datetime.timedelta(days=1)  # タイムスケジュールの間隔
    while True:
        print(datetime.datetime.now(), 'start')
        s.enterabs(int(time.mktime(set_time.timetuple())), 1, processing, argument=('event1',))
        s.enterabs(int(time.mktime(set_time.timetuple())), 2, processing, argument=('event2',))
        s.enterabs(int(time.mktime(set_time.timetuple())), 3, processing, argument=('event3',))
        s.run()
        set_time += add_date  # 基準となる日付に1日追加
        print(datetime.datetime.now(), 'end')
        
def control():
    thread_obj = threading.Thread(target=schedule, daemon=True)  # daemon=Trueでデーモンスレッドになる
    thread_obj.start()
    while True:
        stop = input()
        if stop == 'stop':
            print(datetime.datetime.now(), 'stop of time_schedule')
            sys.exit()
    
if __name__ == '__main__':
    control()