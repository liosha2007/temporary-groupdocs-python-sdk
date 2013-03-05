####<i>This sample will show how to use <b>MoveFile</b> method from Storage Api to copy/move a file in GroupDocs Storage </i>

#Import of classes from libraries
import base64

from pyramid.renderers import render_to_response

# Checking value on null
def IsNotNull(value):
    return value is not None and len(value) > 0

####Set variables and get POST data
def sample09(request):
    fileGuId = request.POST.get('fileId')
    width = request.POST.get('width') or '300'
    height = request.POST.get('height') or '200'
    #Checking parameters
    if IsNotNull(fileGuId) == False:
        return render_to_response('__main__:templates/sample09.pt',
                                  { 'error' : 'You do not enter all parameters' })
    #Generation of iframe URL using fileGuId
    iframe_url = 'https://apps.groupdocs.com/document-viewer/embed/' + fileGuId + '?frameborder=0&width=' + width + '&height=' + height
    #If request was successfull - set variables for template
    return render_to_response('__main__:templates/sample09.pt',
                              { 
                               'iframe_url' : iframe_url,
                               'fileId' : fileGuId,
                               'width' : width,
                               'height' : height },
                              request=request)
