import unittest

from checkov.terraform.models.enums import CheckResult
from checkov.terraform.checks.resource.aws.SagemakerEncryption import check


class TestSagemakerEncryption(unittest.TestCase):

    def test_failure(self):
        resource_conf = {'name': ['my-notebook-instance'], 'role_arn': ['${aws_iam_role.role.arn}'],
                         'instance_type': ['ml.t2.medium']}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILURE, scan_result)

    def test_success(self):
        resource_conf = {'name': ['my-notebook-instance'], 'role_arn': ['${aws_iam_role.role.arn}'],
                         'instance_type': ['ml.t2.medium'], 'kms_key_id': ['foo']}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.SUCCESS, scan_result)

if __name__ == '__main__':
    unittest.main()
