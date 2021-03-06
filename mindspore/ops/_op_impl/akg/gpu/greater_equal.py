# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""GreaterEqual op"""
from mindspore.ops.op_info_register import op_info_register, AkgRegOp, DataType

greater_equal_op_info = AkgRegOp("GreaterEqual") \
    .fusion_type("OPAQUE") \
    .input(0, "x") \
    .input(1, "y") \
    .output(0, "output") \
    .dtype_format(DataType.F16_Default, DataType.F16_Default, DataType.BOOL_Default) \
    .dtype_format(DataType.F32_Default, DataType.F32_Default, DataType.BOOL_Default) \
    .dtype_format(DataType.I32_Default, DataType.I32_Default, DataType.BOOL_Default) \
    .get_op_info()


@op_info_register(greater_equal_op_info)
def _greater_equal_akg():
    """GreaterEqual register"""
    return
