import pyaudio

def list_mics():
    p = pyaudio.PyAudio()
    print("\n" + "="*40)
    print(" AVAILABLE MICROPHONES")
    print("="*40)
    
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    
    found = False
    for i in range(0, numdevices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        if device_info.get('maxInputChannels') > 0:
            print(f"Index {i}: {device_info.get('name')}")
            found = True
            
    if not found:
        print("No input devices found.")
    
    print("="*40)
    print("To use a specific mic, set MIC_INDEX in voice_control.py")
    print("="*40 + "\n")
    p.terminate()

if __name__ == "__main__":
    list_mics()
