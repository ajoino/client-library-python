from __future__ import annotations
import re
from dataclasses import dataclass
from typing import Union, List, Callable


def handle_requirements(requirement_list: Union[List[str], str]) -> List[str]:
    """
        Uppercases single string and puts it in a list,
        or uppercases strings in a list
    """
    # TODO: This function has a terrible name, then name should be more specific than it is
    if isinstance(requirement_list, str):
        return [requirement_list.upper()]
    else:
        return [requirement.upper() for requirement in requirement_list]


def to_camel_case(variable_name: str) -> str:
    """ Turns snake_case variable name into camelCase """
    split_name = variable_name.split('_')
    if split_name[0] == '':
        split_name[1] = '_' + split_name[1]

    trailing_underscore = '_' if split_name[-1] == '' else ''

    return split_name[0] + \
           ''.join([split.capitalize() for split in split_name[1:]]) + \
           trailing_underscore


def to_snake_case(variable_name: str) -> str:
    """ Turns camelCase variable name into snake_case """
    split_camel = re.findall(r'[A-Z][a-z0-9]*|[a-z0-9]+', variable_name)
    initial_underscore = '_' if variable_name.startswith('_') else ''
    trailing_underscore = '_' if variable_name.endswith('_') else ''

    return initial_underscore + \
           '_'.join([camel.lower() for camel in split_camel]) + \
           trailing_underscore


@dataclass
class ServiceInterface:
    protocol: str
    secure: str
    payload: str

    @classmethod
    def from_str(cls, interface_str: str) -> ServiceInterface:
        return cls(*interface_str.split('-'))

    @property
    def dto(self) -> str:
        return '-'.join(vars(self).values())

    def __eq__(self, other: Union[ServiceInterface, str]) -> bool:
        if isinstance(other, str):
            other_si = ServiceInterface.from_str(other)
        elif isinstance(other, ServiceInterface):
            other_si = other
        else:
            raise ValueError('Other must be of type ServiceInterface or str')

        return self.protocol == other_si.protocol and \
               self.secure == other_si.secure and \
               self.payload == other_si.payload

if __name__ == "__main__":
    pass