
from libtaxii.constants import *

from .bindings import *
from .exceptions import raise_failure
from .transform import parse_message

#: HTTP Headers
HTTP_CONTENT_TYPE = 'Content-Type'
HTTP_ACCEPT = 'Accept'
HTTP_X_TAXII_CONTENT_TYPE = 'X-TAXII-Content-Type'
HTTP_X_TAXII_PROTOCOL = 'X-TAXII-Protocol'
HTTP_X_TAXII_ACCEPT = 'X-TAXII-Accept'
HTTP_X_TAXII_SERVICES = 'X-TAXII-Services'

HTTP_CONTENT_XML = 'application/xml'

BASIC_REQUEST_HEADERS = (HTTP_CONTENT_TYPE, HTTP_X_TAXII_CONTENT_TYPE)

REQUIRED_REQUEST_HEADERS = BASIC_REQUEST_HEADERS + (HTTP_X_TAXII_SERVICES,)
REQUIRED_RESPONSE_HEADERS = (HTTP_CONTENT_TYPE, HTTP_X_TAXII_CONTENT_TYPE, HTTP_X_TAXII_PROTOCOL, HTTP_X_TAXII_SERVICES)

TAXII_11_HTTPS_Headers = {
    HTTP_CONTENT_TYPE: HTTP_CONTENT_XML,
    HTTP_X_TAXII_CONTENT_TYPE: VID_TAXII_XML_11,
    HTTP_X_TAXII_PROTOCOL: VID_TAXII_HTTPS_10,
    HTTP_X_TAXII_SERVICES: VID_TAXII_SERVICES_11
}

TAXII_11_HTTP_Headers = {
    HTTP_CONTENT_TYPE: HTTP_CONTENT_XML,
    HTTP_X_TAXII_CONTENT_TYPE: VID_TAXII_XML_11,
    HTTP_X_TAXII_PROTOCOL: VID_TAXII_HTTP_10,
    HTTP_X_TAXII_SERVICES: VID_TAXII_SERVICES_11
}

TAXII_10_HTTPS_Headers = {
    HTTP_CONTENT_TYPE: HTTP_CONTENT_XML,
    HTTP_X_TAXII_CONTENT_TYPE: VID_TAXII_XML_10,
    HTTP_X_TAXII_PROTOCOL: VID_TAXII_HTTPS_10,
    HTTP_X_TAXII_SERVICES: VID_TAXII_SERVICES_10
}

TAXII_10_HTTP_Headers = {
    HTTP_CONTENT_TYPE: HTTP_CONTENT_XML,
    HTTP_X_TAXII_CONTENT_TYPE: VID_TAXII_XML_10,
    HTTP_X_TAXII_PROTOCOL: VID_TAXII_HTTP_10,
    HTTP_X_TAXII_SERVICES: VID_TAXII_SERVICES_10
}


def get_content_type(headers):
    return headers[HTTP_X_TAXII_CONTENT_TYPE]


def get_http_headers(version, is_secure):

    taxii_11 = [VID_TAXII_XML_11, VID_TAXII_SERVICES_11]
    taxii_10 = [VID_TAXII_XML_10, VID_TAXII_SERVICES_10]

    if version in taxii_11:
        if is_secure:
            return TAXII_11_HTTPS_Headers
        else:
            return TAXII_11_HTTP_Headers
    elif version in taxii_10:
        if is_secure:
            return TAXII_10_HTTPS_Headers
        else:
            return TAXII_10_HTTP_Headers

    raise ValueError("Unknown combination: version=%s, is_secure=%s" % (version, is_secure))

