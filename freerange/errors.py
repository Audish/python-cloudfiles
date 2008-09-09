
"""
exception classes

See COPYING for license information.
"""

class ResponseError(Exception):
    """
    Raised when the remote service returns an error.
    """
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason
        Exception.__init__(self)

    def __str__(self):
        return '%d: %s' % (self.status, self.reason)

    def __repr__(self):
        return '%d: %s' % (self.status, self.reason)

class NoSuchContainer(Exception):
    """
    Raised on a non-existent Container.
    """
    pass

class NoSuchObject(Exception):
    """
    Raised on a non-existent Object.
    """
    pass

class ContainerNotEmpty(Exception):
    """
    Raised when attempting to delete a Container that still contains Objects.
    """
    def __init__(self, container_name):
        self.container_name = container_name
        
    def __str__(self):
        return "Cannot delete non-empty Container %s" % self.container_name
    
    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.container_name)

class InvalidContainerName(Exception):
    """
    Raised for invalid storage container names.
    """

class InvalidObjectName(Exception):
    """
    Raised for invalid storage object names.
    """
    pass

class InvalidUrl(Exception):
    """
    Not a valid url for use with this software.
    """
    pass

class InvalidObjectSize(Exception):
    """
    Not a valid storage_object size attribute.
    """
    pass

class IncompleteSend(Exception):
    """
    Raised when there is a insufficient amount of data to send.
    """
    pass
