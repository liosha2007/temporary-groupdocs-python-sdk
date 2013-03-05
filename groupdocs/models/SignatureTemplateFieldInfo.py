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
"""
class SignatureTemplateFieldInfo:
    """
    
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'id': 'str',
            'templateId': 'str',
            'recipientId': 'str',
            'name': 'str',
            'mandatory': 'bool',
            'order': 'float',
            'regularExpression': 'str',
            'signatureFieldId': 'float',
            'locations': 'list[SignatureTemplateFieldLocationInfo]',
            'fieldType': 'int',
            'acceptableValues': 'str',
            'defaultValue': 'str',
            'tooltip': 'str'

        }


        self.id = None # str
        self.templateId = None # str
        self.recipientId = None # str
        self.name = None # str
        self.mandatory = None # bool
        self.order = None # float
        self.regularExpression = None # str
        self.signatureFieldId = None # float
        self.locations = None # list[SignatureTemplateFieldLocationInfo]
        self.fieldType = None # int
        self.acceptableValues = None # str
        self.defaultValue = None # str
        self.tooltip = None # str
        
