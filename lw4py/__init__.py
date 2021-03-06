# -*- coding: utf-8 -*-
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of ws4py nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
import logging
import logging.handlers as handlers

__author__ = 'Qitian Chan'
__version__ = '0.1.0'
__all__ = ['configure_logger', 'NETWORKID']


NETWORKID = 0b01010000
def configure_logger(stdout=True, filepath=None, level=logging.INFO):
    logger = logging.getLogger('lrw4py')
    logger.setLevel(level)
    logfmt = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s")

    if filepath:
        h = handlers.RotatingFileHandler(filepath, maxBytes=10485760, backupCount=3)
        h.setLevel(level)
        h.setFormatter(logfmt)
        logger.addHandler(h)

    if stdout:
        import sys
        h = logging.StreamHandler(sys.stdout)
        h.setLevel(level)
        h.setFormatter(logfmt)
        logger.addHandler(h)

    return logger