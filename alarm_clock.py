import pygame, time, datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        time.sleep(1)
        print(current_time)
        sound_file = "sound.mp3"

        if current_time == alarm_time:
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            time.sleep(10)
            print("WAKE UP SLEEPYHEAD!")
            is_running = False

if __name__ == "__main__":
    alarm_time = input("Set an alarm (in HH:MM:SS): ")
    set_alarm(alarm_time)
