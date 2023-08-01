
import os;
import shutil;
from PyQt5.QtWidgets import *;
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap;
import sys;



list = 'C:/Program Files (x86)/Steam/steamapps/workshop/content/636480'
destination = 'C:/Program Files (x86)/Steam/steamapps/workshop/content/636480/saved'


green = '\u001b[32m';
reset = '\u001b[0m';

os.system("cls");

def clearMods():

    print("Moving files")

    for path, dirs, files in os.walk(list):
        for d in dirs:
            dest = shutil.move(list + "/" + d, destination); 

    print("done!")

def getModID(modName, type):

    dirTarget = "";
    if(type == "LOADED"):
        dirTarget = list;
    elif(type == "SAVED"):
        dirTarget = destination;
    for path, dirs, files in os.walk(dirTarget):
        for d in dirs:         
            if(os.path.isfile(dirTarget + "/" + d + "/" + modName)):
               return d;    

def loadMod(name, id):
    shutil.move(destination + "/" + id, list +  "/" + id);           
    print("Loaded mod " + name + "! (" + id + ")");

def unloadMod(name, id):
    shutil.move(list + "/" + id, destination +  "/" + id);           
    print("Unloaded mod " + name + "! (" + id + ")");


def getLoaded():

    loadedMods = [];
    
    for path, dirs, files in os.walk(list):

        dirname = path.split(os.path.sep)[-1];
        if(dirname == "saved"):
            break;
        
        #print(green,"\n============================",dirname,"============================",reset);
        
        for f in files:
        
            if("rfc" in f or "rfl" in f):
                loadedMods.append(f);
    return loadedMods


def getSaved():
    savedMods = [];
    for path, dirs, files in os.walk(destination):
                
        dirname = path.split(os.path.sep)[-1];
        
        #print(green,"\n============================",dirname,"============================",reset);
   
        for f in files:
            if("rfc" in f or "rfl" in f):
                savedMods.append(f);
                
    return savedMods;
def unloadAll(modList):
    for mod in modList:
        for path, dirs, files in os.walk(list):
            for d in dirs:                            
                if(os.path.isfile(list + "/" + d + "/" + mod)):
                    unloadMod(mod, d);
                    
def loadAll(modList):
    for mod in modList:
        for path, dirs, files in os.walk(list):
            for d in dirs:                            
                if(os.path.isfile(list + "/" + d + "/" + mod)):
                    loadMod(mod, d);
def loadImg(id, type):
    path = "";
    if(type == "LOADED"):
        path = list;
    elif(type == "SAVED"):
        path = destination;
    path = path + "/"+id + "/icon.png";
    print(path);
    img = QPixmap(path)
    img = img.scaled(256, 256);
    return img
    

class App(QWidget):

    loadedMods = None
    savedMods = None;
    modIcon = None;
    
    def __init__(self):
        super().__init__()
        self.title = 'Mod Manager'
        self.left = 10
        self.top = 100
        self.width = 800
        self.height = 800
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.modIcon = QLabel("sex", self)
        self.modIcon.setFixedSize(256, 256);
        self.modIcon.move(450,20);
        
        self.loadedMods = QListWidget()
        self.loadedMods.setFixedSize(400, 400)
        self.loadedMods.clicked.connect(self.show_loaded_icon)
        loadList = getLoaded();
        #os.system("cls");
        
        for mod in loadList:
            QListWidgetItem(mod, self.loadedMods)
        #itemsTextList =  [str(self.loadedMods.item(i).text()) for i in range(self.loadedMods.count())]
        #unloadAll(itemsTextList);

        self.savedMods = QListWidget()
        self.savedMods.setFixedSize(400, 400)
        self.savedMods.clicked.connect(self.show_saved_icon)
        savedList = getSaved();
        for mod in savedList:
            QListWidgetItem(mod, self.savedMods)
        
        window_layout = QVBoxLayout(self)
        window_layout.addWidget(self.loadedMods)
        window_layout.addWidget(self.savedMods)
        self.setLayout(window_layout)
        
        button = QPushButton('Load', self)
        button.move(500,300)
        button.clicked.connect(self.btn_load)
        
        unloadBtn = QPushButton('Unload', self)
        unloadBtn.move(600,300)
        unloadBtn.clicked.connect(self.btn_unload)
        
        self.show()

    @pyqtSlot()
    def btn_load(self):
        item = self.savedMods.currentItem()
        self.loadedMods.addItem(item.text());
        self.savedMods.takeItem(self.savedMods.row(item))
        loadMod(item.text(),getModID(item.text(), "SAVED"));
    def btn_unload(self):
        item = self.loadedMods.currentItem()
        if(item == None):
            return;
        self.savedMods.addItem(item.text());
        self.loadedMods.takeItem(self.loadedMods.row(item))
        unloadMod(item.text(),getModID(item.text(), "LOADED"));
        
    def show_saved_icon(self, savedMods):
        item = self.savedMods.currentItem()
        print(item.text())
        
        self.modIcon.setPixmap(loadImg(getModID(item.text(),"SAVED"), "SAVED"))
        
    def show_loaded_icon(self, loadedMods):
        item = self.loadedMods.currentItem()
        print(item.text())
        
        self.modIcon.setPixmap(loadImg(getModID(item.text(),"LOADED"), "LOADED"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

    
    