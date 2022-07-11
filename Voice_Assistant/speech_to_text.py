import vosk
import sys
import sounddevice as sd
import queue

model = vosk.Model("model")
samplerate = 16000 # частота дискретизации: рекомендация от 8kHz до 16kHz
device = 6 # id устройства записи (микрофона)

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

with sd.RawInputStream(samplerate=samplerate,
                       blocksize=8000,
                       device=device,
                       dtype='int16',
                       channels=1,
                       callback=callback):
    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            print(rec.Reset())
        else:
            print(rec.PartialResult())
