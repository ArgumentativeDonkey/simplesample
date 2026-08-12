from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget

from import_utils import ImportManager


class TrackList(QWidget):
    track_selected: Signal = Signal(Path)
    
    def __init__(self, import_manager: ImportManager):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.list = QTreeWidget()
        self.list.setRootIsDecorated(False)
        self.list.setHeaderLabels(["Path", "Name"])
        self.list.setColumnHidden(0, True)
        self.import_manager = import_manager

        self.list.itemSelectionChanged.connect(self.on_track_selected)

        self.add_paths(self.import_manager.imported_paths)
        self.list.show()

        layout.addWidget(self.list)

    def reload(self):
        self.list.clear()
        self.import_manager.reload()

    def add_paths(self, paths: list[Path]):
        self.list.addTopLevelItems([QTreeWidgetItem([str(path), path.name]) for path in paths])

    def on_track_selected(self):
        item = self.list.currentItem()
        path = Path(item.text(0))
        if not path.exists() or not path.is_file():
            self.import_manager.remove(path)
            # item = self.list.rehe item when we use takeItem.
            idx = self.list.indexOfTopLevelItem(item)
            item = self.list.takeTopLevelItem(idx)
            del item
            return
        self.track_selected.emit(path)