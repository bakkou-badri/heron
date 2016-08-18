# copyright 2016 twitter. all rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''module for example bolt: Consume Bolt'''
from heron.pyheron.src.python import Bolt

# pylint: disable=unused-argument
class ConsumeBolt(Bolt):
  def initialize(self, config, context):
    self.logger.info("In prepare() of ConsumerBolt")
    self.total = 0

  def process(self, tup):
    if self.is_tick(tup):
      self.log("Got tick tuple!")
      self.log("Total received data tuple: %d" % self.total)
    else:
      self.total += 1