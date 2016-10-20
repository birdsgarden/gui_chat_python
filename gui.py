__author__ = 'cxtan'
import wx
class my_frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "cxtan", size = (300, 200))
        panel = wx.Panel(self, -1)
        label = wx.StaticText(panel, -1, "hell cxtan", (100,10))
        txt = wx.TextCtrl(panel, -1, "input your name:", (100,50))
        txt.SetInsertionPoint(0)

        self.button = wx.Button(panel, -1, "connect", pos = (100, 100))
if __name__ == '__main__':
    app = wx.App()
    mframe = my_frame()
    mframe.Show()
    app.MainLoop()
    pass



































