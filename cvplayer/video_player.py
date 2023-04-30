from PyQt6.QtWidgets import QApplication, QMainWindow
from cvplayer.core.media_player.video_player_widget import VideoPlayerWidget
import sys

class VideoPlayer():
    def __init__(self, custom_class) -> None:
        app = QApplication(sys.argv)
        video_player = VideoPlayerWidget(custom_class)
        window = QMainWindow()
        window.setStyleSheet('background-color: rgba(31,29,30,255);')
        window.setCentralWidget(video_player)
        window.show()
        sys.exit(app.exec())


        
    

