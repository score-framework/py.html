# Copyright © 2015 STRG.AT GmbH, Vienna, Austria
#
# This file is part of the The SCORE Framework.
#
# The SCORE Framework and all its parts are free software: you can redistribute
# them and/or modify them under the terms of the GNU Lesser General Public
# License version 3 as published by the Free Software Foundation which is in the
# file named COPYING.LESSER.txt.
#
# The SCORE Framework and all its parts are distributed without any WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. For more details see the GNU Lesser General Public
# License.
#
# If you have not received a copy of the GNU Lesser General Public License see
# http://www.gnu.org/licenses/.
#
# The License-Agreement realised between you as Licensee and STRG.AT GmbH as
# Licenser including the issue of its valid conclusion and its pre- and
# post-contractual effects is governed by the laws of Austria. Any disputes
# concerning this License-Agreement including the issue of its valid conclusion
# and its pre- and post-contractual effects are exclusively decided by the
# competent court, in whose district STRG.AT GmbH has its registered seat, at
# the discretion of STRG.AT GmbH also the competent court, in whose district the
# Licensee has his registered seat, an establishment or assets.

import os
from score.init import init_cache_folder, ConfiguredModule


defaults = {
    'rootdir': None,
    'cachedir': None,
}


def init(confdict, tpl):
    """
    Initializes this module acoording to :ref:`our module initialization
    guidelines <module_initialization>` with the following configuration keys:

    :confkey:`rootdir` :confdefault:`None`
        Denotes the root folder containing the html templates. Will fall back
        to the folder in :mod:`score.tpl`'s configuration.

    :confkey:`cachedir` :confdefault:`None`
        A dedicated cache folder for this module. It is generally sufficient
        to provide a ``cachedir`` for :mod:`score.tpl`, as this module will
        use a sub-folder of that by default.
    """
    conf = dict(defaults.items())
    conf.update(confdict)
    if not conf['cachedir'] and tpl.cachedir:
        conf['cachedir'] = os.path.join(tpl.cachedir, 'js')
    if conf['cachedir']:
        init_cache_folder(conf, 'cachedir', autopurge=True)
    if not conf['rootdir']:
        conf['rootdir'] = tpl.rootdir
    tpl.renderer.register_format('html', conf['rootdir'], conf['cachedir'])
    return ConfiguredHtmlModule()


class ConfiguredHtmlModule(ConfiguredModule):
    """
    This module's :class:`configuration object
    <score.init.ConfiguredModule>`.
    """

    def __init__(self):
        super().__init__(__package__)
