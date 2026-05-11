import pygame
import threading

pygame.mixer.init()

def play_alarm(path):
    if not pygame.mixer.music.get_busy():
        def run():
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        
        t = threading.Thread(target=run)
        t.daemon=True
        t.start()
        
def stop_alarm():
    pygame.mixer.music.stop()