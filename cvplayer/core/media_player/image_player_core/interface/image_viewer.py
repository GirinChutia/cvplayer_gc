from PyQt6 import QtCore, QtGui, QtWidgets
import cvplayer.core.utils.widgets_utils as widgets_utils
import cvplayer.core.utils.video_utils as video_utils


class ImageViewer(QtWidgets.QLabel):
    def __init__(self, layout=None, CSS='cvplayer/stylesheets/image_viewer.css'):
        super().__init__()        
        #self.setScaledContents(True)  
        widgets_utils.start_widget_basics(self, layout, CSS)
        self.cv2_image = None    
    def show_cv2_image(self, cv2_image):
        QPixmap = video_utils.cv2_image_to_QPixmap(cv2_image)
        print(QPixmap.width(), QPixmap.height())
        w= self.width()
        h= self.height()
        scaled_pixmap = QPixmap.scaled(w,h, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.setPixmap(scaled_pixmap)


# AspectRatioPixmapLabel::AspectRatioPixmapLabel(QWidget *parent) :
#     QLabel(parent)
# {
#     this->setMinimumSize(1,1);
#     setScaledContents(false);
# }

# void AspectRatioPixmapLabel::setPixmap ( const QPixmap & p)
# {
#     pix = p;
#     QLabel::setPixmap(scaledPixmap());
# }

# int AspectRatioPixmapLabel::heightForWidth( int width ) const
# {
#     return pix.isNull() ? this->height() : ((qreal)pix.height()*width)/pix.width();
# }

# QSize AspectRatioPixmapLabel::sizeHint() const
# {
#     int w = this->width();
#     return QSize( w, heightForWidth(w) );
# }

# QPixmap AspectRatioPixmapLabel::scaledPixmap() const
# {
#     return pix.scaled(this->size(), Qt::KeepAspectRatio, Qt::SmoothTransformation);
# }

# void AspectRatioPixmapLabel::resizeEvent(QResizeEvent * e)
# {
#     if(!pix.isNull())
#         QLabel::setPixmap(scaledPixmap());
# }

# class ImageViewer(QtWidgets.QGraphicsView):
#     photoClicked = QtCore.pyqtSignal(QtCore.QPoint)
#     change_image_on_viewer = QtCore.pyqtSignal()
    
#     def __init__(self, layout=None, CSS=None):
#         super(ImageViewer, self).__init__()
#         widgets_utils.start_widget_basics(self, layout, CSS)
#         self.cv2_image = None
        
#         self._zoom = 0
#         self._empty = True
#         self._scene = QtWidgets.QGraphicsScene(self)
#         self._photo = QtWidgets.QGraphicsPixmapItem()
#         self._scene.addItem(self._photo)
#         self.setScene(self._scene)
#         self.setTransformationAnchor(QtWidgets.QGraphicsView.ViewportAnchor.AnchorUnderMouse)
#         self.setResizeAnchor(QtWidgets.QGraphicsView.ViewportAnchor.AnchorUnderMouse)
#         self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(30, 30, 30)))
#         self.setFrameShape(QtWidgets.QFrame.Shape.NoFrame  )
#         self.change_image_on_viewer.connect(self.setPhoto)

#     def show_cv2_image(self, cv2_image):
#         self.QPixmap = video_utils.cv2_image_to_QPixmap(cv2_image)
#         self.change_image_on_viewer.emit()

#     def hasPhoto(self):
#         return not self._empty

#     def fitInView(self, scale=True):
#         rect = QtCore.QRectF(self._photo.pixmap().rect())
#         self.setSceneRect(rect)
#         unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
#         self.scale(1 / unity.width(), 1 / unity.height())
#         viewrect = self.viewport().rect()
#         scenerect = self.transform().mapRect(rect)
#         factor = min(viewrect.width() / scenerect.width(),
#                         viewrect.height() / scenerect.height())
#         self.scale(factor, factor)
#         self._zoom = 0

#     def setPhoto(self):
#         self._zoom = 0
#         self._empty = False
#         self.setDragMode(QtWidgets.QGraphicsView.DragMode.ScrollHandDrag)
#         self._photo.setPixmap(self.QPixmap)
#         self.fitInView()

#     def wheelEvent(self, event):
#         if self.hasPhoto():
#             if event.angleDelta().y() > 0:
#                 factor = 1.25
#                 self._zoom += 1
#             else:
#                 factor = 0.8
#                 self._zoom -= 1
#             if self._zoom > 0:
#                 self.scale(factor, factor)
#             elif self._zoom == 0:
#                 self.fitInView()
#             else:
#                 self._zoom = 0

#     def toggleDragMode(self):
#         if self.dragMode() == QtWidgets.QGraphicsView.DragMode.ScrollHandDrag:
#             self.setDragMode(QtWidgets.QGraphicsView.DragMode.NoDrag)
#         elif not self._photo.pixmap().isNull():
#             self.setDragMode(QtWidgets.QGraphicsView.DragMode.ScrollHandDrag)

#     def mousePressEvent(self, event):
#         if self._photo.isUnderMouse():
#             self.photoClicked.emit(self.mapToScene(event.pos()).toPoint())
#         super(ImageViewer, self).mousePressEvent(event)


