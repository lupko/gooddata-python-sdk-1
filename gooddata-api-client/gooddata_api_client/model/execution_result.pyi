# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gooddata_api_client import schemas  # noqa: F401


class ExecutionResult(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Contains the result of an AFM execution.
    """


    class MetaOapg:
        required = {
            "data",
            "dimensionHeaders",
            "paging",
            "grandTotals",
        }
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.DictSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class dimensionHeaders(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DimensionHeader']:
                        return DimensionHeader
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DimensionHeader'], typing.List['DimensionHeader']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dimensionHeaders':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DimensionHeader':
                    return super().__getitem__(i)
            
            
            class grandTotals(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ExecutionResultGrandTotal']:
                        return ExecutionResultGrandTotal
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ExecutionResultGrandTotal'], typing.List['ExecutionResultGrandTotal']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'grandTotals':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ExecutionResultGrandTotal':
                    return super().__getitem__(i)
        
            @staticmethod
            def paging() -> typing.Type['ExecutionResultPaging']:
                return ExecutionResultPaging
            __annotations__ = {
                "data": data,
                "dimensionHeaders": dimensionHeaders,
                "grandTotals": grandTotals,
                "paging": paging,
            }
    
    data: MetaOapg.properties.data
    dimensionHeaders: MetaOapg.properties.dimensionHeaders
    paging: 'ExecutionResultPaging'
    grandTotals: MetaOapg.properties.grandTotals
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dimensionHeaders"]) -> MetaOapg.properties.dimensionHeaders: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["grandTotals"]) -> MetaOapg.properties.grandTotals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paging"]) -> 'ExecutionResultPaging': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "dimensionHeaders", "grandTotals", "paging", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dimensionHeaders"]) -> MetaOapg.properties.dimensionHeaders: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["grandTotals"]) -> MetaOapg.properties.grandTotals: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paging"]) -> 'ExecutionResultPaging': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "dimensionHeaders", "grandTotals", "paging", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, ],
        dimensionHeaders: typing.Union[MetaOapg.properties.dimensionHeaders, list, tuple, ],
        paging: 'ExecutionResultPaging',
        grandTotals: typing.Union[MetaOapg.properties.grandTotals, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExecutionResult':
        return super().__new__(
            cls,
            *_args,
            data=data,
            dimensionHeaders=dimensionHeaders,
            paging=paging,
            grandTotals=grandTotals,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.dimension_header import DimensionHeader
from gooddata_api_client.model.execution_result_grand_total import ExecutionResultGrandTotal
from gooddata_api_client.model.execution_result_paging import ExecutionResultPaging