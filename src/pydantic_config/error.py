class PydantiCliError(ValueError): ...


class CliArgError(PydantiCliError): ...


class CliValueError(PydantiCliError): ...


class DuplicateKeyError(PydantiCliError): ...