from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QTableWidget


class Table(QTableWidget):
    def __init__(
            self,
            selection_color,
            text_color,
            hover_color,
            background_color,
            parent=None
    ):
        super().__init__(parent)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.verticalHeader().setVisible(False)
        self.setAlternatingRowColors(True)
        self.setStyleSheet("""
            QTableWidget {
                border: 2px solid $HOVER;
                border-radius: 5px;
                background: $BG1;
                color: $TEXT_COLOR;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QTableWidget::item:selected {
                background: $SELECTION;
                color: $TEXT_COLOR;
            }
            QTableWidget::item:hover {
                background: $HOVER;
                color: $TEXT_COLOR;
            }
            
            QHeaderView::section {
                background: $BG1;
                color: $TEXT_COLOR;
                padding: 5px;
                border-bottom: 2px solid $HOVER;
            }
            QHeaderView::section:hover {
                background: $HOVER;
            }
            
            QScrollBar:vertical {
                border: none;
                background: $BG1;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: $HOVER;
                border-radius: 2px;
                min-height: 0px;
            }
            QScrollBar::add-line:vertical {
                border: none;
                background: none;
            }
            QScrollBar::sub-line:vertical {
                border: none;
                background: none;
            }
            
        """.replace(
            "$SELECTION", selection_color
        ).replace(
            "$TEXT_COLOR", text_color
        ).replace(
            "$HOVER", hover_color
        ).replace(
            "$BG1", background_color
        ))

    def add_style(self, style: str):
        self.setStyleSheet(self.styleSheet() + style)
