# from gtts import gTTS
import pdfplumber
from gtts import gTTS
from pathlib import Path
from art import tprint
# from IPython.display import Audio, display
# from playsound import playsound

# import os
# import torch
# import wave
# import contextlib

# ##### text to speech
# device = torch.device('cpu')
# torch.set_num_threads(4)
# local_file = 'model.pt'
# speaker = 'xenia'  # 'aidar', 'baya', 'kseniya', 'xenia', 'eugene', 'random'
# sample_rate = 48000  # 8000, 24000, 48000
#
# if not os.path.isfile(local_file):
#     torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt',
#                                    local_file)
#
# model = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
# model.to(device)


def pdf_to_speech(file_path = '/home/vasiliyeskin/MachineLearningExperiences/Voice_Assistant/basnya-martyshka-i-ochki_11990.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'File exists!'
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', '')

        # audio = model.apply_tts(text='В недрах тундры выдры в г+етрах т+ырят в вёдра ядра к+едров',
        #                         speaker=speaker,
        #                         sample_rate=sample_rate)
        #
        # def write_wave(path, audio, sample_rate):
        #     """Writes a .wav file.
        #     Takes path, PCM audio data, and sample rate.
        #     """
        #     with contextlib.closing(wave.open(path, 'wb')) as wf:
        #         wf.setnchannels(1)
        #         wf.setsampwidth(2)
        #         wf.setframerate(sample_rate)
        #         wf.writeframes(audio)
        #
        # write_wave(path='test_test.wav',
        #            audio=audio.numpy().astype('int16'),
        #            sample_rate=sample_rate)

        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')

        return text
    else:
        return 'File not exists, check the file path!'


def main():
    tprint('PDF>>TO>>SPEECH', font='bulbhead')
    # file_path = input("\nEnter a file's path:")
    # language = input("Choose language, for example 'en' or 'ru':")
    # print(pdf_to_speech(file_path=file_path,language=language))

    print(pdf_to_speech())


if __name__ == '__main__':
    main()
