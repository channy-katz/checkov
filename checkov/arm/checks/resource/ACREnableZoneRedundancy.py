from __future__ import annotations

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.arm.base_resource_check import BaseResourceCheck

from typing import Any


class ACREnableZoneRedundancy(BaseResourceCheck):

    def __init__(self) -> None:
        """
        Zone redundancy provides resiliency and high availability to
        a registry or replication resource in a specific region. Supported on Premium.
        """
        name = "Ensure Azure Container Registry (ACR) is zone redundant"
        id = "CKV_AZURE_233"
        supported_resources = ("Microsoft.ContainerRegistry/registries","Microsoft.ContainerRegistry/registries/replications")
        categories = (CheckCategories.BACKUP_AND_RECOVERY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:
        # check registry. default=false
        if conf.get("properties").get("zoneRedundancy", []) != [True]:
            return CheckResult.FAILED

        # check each replica. default=false
        replications = conf.get("replications", {})
        for replica in replications:
            zone_redundancy_enabled = replica.get('zoneRedundancy', [])
            if zone_redundancy_enabled != [True]:
                return CheckResult.FAILED

        return CheckResult.PASSED


check = ACREnableZoneRedundancy()
