from typing import List

from dotenv import load_dotenv
from unstructured.documents.elements import Element
from unstructured.partition.auto import partition

from megaparse.core.parser import MegaParser
from megaparse.core.parser.type import StrategyEnum


class UnstructuredParser(MegaParser):
    load_dotenv()

    def __init__(self, strategy=StrategyEnum.AUTO, **kwargs):
        self.strategy = strategy

    async def convert(self, file_path, **kwargs) -> List[Element]:
        print("Converting file to elements using UnstructuredParser...")
        elements = partition(
            filename=str(file_path),
            strategy=self.strategy,
            skip_infer_table_types=[],
        )
        return elements
