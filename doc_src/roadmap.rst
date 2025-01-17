Roadmap
==================================

Devana is still under development. Two main functional modules are planned: a parser and a code generator.
For now, parser is mostly done and basic functionality of the code generator is working.
Many additional functionalities, not assigned to these modules, are also missing.

Parser
-------
The main purpose of this part is to ensure correct translation of the C++17 headers code to python objects
representing types and declarations. Standard preprocessor is not supported: code is parsed after preprocessor
transformation.

If some parser functionality (in the context of C++ and headers) does not work in the current version of the
project and is not included in the list of future functionalities, then most likely it should be treated as a bug.

In addition to the properties listed below, the most important thing at the moment is to prepare tests for unsupported
language features to ensure that valid exceptions are thrown.

* **Parsing types and types traits**
    * Functions pointers: *medium priority*
    * Array: *medium priority*

* **Other code**
    * Using directive: *medium priority*
    * Auto keyword: *extreme low priority*
    * Decltype: *extreme low priority*
    * Function declaration as trailing-return-type: *extreme low priority*
    * Noexcept and throw function declaration: *medium priority*
    * Final class attribute: *extreme low priority*
    * C++ standard attributes: *medium priority*
    * GCC attributes: *medium priority*
    * Except destructor: *extreme low priority*
    * Comment in code: *low priority*
    * Headers guard: *medium priority*

* **Other**
    * Includes list as an alternative to relative paths: *low priority*
    * Prevent re-parsing unchanged files: *low priority*
    * Better exceptions: *medium priority*
    * Reducing memory usage: *medium priority*
    * Split syntax abstraction element representation from parsing: *low priority*

Code generator
--------------
Currently, core code generation functionality is working. Current work is focused on improving the convenience of
using code generation. The main goal is to be able to edit and represent C ++ headers using Python code representations
and to make it easy to generate implementations (as text based). Code generation is now the main focus of the project.

Each element present in the parser module should be available for editing and creation for generation purposes.

* **Code generator**
    * High level code generation rules as framework: *low priority*
    * Low level code generation rules as  in code directives: *medium priority*
    * Context aware preprocessor: *high priority*
    * Better way to create and modify source code (builder pattern etc.): *low priority*
    * Possibility to verify the correctness of manually created code: *medium priority*
    * New example/tutorial: *high priority*
    * Lexicon automatic update for code generation: *medium priority*

Utility
--------
Devana is young project, a wide range of minor elements needs to be refined.

* **Utility**
    * Speed up parsing code: *low priority*
    * More examples: *low priority*
    * Build-in preprocessor: *low priority*
    * Serialize code representation: *low priority*
    * Better documentation: *medium priority*