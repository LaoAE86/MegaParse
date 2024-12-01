from abc import ABC, abstractmethod
from pathlib import Path
from typing import IO, List

from unstructured.documents.elements import Element


class BaseParser(ABC):
    """Mother Class for all the parsers [Unstructured, LlamaParse, MegaParseVision]"""

    @abstractmethod
    async def convert(
        self,
        file_path: str | Path | None = None,
        file: IO[bytes] | None = None,
        **kwargs,
    ) -> List[Element] | str:
        """
        Convert the given file to the unstructured format.

        Args:
            file_path (str | Path): The path to the file to be converted.
            **kwargs: Additional keyword arguments for the conversion process.

        Returns:
            str: The result of the conversion process.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclasses should implement this method")
