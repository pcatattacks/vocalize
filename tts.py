from gtts import gTTS
from pydub import AudioSegment

FILEPATH = 'tts_dump.mp3'

def tts(text):
    """
        returns list of AudioSegments corresponding to each word in text
    """
    tokens = text.split(' ')
    audio_chunks = [tts_word(token) for token in tokens]
    return audio_chunks

def tts_word(word):
    sound_obj = gTTS(word)
    sound_obj.save(FILEPATH)
    y = AudioSegment.from_mp3(FILEPATH)
    return y