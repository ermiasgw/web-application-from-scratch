import typing

from collections import defaultdict

HeadersDict = typing.Dict[str, typing.List[str]]
HeadersGenerator = typing.Generator[typing.Tuple[str, str], None, None]


class Headers:
    """
    Represents a header with multiple vlues.

    Attributes:
    _headers (dictionaries of list): the header with list of values

    """

    def __init__(self) -> None:
        self._headers = defaultdict(list)

    def add(self, name: str, value: str) -> None:
        """

        used to add header values

        Attributes:
        name (str): name of the header
        value (str): value of the header

        Returns:
        None

        """
        self._headers[name.lower()].append(value)

    def get_all(self, name: str) -> typing.List[str]:
        """

        retrieves header by name

        Attributes:
        name (str): name of the header

        returns:
        array of values for the header

        """
        return self._headers[name.lower()]

    def get(
        self, name: str, default: typing.Optional[str] = None
    ) -> typing.Optional[str]:
        """

        retrieves the last value of a header.

        Attributes:
        name (str): name of the header
        default (str): the default value if the value of the header is none

        Returns:
        last value of the header or the default

        """
        try:
            return self.get_all(name)[-1]
        except IndexError:
            return default

    def __iter__(self) -> HeadersGenerator:
        """

        header name and value pair generator
        """
        for name, values in self._headers.items():
            for value in values:
                yield name, value
