## This file is part of Scapy
## See http://www.secdev.org/projects/scapy for more informations
## Copyright (C) Arnaud Ebalard <arno@natisbad.org>
## This program is published under a GPLv2 license

"""
Tools for handling with digital certificates.
"""

try:
    import cryptography
except ImportError:
    import logging
    log_loading = logging.getLogger("kamene.loading")
    log_loading.info("Can't import python cryptography. Disabled certificate manipulation tools")
else:
    from kamene.crypto.cert import *
