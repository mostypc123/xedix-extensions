    import wx

    def OnRunRepomixTxt(self, event):
        subprocess.run("npx repomix --style plain")
    
    def OnRunRepomixXml(self, event):
        subprocess.run("npx repomix --style xml")

    def OnRunRepomixMd(self, event):
        subprocess.run("npx repomix --style markdown")
