from PyQt6.QtWidgets import QPushButton, QFileDialog
from cvplayer.core.utils.widgets_utils import start_widget_basics


class AddVideosButton(QPushButton):
    def __init__(self, videos_list, layout=None, CSS='cvplayer/stylesheets/add_videos_button.css'):
        super().__init__()
        start_widget_basics(self, layout, CSS)
        self.setText('Add Videos')
        self.videos_list = videos_list
        self.clicked.connect(self.get_videos)

    def get_videos(self):
        mp4_files = QFileDialog.getOpenFileNames(self, "Select videos", "", "Video Files (*.mp4 *.MP4 *.avi *.mov)")[0]
        if len(mp4_files) > 0:
            self.videos_list.add_videos(mp4_files)



        


        