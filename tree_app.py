import sys
from PySide6 import QtWidgets

data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": ["file_rahasia.csv"]}

app = QtWidgets.QApplication()

tree = QtWidgets.QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

items = []
for key, values in data.items():
    item = QtWidgets.QTreeWidgetItem([key, "folder"])
    for value in values:
        ext = value.split(".")[-1].upper()
        child = QtWidgets.QTreeWidgetItem([value, ext])
        item.addChild(child)
    items.append(item)

tree.insertTopLevelItems(0, items)

tree.show()
sys.exit(app.exec())