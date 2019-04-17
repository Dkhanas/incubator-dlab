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

# TODO: Nodes deployment versions nodes with new and old deployment procedures

import abc
import six

from dlab.common.exceptions import DLabException
from dlab.common import node
from dlab.common.repositories import ArrayRepository


registry = ArrayRepository()


def register(key):
    """Register a class as a plug-in"""
    def wrapper(cls):
        # TODO show error if key already exists
        registry.append(key, cls)
        return cls

    return wrapper


@six.add_metaclass(abc.ABCMeta)
class BaseController:

    LC_WRONG_NODE = 'There is no node type "{name}" in available nodes list'

    def __init__(self, logger):
        self._type = None
        self._logger = logger
        logger.debug('Init controller "{name}".'.format(
            name=self.__class__.__name__
        ))

    @classmethod
    def get_node(cls, name):
        try:
            items = node.registry.find_one(cls.__module__)
            return items[name]
        except KeyError as e:
            raise DLabException(e)

    @abc.abstractproperty
    def get_data_engine_node(self):
        pass

    @abc.abstractproperty
    def get_data_engine_server_node(self):
        pass

    @abc.abstractproperty
    def get_edge_node(self):
        pass

    @abc.abstractproperty
    def get_notebook_node(self):
        pass

    @abc.abstractproperty
    def get_ssn_node(self):
        pass
