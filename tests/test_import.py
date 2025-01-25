from types import ModuleType

import cloudcoil.models.kyverno as kyverno


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), kyverno.__dict__.values()))
    assert modules, "No modules found in kyverno"
