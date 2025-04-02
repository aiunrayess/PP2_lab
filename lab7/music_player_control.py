import pygame
import keyboard
from pygame import mixer

# Initialize pygame mixer
pygame.mixer.init()

# List of music tracks (update with your own files)
tracks = [
    "track1.mp3",
    "track2.mp3",
    "track3.mp3"
]
current_track = 0

def play_music():
    try:
        pygame.mixer.music.load(tracks[current_track])
        pygame.mixer.music.play()
        print(f"Playing: {tracks[current_track]}")
    except Exception as e:
        print(f"Error loading track: {e}")

def stop_music():
    pygame.mixer.music.stop()
    print("Playback stopped")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    print(f"Switched to next track: {tracks[current_track]}")
    if pygame.mixer.music.get_busy():
        play_music()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    print(f"Switched to previous track: {tracks[current_track]}")
    if pygame.mixer.music.get_busy():
        play_music()

# Set up keyboard bindings (customize these as needed)
keyboard.add_hotkey('p', play_music)       # Play
keyboard.add_hotkey('s', stop_music)       # Stop
keyboard.add_hotkey('n', next_track)       # Next track
keyboard.add_hotkey('b', previous_track)   # Previous track

print("Music player is running. Press keys to control playback:")
print("p - Play")
print("s - Stop")
print("n - Next track")
print("b - Previous track")
print("Press Ctrl+C to exit")

# Keep the program running
try:
    keyboard.wait('ctrl+c')  # Wait for Ctrl+C to exit
except KeyboardInterrupt:
    print("\nExiting music player")
    pygame.mixer.quit()