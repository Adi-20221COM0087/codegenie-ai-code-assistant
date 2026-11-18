
import ast


def analyze_python_code(code):
    """
    Detect Python syntax errors and simple
    function argument mismatches without
    executing the user's code.
    """

    errors = []

    try:
        tree = ast.parse(code)

    except SyntaxError as error:
        return [
            f"SyntaxError on line {error.lineno}: "
            f"{error.msg}"
        ]

    functions = {}

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions[node.name] = node

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue

        if not isinstance(node.func, ast.Name):
            continue

        name = node.func.id

        if name not in functions:
            continue

        function = functions[name]

        # Skip calls involving *args or **kwargs,
        # which need more advanced analysis.
        if any(isinstance(arg, ast.Starred) for arg in node.args):
            continue

        if any(keyword.arg is None for keyword in node.keywords):
            continue

        params = function.args

        # This initial checker handles ordinary
        # positional-or-keyword parameters only.
        if (
            params.posonlyargs
            or params.kwonlyargs
            or params.vararg
            or params.kwarg
        ):
            continue

        parameter_names = [arg.arg for arg in params.args]

        defaults_count = len(params.defaults)

        required_count = len(parameter_names) - defaults_count

        positional_count = len(node.args)

        keyword_names = [
            keyword.arg for keyword in node.keywords
        ]

        if len(keyword_names) != len(set(keyword_names)):
            errors.append(
                f"Line {node.lineno}: Duplicate keyword argument."
            )
            continue

        if any(name not in parameter_names for name in keyword_names):
            continue

        if positional_count > len(parameter_names):
            errors.append(
                f"Line {node.lineno}: {name}() receives too many "
                f"positional arguments."
            )
            continue

        positional_params = set(
            parameter_names[:positional_count]
        )

        if positional_params.intersection(keyword_names):
            errors.append(
                f"Line {node.lineno}: {name}() receives "
                f"multiple values for an argument."
            )
            continue

        supplied = positional_count + len(keyword_names)

        if supplied < required_count:
            errors.append(
                f"Line {node.lineno}: {name}() is missing "
                f"required arguments. Expected at least "
                f"{required_count}, received {supplied}."
            )
            continue

        required_names = set(
            parameter_names[:required_count]
        )

        provided_names = positional_params.union(keyword_names)

        missing_names = required_names - provided_names

        if missing_names:
            errors.append(
                f"Line {node.lineno}: {name}() is missing "
                f"required argument(s): "
                f"{', '.join(sorted(missing_names))}."
            )

    return errors
