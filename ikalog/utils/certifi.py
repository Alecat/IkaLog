#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  IkaLog
#  ======
#  Copyright (C) 2015 Takeshi HASEGAWA
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os.path

from ikalog.utils.ikautils import *

class Certifi(object):

    @staticmethod
    def where():
        cacert_pem = os.path.join(IkaUtils.baseDirectory(), 'cacert.pem')
        if os.path.exists(cacert_pem):
            return cacert_pem

        try:
            import certifi
            cacert_pem = certifi.where()
            if os.path.exists(cacert_pem):
                return cacert_pem
        except ImportError:
            pass

        try:
            import requests.certs
            cacert_pem = requests.certs.where()
            if os.path.exists(cacert_pem):
                return cacert_pem
        except ImportError:
            pass

        IkaUtils.dprint('ikalog.utils.Certifi: Cannot find any cacert.pem')

        return None
