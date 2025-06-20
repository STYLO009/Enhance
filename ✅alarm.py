import datetime
import time
import threading
from playsound import playsound
import os

TONE_OPTIONS = {
    'default': 'default_alarm.mp3',
    'beep': 'beep_alarm.mp3',
    'ring': 'ring_alarm.mp3',
    'tumhe': r'C:\Users\LOQ\Downloads\128-Tumhe Kitna Pyaar Karte - Bawaal 128 Kbps.mp3'
}

def play_alarm(tone):
    sound_file = TONE_OPTIONS.get(tone, TONE_OPTIONS['default'])
    if not os.path.exists(sound_file):
        print(f"❌ Sound file not found: {sound_file}")
        return
    print("⏰ Wake up! Alarm is ringing...")
    playsound(sound_file)

def set_alarm(alarm_time, tone, snooze_minutes):
    try:
        while True:
            now = datetime.datetime.now().strftime("%H:%M")
            if now == alarm_time:
                play_alarm(tone)
                while True:
                    snooze = input(f"Snooze for {snooze_minutes} minutes? (y/n): ").lower()
                    if snooze == 'y':
                        print("😴 Snoozing...")
                        time.sleep(snooze_minutes * 60)
                        play_alarm(tone)
                    elif snooze == 'n':
                        print("✅ Alarm stopped.")
                        return
                    else:
                        print("Please enter 'y' or 'n'.")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nAlarm stopped by user.")

def validate_time(input_time):
    try:
        datetime.datetime.strptime(input_time, "%H:%M")
        return True
    except ValueError:
        return False

def main():
    while True:
        alarm_time = input("Enter alarm time (HH:MM in 24hr format): ")
        if validate_time(alarm_time):
            break
        print("Invalid time format. Please use HH:MM (24hr).")
    
    tone = input("Choose a tone (default, beep, ring, tumhe): ").lower()
    if tone not in TONE_OPTIONS:
        print("Invalid tone selected. Using default.")
        tone = 'default'

    while True:
        try:
            snooze_minutes = int(input("Enter snooze duration in minutes: "))
            if snooze_minutes > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")
    
    alarm_thread = threading.Thread(target=set_alarm, args=(alarm_time, tone, snooze_minutes))
    alarm_thread.start()

if __name__ == "__main__":
    main()
