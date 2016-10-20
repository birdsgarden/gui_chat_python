__author__ = 'cxtan'
import wx
class my_frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "cxtan", size = (300, 200))
        label = wx.StaticText(self, -1, "hell cxtan", (100,10), (160, 1),  wx.ALIGN_CENTER)
        label.SetBackgroundColour("black")
        label.SetForegroundColour("green")
if __name__ == '__main__':
    app = wx.App()
    mframe = my_frame()
    mframe.Show()
    app.MainLoop()
    pass



































