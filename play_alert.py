import multiprocessing

from playsound import playsound


class play_alert:
    p: multiprocessing.Process = None

    def start_alert(self):
        if self.p is not None and self.p.is_alive():
            return

        self.p = multiprocessing.Process(
            target=playsound, args=("bomb_siren.mp3",))
        self.p.start()

    def stop_alert(self):
        if self.p is not None and self.p.is_alive():
            self.p.terminate()
