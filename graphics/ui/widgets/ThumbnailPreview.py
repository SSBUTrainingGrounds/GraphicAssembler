from typing import Callable

from PIL.Image import Image
from PyQt6.QtCore import QObject, QRunnable, Qt, QThreadPool, pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel

from graphics.app.generate import generate_thumbnail
from graphics.utils.types import ThumbnailData


class ImagePreview(QLabel):
    def __init__(self, data: ThumbnailData) -> None:
        super().__init__()
        self.data = data
        self.threadpool = QThreadPool()
        self.setPixmap(
            QPixmap(generate_thumbnail(self.data).toqpixmap()).scaledToHeight(  # type: ignore
                300, mode=Qt.TransformationMode.SmoothTransformation
            )
        )

    def set_pixmap(self, image: Image) -> None:
        self.setPixmap(
            QPixmap(image.toqpixmap()).scaledToHeight(  # type: ignore
                300, mode=Qt.TransformationMode.SmoothTransformation
            )
        )

    def update(self) -> None:
        worker = Worker(generate_thumbnail, self.data)
        worker.signals.result.connect(self.set_pixmap)
        self.threadpool.start(worker)


class Worker(QRunnable):
    def __init__(
        self,
        fn: Callable[[ThumbnailData], Image],
        *args: ThumbnailData,
        **kwargs: ThumbnailData
    ) -> None:
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    def run(self) -> None:
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            self.signals.error.emit((type(e), e, e.__traceback__))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
