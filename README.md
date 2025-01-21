# cloudcoil-models-kyverno

Versioned Kyverno models for cloudcoil.

## 🔧 Installation

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

## 📚 Documentation

For complete documentation, visit [cloudcoil.github.io/cloudcoil](https://cloudcoil.github.io/cloudcoil)

## 📜 License

Apache License, Version 2.0 - see [LICENSE](LICENSE)
