from PySide6.QtWidgets import *
from PySide6.QtCore import *
from qfluentwidgets import BodyLabel


class roll_call(QWidget):
    """班级点名主界面类"""

    settingsChanged = Signal()

    def __init__(self, parent=None):
        """初始化班级点名界面

        Args:
            parent: 父窗口对象
        """
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        """初始化用户界面"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        label = BodyLabel("当前是点名页面")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("font-size: 24px;")

        layout.addWidget(label)
