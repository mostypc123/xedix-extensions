    import wx
    import main # noqa

    txt_repomix_item = main.TextEditor.toolsMenu.Append(wx.ID_ANY, "&Run Repomix (txt)", "Run Repomix on current folder")
    xml_repomix_item = main.TextEditor.toolsMenu.Append(wx.ID_ANY, "&Run Repomix (xml)", "Run Repomix on current folder")
    md_repomix_item  = main.TextEditor.toolsMenu.Append(wx.ID_ANY, "&Run Repomix (markdown)", "Run Repomix on current folder")
