# Auto generated from softinfo.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-27T15:14:40
# Schema: softwareO
#
# id: https://w3id.org/linkml/examples/softwareO
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DOI = CurieNamespace('DOI', 'https://doi.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MLS = CurieNamespace('mls', 'http://www.w3.org/ns/mls')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SOFTINFO = CurieNamespace('softinfo', 'https://w3id.org/linkml/examples/softinfo')
DEFAULT_ = SOFTINFO


# Types

# Class references
class SoftwareId(extended_str):
    pass


@dataclass
class Software(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MLS.Software
    class_class_curie: ClassVar[str] = "mls:Software"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = SOFTINFO.Software

    id: Union[str, SoftwareId] = None
    title: str = None
    aliases: Optional[Union[str, List[str]]] = empty_list()
    function: Optional[str] = None
    dependencies: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        if self.function is not None and not isinstance(self.function, str):
            self.function = str(self.function)

        if self.dependencies is not None and not isinstance(self.dependencies, int):
            self.dependencies = int(self.dependencies)

        super().__post_init__(**kwargs)


@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SOFTINFO.Container
    class_class_curie: ClassVar[str] = "softinfo:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = SOFTINFO.Container

    softwares: Optional[Union[Dict[Union[str, SoftwareId], Union[dict, Software]], List[Union[dict, Software]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="softwares", slot_type=Software, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.software__id = Slot(uri=SOFTINFO.id, name="software__id", curie=SOFTINFO.curie('id'),
                   model_uri=SOFTINFO.software__id, domain=None, range=URIRef)

slots.software__title = Slot(uri=SCHEMA.name, name="software__title", curie=SCHEMA.curie('name'),
                   model_uri=SOFTINFO.software__title, domain=None, range=str)

slots.software__aliases = Slot(uri=SOFTINFO.aliases, name="software__aliases", curie=SOFTINFO.curie('aliases'),
                   model_uri=SOFTINFO.software__aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.software__function = Slot(uri=SOFTINFO.function, name="software__function", curie=SOFTINFO.curie('function'),
                   model_uri=SOFTINFO.software__function, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\d\(\)\-]+$'))

slots.software__dependencies = Slot(uri=SOFTINFO.dependencies, name="software__dependencies", curie=SOFTINFO.curie('dependencies'),
                   model_uri=SOFTINFO.software__dependencies, domain=None, range=Optional[int])

slots.container__softwares = Slot(uri=SOFTINFO.softwares, name="container__softwares", curie=SOFTINFO.curie('softwares'),
                   model_uri=SOFTINFO.container__softwares, domain=None, range=Optional[Union[Dict[Union[str, SoftwareId], Union[dict, Software]], List[Union[dict, Software]]]])
