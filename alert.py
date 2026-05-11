import pygame
import threading

pygame.mixer.init()

def play_alarm(path):
    def run():
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        
    t = threading.Thread(target=run)
    t.daemon=True
    t.start()