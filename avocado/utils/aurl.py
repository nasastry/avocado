# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: Red Hat Inc. 2013-2014
# Author: Lucas Meneghel Rodrigues <lmr@redhat.com>

"""
URL related functions.

The strange name is to avoid accidental naming collisions in code.
"""
import logging
import urllib.parse

#: The most common schemes (protocols) used in URLs
COMMON_SCHEMES = ("http", "https", "ftp", "git")

LOG = logging.getLogger(__name__)


def is_url(path):
    """Return `True` if path looks like an URL of common protocols.

    Refer to :data:`COMMON_SCHEMES` for the list of common protocols.

    :param path: path to check.
    :rtype: Boolean.
    """
    LOG.warning(
        "The aurl utility is deprecated and will be removed after the next LTS release."
    )
    url_parts = urllib.parse.urlparse(path)
    return url_parts[0] in COMMON_SCHEMES
