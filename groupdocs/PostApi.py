#!/usr/bin/env python
"""
Copyright 2012 GroupDocs.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os

from models import *
from groupdocs.FileStream import FileStream
from groupdocs.ApiClient import ApiException

class PostApi(object):

    def __init__(self, apiClient):
        self.apiClient = apiClient
        self.__basePath = "https://dev-api.groupdocs.com/v2.0"

    @property
    def basePath(self):
        return self.__basePath
    
    @basePath.setter
    def basePath(self, value):
        self.__basePath = value

    
    def RenameByPost(self, userId, fileId, newName, **kwargs):
        """Rename by post

        Args:
            userId, str: User GUID (required)
            fileId, str: File GUID (required)
            newName, str: New name (required)
            
        Returns: RenameResponse
        """
        if( userId == None or fileId == None or newName == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'fileId', 'newName']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method RenameByPost" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/post/file.rename?user_id={userId}&file_id={fileId}&new_name={newName}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            queryParams['user_id'] = self.apiClient.toPathValue(params['userId'])
        if ('fileId' in params):
            queryParams['file_id'] = self.apiClient.toPathValue(params['fileId'])
        if ('newName' in params):
            queryParams['new_name'] = self.apiClient.toPathValue(params['newName'])
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'RenameResponse')
        return responseObject
        
        
    def DeleteByPost(self, userId, fileId, **kwargs):
        """Delete by post

        Args:
            userId, str: User GUID (required)
            fileId, str: File GUID (required)
            
        Returns: DeleteResponse
        """
        if( userId == None or fileId == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'fileId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteByPost" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/post/file.delete?user_id={userId}&file_id={fileId}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            queryParams['user_id'] = self.apiClient.toPathValue(params['userId'])
        if ('fileId' in params):
            queryParams['file_id'] = self.apiClient.toPathValue(params['fileId'])
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeleteResponse')
        return responseObject
        
        
    def DeleteFromFolderByPost(self, userId, path, **kwargs):
        """Delete from folder by post

        Args:
            userId, str: User GUID (required)
            path, str: Path (required)
            
        Returns: DeleteResponse
        """
        if( userId == None or path == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'path']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method DeleteFromFolderByPost" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/post/file.delete.in?user_id={userId}&path={path}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            queryParams['user_id'] = self.apiClient.toPathValue(params['userId'])
        if ('path' in params):
            queryParams['path'] = self.apiClient.toPathValue(params['path'])
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'DeleteResponse')
        return responseObject
        
        
    def CompressByPost(self, userId, fileId, archiveType, **kwargs):
        """Compress by post

        Args:
            userId, str: User GUID (required)
            fileId, str: File GUID (required)
            archiveType, str: Archive Type (required)
            
        Returns: CompressResponse
        """
        if( userId == None or fileId == None or archiveType == None ):
            raise ApiException(400, "missing required parameters")
        allParams = ['userId', 'fileId', 'archiveType']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method CompressByPost" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/post/file.compress?user_id={userId}&file_id={fileId}&archive_type={archiveType}'.replace('*', '')
        pos = resourcePath.find("?")
        if pos != -1:
            resourcePath = resourcePath[0:pos]
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}

        if ('userId' in params):
            queryParams['user_id'] = self.apiClient.toPathValue(params['userId'])
        if ('fileId' in params):
            queryParams['file_id'] = self.apiClient.toPathValue(params['fileId'])
        if ('archiveType' in params):
            queryParams['archive_type'] = self.apiClient.toPathValue(params['archiveType'])
        postData = (params['body'] if 'body' in params else None)
        response = self.apiClient.callAPI(self.basePath, resourcePath, method, queryParams,
                                          postData, headerParams)

        if not response:
            return None

        responseObject = self.apiClient.deserialize(response, 'CompressResponse')
        return responseObject
        
        
    


