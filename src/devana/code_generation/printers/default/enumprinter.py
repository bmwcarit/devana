from devana.code_generation.printers.icodeprinter import ICodePrinter
from devana.syntax_abstraction.enuminfo import EnumInfo
from devana.syntax_abstraction.typeexpression import BasicType
from devana.syntax_abstraction.typeexpression import TypeExpression
from devana.code_generation.printers.dispatcherinjectable import DispatcherInjectable
from devana.code_generation.printers.configuration import PrinterConfiguration
from devana.code_generation.printers.formatter import Formatter
from typing import Optional


class EnumPrinter(ICodePrinter, DispatcherInjectable):

    def print(self, source: EnumInfo, config: Optional[PrinterConfiguration] = None, context: Optional = None) -> str:
        if config is None:
            config = PrinterConfiguration()
        formatter = Formatter(config)
        if type(context) is TypeExpression:
            return source.name
        formatter.line = "enum"
        if source.is_scoped:
            formatter.line += f" {source.prefix}"
        formatter.line += f" {source.name}"
        if source.numeric_type != BasicType.INT and source.numeric_type != BasicType.U_INT:  # OS standard types
            formatter.line += f": {self.printer_dispatcher.print(source.numeric_type, config, source)}"
        if source.is_declaration:
            formatter.line += ";"
            formatter.next_line()

            return formatter.text
        formatter.next_line()
        formatter.line = "{"
        formatter.next_line()
        formatter.indent.count += 1
        for v in source.values:
            formatter.line = v.name + ("" if v.is_default else f" = {v.value}")
            if v != source.values[-1]:
                formatter.line += ","
            formatter.next_line()
        formatter.indent.count -= 1
        formatter.line = "};"
        formatter.next_line()
        return formatter.text


class EnumAsTypePrinter(ICodePrinter, DispatcherInjectable):

    def print(self, source: EnumInfo, _1=None, _2=None) -> str:
        return source.name
