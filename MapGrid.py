from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtCore import Qt, QPointF

class TokenItem(QGraphicsPixmapItem):
    def __init__(self, pixmap, name, grid_size=48):
        super().__init__(pixmap)
        self.setFlags(
            QGraphicsPixmapItem.ItemIsMovable |
            QGraphicsPixmapItem.ItemIsSelectable
        )
        self.setAcceptHoverEvents(True)
        self.setToolTip(name)
        self.grid_size = grid_size

    def mouseReleaseEvent(self, event):
        # Snap to grid on release
        pos = self.pos()
        x = round(pos.x() / self.grid_size) * self.grid_size
        y = round(pos.y() / self.grid_size) * self.grid_size
        self.setPos(QPointF(x, y))
        super().mouseReleaseEvent(event)