import wx as wx        #Libreria de python para jframe              

app = wx.App()                 #Creacion de objeto
frame = wx.Frame(None, title="Hola mundo") #JFrame con titulo hola mundo
frame.Show()                               #Hacemos visible el jframe
app.MainLoop()                             #Llamamos el metodo Mainloop usando el objeto