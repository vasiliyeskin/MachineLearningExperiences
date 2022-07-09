# from gtts import gTTS
import pdfplumber
from gtts import gTTS
from pathlib import Path
from art import tprint


def pdf_to_speech(file_path = '/home/vasiliyeskin/MachineLearningExperiences/Voice_Assistant/basnya-martyshka-i-ochki_11990.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'File exists!'
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages)
        text = text.replace('\n', ' ')

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
