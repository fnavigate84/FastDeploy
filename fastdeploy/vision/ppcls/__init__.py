# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
import logging
import fastdeploy as fd
from fastdeploy import C


class Model(fd.FastDeployModel):
    def __init__(self,
                 model_file,
                 params_file,
                 config_file,
                 backend_option=None,
                 model_format=fd.Frontend.PADDLE):
        super(Model, self).__init__(backend_option)

        assert model_format == fd.Frontend.PADDLE, "PaddleClas only support model format of Frontend.Paddle now."
        self._model = C.vision.ppcls.Model(model_file, params_file,
                                           config_file, self._runtime_option,
                                           model_format)
        assert self.initialized, "PaddleClas model initialize failed."

    def predict(self, input_image, topk=1):
        return self._model.predict(input_image, topk)