"""
A library of functions that support credential management using *Gnome*
`libsecret`

Created on May 12, 2020

@author: Jonathan Gossage
"""

from gi.repository import Secret

class Secrets():
    def __init__(self):
        """Define the predefined schemas and attributes for `libsecret`"""
        # Define the attributes
        # Define the password schema
        self._passwordSchema = Secret.Schema.new()

    def getSecret(self):
        pass

    def putSecret(self):
        pass

    def deleteSecret(self):
        pass

    def defineSecretSchema(self, schema, name='GlobalVillage.Schema',
                           attributes=None, roles=None):
        sch = Secret.Schema.new(name, Secret.SchemaFlags.NONE, schema)

    def createSchemaAttributes(self, **kwargs):
        return {k:v for (k, v) in kwargs.items()}

