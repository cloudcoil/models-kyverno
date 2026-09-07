# cloudcoil-models-kyverno

Versioned kyverno models for cloudcoil.

[![PyPI](https://img.shields.io/pypi/v/cloudcoil.models.kyverno.svg)](https://pypi.python.org/pypi/cloudcoil.models.kyverno)
[![Downloads](https://static.pepy.tech/badge/cloudcoil.models.kyverno)](https://pepy.tech/project/cloudcoil.models.kyverno)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/license/apache-2-0/)
[![CI](https://github.com/cloudcoil/models-kyverno/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudcoil/models-kyverno/actions/workflows/ci.yml)
> [!WARNING]  
Models are generated from kyverno **1.19.0** using **Cloudcoil 0.7**. Run `uv sync` followed by `make gen-models` to regenerate them from the pinned upstream schema. Cloudcoil infers resource names and normalizes Kubernetes schemas without project-specific patches.


## 🔧 Installation

> [!NOTE]
> For versioning information and compatibility, see the [Versioning Guide](https://github.com/cloudcoil/cloudcoil/blob/main/VERSIONING.md).

Using [uv](https://github.com/astral-sh/uv) (recommended):

```bash
# Install with Kyverno support
uv add cloudcoil.models.kyverno
```

Using pip:

```bash
pip install cloudcoil.models.kyverno
```

## 💡 Examples

### Using Kyverno Models

```python
from cloudcoil import apimachinery
import cloudcoil.models.kyverno.v1 as kyverno

# Create a ClusterPolicy
policy = kyverno.ClusterPolicy(
    metadata=apimachinery.ObjectMeta(name="require-labels"),
    spec=kyverno.ClusterPolicySpec(
        rules=[
            kyverno.Rule(
                name="require-team-label",
                match=kyverno.Match(
                    resources=kyverno.Resources(
                        kinds=["Deployment", "StatefulSet"]
                    )
                ),
                validate=kyverno.Validate(
                    message="The label 'team' is required",
                    pattern={
                        "metadata": {
                            "labels": {
                                "team": "*"
                            }
                        }
                    }
                )
            )
        ]
    )
).create()

# List Policies
for pol in kyverno.ClusterPolicy.list():
    print(f"Found policy: {pol.metadata.name}")

# Update a Policy
policy.spec.rules[0].validate.message = "The 'team' label is mandatory"
policy.save()

# Delete a Policy
kyverno.ClusterPolicy.delete("require-labels")
```

### Using the Fluent Builder API

Cloudcoil provides a powerful fluent builder API for Kyverno resources with full IDE support and rich autocomplete capabilities:

```python
from cloudcoil.models.kyverno.v1 import ClusterPolicy

# Create a ClusterPolicy using the builder
policy = (
    ClusterPolicy.builder()
    .metadata(lambda m: m
        .name("require-labels")
    )
    .spec(lambda s: s
        .rules([
            lambda r: r
            .name("require-team-label")
            .match(lambda m: m
                .resources(lambda res: res
                    .kinds(["Deployment", "StatefulSet"])
                )
            )
            .validate(lambda v: v
                .message("The label 'team' is required")
                .pattern({
                    "metadata": {
                        "labels": {
                            "team": "*"
                        }
                    }
                })
            )
        ])
    )
    .build()
)
```

The fluent builder provides:
- ✨ Full IDE support with detailed type information
- 🔍 Rich autocomplete for all fields and nested objects
- ⚡ Compile-time validation of your configuration
- 🎯 Clear and chainable API that guides you through resource creation

### Using the Context Manager Builder API

For complex nested resources, Cloudcoil also provides a context manager-based builder pattern that can make the structure more clear:

```python
from cloudcoil.models.kyverno.v1 import ClusterPolicy

# Create a policy using context managers
with ClusterPolicy.new() as policy:
    with policy.metadata() as metadata:
        metadata.name("require-labels")
        metadata.labels({"app": "kyverno"})
    
    with policy.spec() as spec:
        with spec.rules() as rules:
            with rules.add() as rule:
                rule.name("require-team-label")
                
                with rule.match() as match:
                    with match.resources() as resources:
                        resources.kinds(["Deployment", "StatefulSet"])
                
                with rule.validate() as validate:
                    validate.message("The label 'team' is required")
                    validate.pattern({
                        "metadata": {
                            "labels": {
                                "team": "*"
                            }
                        }
                    })

final_policy = policy.build()
```

The context manager builder provides:
- 🎭 Clear visual nesting of resource structure
- 🔒 Automatic resource cleanup
- 🎯 Familiar Python context manager pattern
- ✨ Same great IDE support as the fluent builder

### Mixing Builder Styles

CloudCoil's intelligent builder system automatically detects which style you're using and provides appropriate IDE support:

```python
from cloudcoil.models.kyverno.v1 import ClusterPolicy
from cloudcoil import apimachinery

# Mixing styles lets you choose the best approach for each part
with ClusterPolicy.new() as policy:
    # Direct object initialization with full type checking
    policy.metadata(apimachinery.ObjectMeta(
        name="require-labels",
        labels={"app": "kyverno"}
    ))
    
    with policy.spec() as spec:
        # Fluent style for rules
        spec.rules([
            lambda r: r
            .name("require-team-label")
            .match(lambda m: m
                .resources(lambda res: res
                    .kinds(["Deployment", "StatefulSet"])
                )
            )
            # Context manager style for validate
            .validate(lambda v: v
                .message("The label 'team' is required")
                .pattern({
                    "metadata": {
                        "labels": {
                            "team": "*"
                        }
                    }
                })
            )
        ])

final_policy = policy.build()
```

This flexibility allows you to:
- 🔀 Choose the most appropriate style for each part of your configuration
- 📖 Maximize readability for both simple and complex structures
- 🎨 Format your code according to your team's preferences
- 🧠 Get full IDE support with automatic style detection
- ✨ Enjoy rich autocomplete in all styles
- ⚡ Benefit from type checking across mixed styles
- 🎯 Receive immediate feedback on type errors
- 🔍 See documentation for all fields regardless of style

## 📚 Documentation

For complete documentation, visit [cloudcoil.github.io/cloudcoil](https://cloudcoil.github.io/cloudcoil)

## 📜 License

Apache License, Version 2.0 - see [LICENSE](LICENSE)
