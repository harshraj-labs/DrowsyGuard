import pygame
import threading

_initialized = False


def _ensure_init():
    global _initialized
    if not _initialized:
        pygame.mixer.init()
        _initialized = True


def play_alarm(path):
    _ensure_init()
    if not pygame.mixer.music.get_busy():
        def run():
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        t = threading.Thread(target=run)
        t.daemon = True
        t.start()


def stop_alarm():
    _ensure_init()
    pygame.mixer.music.stop()