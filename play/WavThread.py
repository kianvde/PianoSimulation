import threading
import pyaudio
import wave

# threading class for reading and playing a .wav file
class WavThread (threading.Thread):

    def __init__(self, wav_file):
        super(WavThread, self).__init__()
        self._stop = threading.Event()
        self._play = threading.Event()
        self._terminate = threading.Event()
        self.can_start = True

        self.wav_file = wav_file
        self.chunk = 1024
        self.p = pyaudio.PyAudio()
        self.data = ''

        self.wf = wave.open(self.wav_file, "rb")
        self.stream = self.p.open(format=self.p.get_format_from_width(self.wf.getsampwidth()),
                          channels=self.wf.getnchannels(),
                          rate=self.wf.getframerate(),
                          output=True)

    def run(self):
        while not self.terminated():
            if self.playing():
                self.can_start = False
                self.wf = wave.open(self.wav_file, "rb")
                self.play_note()
                self._play.clear()
                self._stop.set()
            self.can_start = True
        self.exit()

    def play_note(self):

        # read and play
        self.data = self.wf.readframes(self.chunk)
        while self.data != '':
            self.stream.write(self.data)
            self.data = self.wf.readframes(self.chunk)
            if self.stopped():
                self.data = ''

    def exit(self):
        # close stream
        self.p.terminate()

    def play(self):
        self.stop()
        self._stop.clear()
        self._play.set()

    def stop(self):
        self._play.clear()
        self._stop.set()
        while not self.can_start:
            pass

    def terminate(self):
        self.stop()
        self._terminate.set()

    def playing(self):
        return self._play.isSet()

    def stopped(self):
        return self._stop.isSet()

    def terminated(self):
        return self._terminate.isSet()