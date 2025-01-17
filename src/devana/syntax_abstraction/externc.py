from devana.syntax_abstraction.organizers.codecontainer import CodeContainer
from typing import Optional, List
from clang import cindex
from devana.syntax_abstraction.functioninfo import FunctionInfo
from devana.utility.errors import ParserError
from devana.utility.lazy import lazy_invoke
from devana.syntax_abstraction.organizers.lexicon import Lexicon


class ExternC(CodeContainer):
    """"Object representation of current usage of extern C set of functions. It may contain one or more functions."""

    def __init__(self, cursor: Optional[cindex.Cursor] = None, parent: Optional[CodeContainer] = None):
        super().__init__(cursor, parent)
        if cursor is not None:
            if self._cursor.kind != cindex.CursorKind.UNEXPOSED_DECL:
                raise ParserError("It is not a valid type cursor.")
            if len(list(self._cursor.get_children())) <= 0:
                raise ParserError("It is not a valid type cursor.")
            for children in self._cursor.get_children():
                if children.kind != cindex.CursorKind.FUNCTION_DECL:
                    raise ParserError("It is not a valid type cursor. ExternC allow only functions content.")
        self._name = 'extern "C"'
        self._namespace = None
        self._lexicon = Lexicon.create(self)

    @property
    @lazy_invoke
    def name(self) -> str:
        self._name = self._cursor.displayname
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def lexicon(self) -> Lexicon:
        return self._lexicon

    @lexicon.setter
    def lexicon(self, value):
        self._lexicon = value

    def _create_content(self) -> List[any]:
        types = [FunctionInfo]
        content = []
        for children in self._cursor.get_children():
            for t in types:
                el = t(children, self)
                content.append(el)
                break
        return content
