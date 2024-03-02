from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Coordinates(_message.Message):
    __slots__ = ("coordinate",)
    COORDINATE_FIELD_NUMBER: _ClassVar[int]
    coordinate: _containers.RepeatedCompositeFieldContainer[Coordinate]
    def __init__(self, coordinate: _Optional[_Iterable[_Union[Coordinate, _Mapping]]] = ...) -> None: ...

class Coordinate(_message.Message):
    __slots__ = ("lat", "lng", "pickup_identifier")
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    PICKUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    lat: float
    lng: float
    pickup_identifier: int
    def __init__(self, lat: _Optional[float] = ..., lng: _Optional[float] = ..., pickup_identifier: _Optional[int] = ...) -> None: ...

class Centroid(_message.Message):
    __slots__ = ("location_name", "lat", "lng")
    LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    location_name: str
    lat: float
    lng: float
    def __init__(self, location_name: _Optional[str] = ..., lat: _Optional[float] = ..., lng: _Optional[float] = ...) -> None: ...

class Cluster(_message.Message):
    __slots__ = ("centroid", "points", "max_radius", "density_ratio")
    CENTROID_FIELD_NUMBER: _ClassVar[int]
    POINTS_FIELD_NUMBER: _ClassVar[int]
    MAX_RADIUS_FIELD_NUMBER: _ClassVar[int]
    DENSITY_RATIO_FIELD_NUMBER: _ClassVar[int]
    centroid: Centroid
    points: _containers.RepeatedScalarFieldContainer[str]
    max_radius: float
    density_ratio: float
    def __init__(self, centroid: _Optional[_Union[Centroid, _Mapping]] = ..., points: _Optional[_Iterable[str]] = ..., max_radius: _Optional[float] = ..., density_ratio: _Optional[float] = ...) -> None: ...

class ClusterList(_message.Message):
    __slots__ = ("cluster",)
    CLUSTER_FIELD_NUMBER: _ClassVar[int]
    cluster: _containers.RepeatedCompositeFieldContainer[Cluster]
    def __init__(self, cluster: _Optional[_Iterable[_Union[Cluster, _Mapping]]] = ...) -> None: ...
