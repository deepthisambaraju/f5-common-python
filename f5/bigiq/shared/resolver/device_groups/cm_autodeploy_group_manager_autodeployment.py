# coding=utf-8
#
# Copyright 2016 F5 Networks Inc.
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
#

"""BIG-IQ® Device Groups (shared) module for CM AutoDeployed Devices

REST URI
    ``http://localhost/mgmt/shared/resolver/device-groups/cm-autodeploy-group-manager-autodeployment``

GUI Path
    ``Device Management --> Inventory``

REST Kind
    N/A -- HTTP GET returns an error
"""

from f5.bigiq.resource import Collection
from f5.bigiq.resource import Resource
from f5.sdk_exception import F5SDKError


class Cm_Autodeploy_Group_Manager_Autodeployment(Resource):
    def __init__(self, device_groups):
        super(Cm_Autodeploy_Group_Manager_Autodeployment,
              self).__init__(device_groups)
        self._meta_data['required_json_kind'] = \
            'shared:resolver:device-groups:devicegroupstate'
        self._meta_data['attribute_registry'] = {
            'cm:shared:licensing:pools:licensepoolmembercollectionstate':
                Devices_s
        }
        self._meta_data['allowed_lazy_attributes'] = [
            Devices_s
        ]


class Devices_s(Collection):
    def __init__(self, cm_autodeploy_group_manager_autodeployment):
        super(Devices_s, self).__init__(
            cm_autodeploy_group_manager_autodeployment
        )
        self._meta_data['allowed_lazy_attributes'] = [Device]
        self._meta_data['required_json_kind'] = \
            'shared:resolver:device-groups:devicegroupdevicecollectionstate'
        self._meta_data['attribute_registry'] = {
            'shared:resolver:device-groups:restdeviceresolverdevicestate': Device  # NOQA
        }


class Device(Resource):
    def __init__(self, devices_s):
        super(Device, self).__init__(devices_s)
        self._meta_data['required_json_kind'] = \
            'shared:resolver:device-groups:restdeviceresolverdevicestate'
        self._meta_data['required_creation_parameters'] = set(
            ('address', 'password', 'rootPassword')
        )
        self._meta_data['required_load_parameters'] = str(('uuid',))

    def update(self, **kwargs):
        raise F5SDKError(
            'Auto Deploy items can be created or deleted, not updated'
        )
