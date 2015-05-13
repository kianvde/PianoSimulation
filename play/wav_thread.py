import threading
import pyaudio
import wave

class WavThread (threading.Thread):

    def __init__(self, wav_file):
        threading.Thread.__init__(self)
        self.handled = False
        self.chunk = 1024
        self.wf = wave.open(wav_file,"rb")
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                        channels=self.wf.getnchannels(),
                        rate=self.wf.getframerate(),
                        output=True)

    def run(self):
        self.play_note()

    def play_note(self):

        # read and play
        data = self.wf.readframes(self.chunk)
        while data != '':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

        # close stream
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()