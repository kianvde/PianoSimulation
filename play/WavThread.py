import threading
import pyaudio
import wave



class WavThread (threading.Thread):

    def __init__(self, wav_file):
        super(WavThread, self).__init__()
        self._stop = threading.Event()
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
            if self.stopped(): break;

    def exit(self):
        # close stream
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()