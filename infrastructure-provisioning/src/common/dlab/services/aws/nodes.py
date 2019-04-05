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

from dlab.common import nodes


class AWSSSNNode(nodes.SSNNode):

    def run(self):
        pass

    def terminate(self):
        pass


class AWSEDGENode(nodes.EDGENode):

    def run(self):
        pass

    def terminate(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def get_status(self):
        pass

    def recreate(self):
        pass

    def reload_keys(self):
        pass


class AWSNotebookNode(nodes.NotebookNode):

    def run(self):
        pass

    def terminate(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def install_libraries(self):
        pass

    def show_libraries(self):
        pass

    def configure(self):
        pass

    def git_creds(self):
        pass


class AWSDataEngineNode(nodes.DataEngineNode):

    def run(self):
        pass

    def terminate(self):
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def install_libraries(self):
        pass

    def show_libraries(self):
        pass


class AWSDataEngineServerNode(nodes.DataEngineServerNode):

    def run(self):
        pass

    def terminate(self):
        pass

    def install_libraries(self):
        pass

    def show_libraries(self):
        pass
