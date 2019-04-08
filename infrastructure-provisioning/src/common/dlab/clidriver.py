# *****************************************************************************
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# ******************************************************************************
# TODO: CliDriver is Controllers factory
# TODO: mv dlab.* => dlabcli.*
import sys
import signal
import logging

from dlab.common.exceptions import DLabException
from dlab.common.controllers import BaseController, registry as cls_registry
from dlab.common.nodes.base import BaseNode

LOG = logging.getLogger('dlabcli.clidriver')
LOG_FORMAT = (
    '%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')


def main():
    driver = create_clidriver()  # type: CLIDriver
    rc = driver.main()
    return rc


def create_clidriver():
    return CLIDriver()


class CLIDriver(object):

    @staticmethod
    def _get_logger():
        logger = logging
        logger.basicConfig(level=logging.DEBUG)
        return logger

    @staticmethod
    def _get_option():
        option = 'aws'

        ctl = cls_registry.find_one(option)
        if ctl:
            return option

        # TODO: show message here if option not in list

    def _execute(self):
        logger = self._get_logger()
        option = self._get_option()

        ctl_name = cls_registry.find_one(option)
        # TODO: set controller type
        ctl = ctl_name(logger)  # type: BaseController
        node = ctl.current_node()  # type: BaseNode
        ctl.execute(node)

    @staticmethod
    def _show_error(msg):
        LOG.debug(msg, exc_info=True)
        sys.stderr.write(msg)
        sys.stderr.write('\n')

    def main(self):
        try:
            self._execute()
            return 0
        # except UnknownArgumentError as e:
        #     return 255
        except DLabException:
            LOG.debug("Exception caught in dlab lib", exc_info=True)
            LOG.debug("Exiting with rc 255")
        except KeyboardInterrupt:
            # Shell standard for signals that terminate
            # the process is to return 128 + signum, in this case
            # SIGINT=2, so we'll have an RC of 130.
            sys.stdout.write("\n")
            return 128 + signal.SIGINT
        except Exception:
            LOG.debug("Exception caught in main()", exc_info=True)
            LOG.debug("Exiting with rc 255")
            return 255
