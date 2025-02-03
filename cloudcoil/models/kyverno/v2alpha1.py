# Generated by cloudcoil-model-codegen v0.4.7
# DO NOT EDIT

from __future__ import annotations

from datetime import datetime
from typing import (
    Annotated,
    Any,
    Callable,
    List,
    Literal,
    Optional,
    Type,
    overload,
)

from pydantic import Field

from cloudcoil import apimachinery
from cloudcoil.pydantic import (
    BaseModel,
    BaseModelBuilder,
    BuilderContextBase,
    GenericListBuilder,
    ListBuilderContext,
    Never,
    Self,
)
from cloudcoil.resources import Resource


class Datum(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Datum"]:
            return Datum

        def build(self) -> "Datum":
            return Datum(**self._attrs)

        def key(self, value: str, /) -> Self:
            """
            Key is a unique identifier for the data value
            """
            return self._set("key", value)

        def value(self, value: Any, /) -> Self:
            """
            Value is the data value
            """
            return self._set("value", value)

    class BuilderContext(BuilderContextBase["Datum.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Datum.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Datum."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Datum", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Datum.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    key: str
    """
    Key is a unique identifier for the data value
    """
    value: Any
    """
    Value is the data value
    """


class Service(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Service"]:
            return Service

        def build(self) -> "Service":
            return Service(**self._attrs)

        def ca_bundle(self, value: Optional[str], /) -> Self:
            """
            CABundle is a PEM encoded CA bundle which will be used to validate
            the server certificate.
            """
            return self._set("ca_bundle", value)

        def url(self, value: str, /) -> Self:
            """
            URL is the JSON web service URL. A typical form is
            `https://{service}.{namespace}:{port}/{path}`.
            """
            return self._set("url", value)

    class BuilderContext(BuilderContextBase["Service.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Service.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Service."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Service", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Service.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    ca_bundle: Annotated[Optional[str], Field(alias="caBundle")] = None
    """
    CABundle is a PEM encoded CA bundle which will be used to validate
    the server certificate.
    """
    url: str
    """
    URL is the JSON web service URL. A typical form is
    `https://{service}.{namespace}:{port}/{path}`.
    """


class ApiCall(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["ApiCall"]:
            return ApiCall

        def build(self) -> "ApiCall":
            return ApiCall(**self._attrs)

        @overload
        def data(self, value_or_callback: List[Datum], /) -> "ApiCall.Builder": ...

        @overload
        def data(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[Datum, Datum.Builder]],
                GenericListBuilder[Datum, Datum.Builder] | List[Datum],
            ],
            /,
        ) -> "ApiCall.Builder": ...

        @overload
        def data(self, value_or_callback: Never = ...) -> ListBuilderContext[Datum.Builder]: ...

        def data(self, value_or_callback=None, /):
            """
            The data object specifies the POST data sent to the server.
            Only applicable when the method field is set to POST.
            """
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[Datum.Builder]()
                context._parent_builder = self
                context._field_name = "data"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Datum.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("data", value)

        def method(self, value: Optional[Literal["GET", "POST"]], /) -> Self:
            """
            Method is the HTTP request type (GET or POST).
            """
            return self._set("method", value)

        def refresh_interval(self, value: Optional[str], /) -> Self:
            """
            RefreshInterval defines the interval in duration at which to poll the APICall.
            The duration is a sequence of decimal numbers, each with optional fraction and a unit suffix,
            such as "300ms", "1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".
            """
            return self._set("refresh_interval", value)

        @overload
        def service(self, value_or_callback: Optional[Service], /) -> "ApiCall.Builder": ...

        @overload
        def service(
            self,
            value_or_callback: Callable[[Service.Builder], Service.Builder | Service],
            /,
        ) -> "ApiCall.Builder": ...

        @overload
        def service(self, value_or_callback: Never = ...) -> "Service.BuilderContext": ...

        def service(self, value_or_callback=None, /):
            """
            Service is an API call to a JSON web service.
            This is used for non-Kubernetes API server calls.
            It's mutually exclusive with the URLPath field.
            """
            if self._in_context and value_or_callback is None:
                context = Service.BuilderContext()
                context._parent_builder = self
                context._field_name = "service"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Service.builder())
                if isinstance(output, Service.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("service", value)

        def url_path(self, value: Optional[str], /) -> Self:
            """
            URLPath is the URL path to be used in the HTTP GET or POST request to the
            Kubernetes API server (e.g. "/api/v1/namespaces" or  "/apis/apps/v1/deployments").
            The format required is the same format used by the `kubectl get --raw` command.
            See https://kyverno.io/docs/writing-policies/external-data-sources/#variables-from-kubernetes-api-server-calls
            for details.
            It's mutually exclusive with the Service field.
            """
            return self._set("url_path", value)

    class BuilderContext(BuilderContextBase["ApiCall.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = ApiCall.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for ApiCall."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["ApiCall", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use ApiCall.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    data: Optional[List[Datum]] = None
    """
    The data object specifies the POST data sent to the server.
    Only applicable when the method field is set to POST.
    """
    method: Optional[Literal["GET", "POST"]] = "GET"
    """
    Method is the HTTP request type (GET or POST).
    """
    refresh_interval: Annotated[Optional[str], Field(alias="refreshInterval")] = "10m"
    """
    RefreshInterval defines the interval in duration at which to poll the APICall.
    The duration is a sequence of decimal numbers, each with optional fraction and a unit suffix,
    such as "300ms", "1.5h" or "2h45m". Valid time units are "ns", "us" (or "µs"), "ms", "s", "m", "h".
    """
    service: Optional[Service] = None
    """
    Service is an API call to a JSON web service.
    This is used for non-Kubernetes API server calls.
    It's mutually exclusive with the URLPath field.
    """
    url_path: Annotated[Optional[str], Field(alias="urlPath")] = None
    """
    URLPath is the URL path to be used in the HTTP GET or POST request to the
    Kubernetes API server (e.g. "/api/v1/namespaces" or  "/apis/apps/v1/deployments").
    The format required is the same format used by the `kubectl get --raw` command.
    See https://kyverno.io/docs/writing-policies/external-data-sources/#variables-from-kubernetes-api-server-calls
    for details.
    It's mutually exclusive with the Service field.
    """


class KubernetesResource(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["KubernetesResource"]:
            return KubernetesResource

        def build(self) -> "KubernetesResource":
            return KubernetesResource(**self._attrs)

        def group(self, value: Optional[str], /) -> Self:
            """
            Group defines the group of the resource.
            """
            return self._set("group", value)

        def namespace(self, value: Optional[str], /) -> Self:
            """
            Namespace defines the namespace of the resource. Leave empty for cluster scoped resources.
            If left empty for namespaced resources, all resources from all namespaces will be cached.
            """
            return self._set("namespace", value)

        def resource(self, value: Optional[str], /) -> Self:
            """
            Resource defines the type of the resource.
            Requires the pluralized form of the resource kind in lowercase. (Ex., "deployments")
            """
            return self._set("resource", value)

        def version(self, value: Optional[str], /) -> Self:
            """
            Version defines the version of the resource.
            """
            return self._set("version", value)

    class BuilderContext(BuilderContextBase["KubernetesResource.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = KubernetesResource.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for KubernetesResource."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["KubernetesResource", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use KubernetesResource.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    group: Optional[str] = None
    """
    Group defines the group of the resource.
    """
    namespace: Optional[str] = None
    """
    Namespace defines the namespace of the resource. Leave empty for cluster scoped resources.
    If left empty for namespaced resources, all resources from all namespaces will be cached.
    """
    resource: Optional[str] = None
    """
    Resource defines the type of the resource.
    Requires the pluralized form of the resource kind in lowercase. (Ex., "deployments")
    """
    version: Optional[str] = None
    """
    Version defines the version of the resource.
    """


class GlobalContextEntrySpec(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["GlobalContextEntrySpec"]:
            return GlobalContextEntrySpec

        def build(self) -> "GlobalContextEntrySpec":
            return GlobalContextEntrySpec(**self._attrs)

        @overload
        def api_call(
            self, value_or_callback: Optional[ApiCall], /
        ) -> "GlobalContextEntrySpec.Builder": ...

        @overload
        def api_call(
            self,
            value_or_callback: Callable[[ApiCall.Builder], ApiCall.Builder | ApiCall],
            /,
        ) -> "GlobalContextEntrySpec.Builder": ...

        @overload
        def api_call(self, value_or_callback: Never = ...) -> "ApiCall.BuilderContext": ...

        def api_call(self, value_or_callback=None, /):
            """
            Stores results from an API call which will be cached.
            Mutually exclusive with KubernetesResource.
            This can be used to make calls to external (non-Kubernetes API server) services.
            It can also be used to make calls to the Kubernetes API server in such cases:
            1. A POST is needed to create a resource.
            2. Finer-grained control is needed. Example: To restrict the number of resources cached.
            """
            if self._in_context and value_or_callback is None:
                context = ApiCall.BuilderContext()
                context._parent_builder = self
                context._field_name = "api_call"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(ApiCall.builder())
                if isinstance(output, ApiCall.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("api_call", value)

        @overload
        def kubernetes_resource(
            self, value_or_callback: Optional[KubernetesResource], /
        ) -> "GlobalContextEntrySpec.Builder": ...

        @overload
        def kubernetes_resource(
            self,
            value_or_callback: Callable[
                [KubernetesResource.Builder],
                KubernetesResource.Builder | KubernetesResource,
            ],
            /,
        ) -> "GlobalContextEntrySpec.Builder": ...

        @overload
        def kubernetes_resource(
            self, value_or_callback: Never = ...
        ) -> "KubernetesResource.BuilderContext": ...

        def kubernetes_resource(self, value_or_callback=None, /):
            """
            Stores a list of Kubernetes resources which will be cached.
            Mutually exclusive with APICall.
            """
            if self._in_context and value_or_callback is None:
                context = KubernetesResource.BuilderContext()
                context._parent_builder = self
                context._field_name = "kubernetes_resource"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(KubernetesResource.builder())
                if isinstance(output, KubernetesResource.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("kubernetes_resource", value)

    class BuilderContext(BuilderContextBase["GlobalContextEntrySpec.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = GlobalContextEntrySpec.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for GlobalContextEntrySpec."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["GlobalContextEntrySpec", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use GlobalContextEntrySpec.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_call: Annotated[Optional[ApiCall], Field(alias="apiCall")] = None
    """
    Stores results from an API call which will be cached.
    Mutually exclusive with KubernetesResource.
    This can be used to make calls to external (non-Kubernetes API server) services.
    It can also be used to make calls to the Kubernetes API server in such cases:
    1. A POST is needed to create a resource.
    2. Finer-grained control is needed. Example: To restrict the number of resources cached.
    """
    kubernetes_resource: Annotated[
        Optional[KubernetesResource], Field(alias="kubernetesResource")
    ] = None
    """
    Stores a list of Kubernetes resources which will be cached.
    Mutually exclusive with APICall.
    """


class Condition(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["Condition"]:
            return Condition

        def build(self) -> "Condition":
            return Condition(**self._attrs)

        def last_transition_time(self, value: datetime, /) -> Self:
            """
            lastTransitionTime is the last time the condition transitioned from one status to another.
            This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
            """
            return self._set("last_transition_time", value)

        def message(self, value: str, /) -> Self:
            """
            message is a human readable message indicating details about the transition.
            This may be an empty string.
            """
            return self._set("message", value)

        def observed_generation(self, value: Optional[int], /) -> Self:
            """
            observedGeneration represents the .metadata.generation that the condition was set based upon.
            For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
            with respect to the current state of the instance.
            """
            return self._set("observed_generation", value)

        def reason(self, value: str, /) -> Self:
            """
            reason contains a programmatic identifier indicating the reason for the condition's last transition.
            Producers of specific condition types may define expected values and meanings for this field,
            and whether the values are considered a guaranteed API.
            The value should be a CamelCase string.
            This field may not be empty.
            """
            return self._set("reason", value)

        def status(self, value: Literal["True", "False", "Unknown"], /) -> Self:
            """
            status of the condition, one of True, False, Unknown.
            """
            return self._set("status", value)

        def type(self, value: str, /) -> Self:
            """
            type of condition in CamelCase or in foo.example.com/CamelCase.
            ---
            Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be
            useful (see .node.status.conditions), the ability to deconflict is important.
            The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)
            """
            return self._set("type", value)

    class BuilderContext(BuilderContextBase["Condition.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = Condition.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for Condition."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["Condition", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use Condition.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    last_transition_time: Annotated[datetime, Field(alias="lastTransitionTime")]
    """
    lastTransitionTime is the last time the condition transitioned from one status to another.
    This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.
    """
    message: Annotated[str, Field(max_length=32768)]
    """
    message is a human readable message indicating details about the transition.
    This may be an empty string.
    """
    observed_generation: Annotated[Optional[int], Field(alias="observedGeneration", ge=0)] = None
    """
    observedGeneration represents the .metadata.generation that the condition was set based upon.
    For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
    with respect to the current state of the instance.
    """
    reason: Annotated[
        str,
        Field(
            max_length=1024,
            min_length=1,
            pattern="^[A-Za-z]([A-Za-z0-9_,:]*[A-Za-z0-9_])?$",
        ),
    ]
    """
    reason contains a programmatic identifier indicating the reason for the condition's last transition.
    Producers of specific condition types may define expected values and meanings for this field,
    and whether the values are considered a guaranteed API.
    The value should be a CamelCase string.
    This field may not be empty.
    """
    status: Literal["True", "False", "Unknown"]
    """
    status of the condition, one of True, False, Unknown.
    """
    type: Annotated[
        str,
        Field(
            max_length=316,
            pattern="^([a-z0-9]([-a-z0-9]*[a-z0-9])?(\\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*/)?(([A-Za-z0-9][-A-Za-z0-9_.]*)?[A-Za-z0-9])$",
        ),
    ]
    """
    type of condition in CamelCase or in foo.example.com/CamelCase.
    ---
    Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be
    useful (see .node.status.conditions), the ability to deconflict is important.
    The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)
    """


class GlobalContextEntryStatus(BaseModel):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["GlobalContextEntryStatus"]:
            return GlobalContextEntryStatus

        def build(self) -> "GlobalContextEntryStatus":
            return GlobalContextEntryStatus(**self._attrs)

        @overload
        def conditions(
            self, value_or_callback: List[Condition], /
        ) -> "GlobalContextEntryStatus.Builder": ...

        @overload
        def conditions(
            self,
            value_or_callback: Callable[
                [GenericListBuilder[Condition, Condition.Builder]],
                GenericListBuilder[Condition, Condition.Builder] | List[Condition],
            ],
            /,
        ) -> "GlobalContextEntryStatus.Builder": ...

        @overload
        def conditions(
            self, value_or_callback: Never = ...
        ) -> ListBuilderContext[Condition.Builder]: ...

        def conditions(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = ListBuilderContext[Condition.Builder]()
                context._parent_builder = self
                context._field_name = "conditions"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(Condition.list_builder())
                if isinstance(output, GenericListBuilder):
                    value = output.build()
                else:
                    value = output
            return self._set("conditions", value)

        def last_refresh_time(self, value: Optional[datetime], /) -> Self:
            """
            Indicates the time when the globalcontextentry was last refreshed successfully for the API Call
            """
            return self._set("last_refresh_time", value)

        def ready(self, value: bool, /) -> Self:
            """
            Deprecated in favor of Conditions
            """
            return self._set("ready", value)

    class BuilderContext(BuilderContextBase["GlobalContextEntryStatus.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = GlobalContextEntryStatus.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for GlobalContextEntryStatus."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["GlobalContextEntryStatus", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use GlobalContextEntryStatus.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    conditions: Optional[List[Condition]] = None
    last_refresh_time: Annotated[Optional[datetime], Field(alias="lastRefreshTime")] = None
    """
    Indicates the time when the globalcontextentry was last refreshed successfully for the API Call
    """
    ready: bool
    """
    Deprecated in favor of Conditions
    """


class GlobalContextEntry(Resource):
    class Builder(BaseModelBuilder):
        @property
        def cls(self) -> Type["GlobalContextEntry"]:
            return GlobalContextEntry

        def build(self) -> "GlobalContextEntry":
            return GlobalContextEntry(**self._attrs)

        def api_version(self, value: Optional[Literal["kyverno.io/v2alpha1"]], /) -> Self:
            """
            APIVersion defines the versioned schema of this representation of an object.
            Servers should convert recognized schemas to the latest internal value, and
            may reject unrecognized values.
            More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
            """
            return self._set("api_version", value)

        def kind(self, value: Optional[Literal["GlobalContextEntry"]], /) -> Self:
            """
            Kind is a string value representing the REST resource this object represents.
            Servers may infer this from the endpoint the client submits requests to.
            Cannot be updated.
            In CamelCase.
            More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
            """
            return self._set("kind", value)

        @overload
        def metadata(
            self, value_or_callback: Optional[apimachinery.ObjectMeta], /
        ) -> "GlobalContextEntry.Builder": ...

        @overload
        def metadata(
            self,
            value_or_callback: Callable[
                [apimachinery.ObjectMeta.Builder],
                apimachinery.ObjectMeta.Builder | apimachinery.ObjectMeta,
            ],
            /,
        ) -> "GlobalContextEntry.Builder": ...

        @overload
        def metadata(
            self, value_or_callback: Never = ...
        ) -> "apimachinery.ObjectMeta.BuilderContext": ...

        def metadata(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = apimachinery.ObjectMeta.BuilderContext()
                context._parent_builder = self
                context._field_name = "metadata"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(apimachinery.ObjectMeta.builder())
                if isinstance(output, apimachinery.ObjectMeta.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("metadata", value)

        @overload
        def spec(
            self, value_or_callback: GlobalContextEntrySpec, /
        ) -> "GlobalContextEntry.Builder": ...

        @overload
        def spec(
            self,
            value_or_callback: Callable[
                [GlobalContextEntrySpec.Builder],
                GlobalContextEntrySpec.Builder | GlobalContextEntrySpec,
            ],
            /,
        ) -> "GlobalContextEntry.Builder": ...

        @overload
        def spec(
            self, value_or_callback: Never = ...
        ) -> "GlobalContextEntrySpec.BuilderContext": ...

        def spec(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = GlobalContextEntrySpec.BuilderContext()
                context._parent_builder = self
                context._field_name = "spec"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(GlobalContextEntrySpec.builder())
                if isinstance(output, GlobalContextEntrySpec.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("spec", value)

        @overload
        def status(
            self, value_or_callback: Optional[GlobalContextEntryStatus], /
        ) -> "GlobalContextEntry.Builder": ...

        @overload
        def status(
            self,
            value_or_callback: Callable[
                [GlobalContextEntryStatus.Builder],
                GlobalContextEntryStatus.Builder | GlobalContextEntryStatus,
            ],
            /,
        ) -> "GlobalContextEntry.Builder": ...

        @overload
        def status(
            self, value_or_callback: Never = ...
        ) -> "GlobalContextEntryStatus.BuilderContext": ...

        def status(self, value_or_callback=None, /):
            if self._in_context and value_or_callback is None:
                context = GlobalContextEntryStatus.BuilderContext()
                context._parent_builder = self
                context._field_name = "status"
                return context

            value = value_or_callback
            if callable(value_or_callback):
                output = value_or_callback(GlobalContextEntryStatus.builder())
                if isinstance(output, GlobalContextEntryStatus.Builder):
                    value = output.build()
                else:
                    value = output
            return self._set("status", value)

    class BuilderContext(BuilderContextBase["GlobalContextEntry.Builder"]):
        def model_post_init(self, __context) -> None:
            self._builder = GlobalContextEntry.Builder()
            self._builder._in_context = True
            self._parent_builder = None
            self._field_name = None

    @classmethod
    def builder(cls) -> Builder:
        return cls.Builder()

    @classmethod
    def new(cls) -> BuilderContext:
        """Creates a new context manager builder for GlobalContextEntry."""
        return cls.BuilderContext()

    class ListBuilder(GenericListBuilder["GlobalContextEntry", Builder]):
        def __init__(self):
            raise NotImplementedError(
                "This class is not meant to be instantiated. Use GlobalContextEntry.list_builder() instead."
            )

    @classmethod
    def list_builder(cls) -> ListBuilder:
        return GenericListBuilder[cls, cls.Builder]()  # type: ignore

    api_version: Annotated[Optional[Literal["kyverno.io/v2alpha1"]], Field(alias="apiVersion")] = (
        "kyverno.io/v2alpha1"
    )
    """
    APIVersion defines the versioned schema of this representation of an object.
    Servers should convert recognized schemas to the latest internal value, and
    may reject unrecognized values.
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
    """
    kind: Optional[Literal["GlobalContextEntry"]] = "GlobalContextEntry"
    """
    Kind is a string value representing the REST resource this object represents.
    Servers may infer this from the endpoint the client submits requests to.
    Cannot be updated.
    In CamelCase.
    More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
    """
    metadata: Optional[apimachinery.ObjectMeta] = None
    spec: GlobalContextEntrySpec
    status: Optional[GlobalContextEntryStatus] = None
