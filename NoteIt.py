import wx
import datetime
class Example(wx.Frame):
    app = wx.App()
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, 
            size=(260, 180))
       
        self.InitUI()
        self.Centre()
        self.Show()     
        
    def InitUI(self):
    
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        self.SetMenuBar(menubar)
        
        nmi = wx.MenuItem(fileMenu, wx.ID_NEW, '&New\tCtrl+N')
        fileMenu.AppendItem(nmi)
        smi = wx.MenuItem(fileMenu, wx.ID_SAVE, '&Save\tCtrl+S')
        fileMenu.AppendItem(smi)
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)
        
        self.Bind(wx.EVT_MENU, self.new, nmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        self.Bind(wx.EVT_MENU, self.savetext, smi)
        
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.tv=wx.TextCtrl(self, style=wx.TE_MULTILINE)
    def new(self, e):
        self.tv.Clear()
    def savetext(self,e):
        s=self.tv.GetValue()
        if s:
            now = datetime.datetime.now()
            now1=str(now)[:19]
            f=open(now1+'.txt','w')
            f.write(s)
    def OnQuit(self, e):
        self.Close()


if __name__ == '__main__':
  
    
    Example(None, title='')
    app.MainLoop()