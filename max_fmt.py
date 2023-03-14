import autopep8
import isort
from IPython.core.magic import register_cell_magic
from yapf.yapflib.yapf_api import FormatCode


@register_cell_magic
def max_fmt(line, cell):
    """
    My formatter cell magic comannd.
    Please install autopep8, isort and yapf before using this magic command.
    !pip install autopep8 isort yapf
    """

    ret = isort.code(cell)
    ret = autopep8.fix_code(ret)
    print(FormatCode(ret, style_config='pep8')[0])
