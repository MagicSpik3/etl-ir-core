import pytest
from src.ir.types import OpType, DataType

def test_critical_op_types_exist():
    """Ensure the OpTypes required by the compiler are present."""
    # Check for the legacy keys used in your current pipeline
    assert OpType.LOAD_CSV == "load_csv"
    assert OpType.COMPUTE_COLUMNS == "compute_columns"
    assert OpType.FILTER_ROWS == "filter_rows"
    assert OpType.MATERIALIZE == "materialize"
    assert OpType.SAVE_BINARY == "save_binary"

def test_data_types_exist():
    """Ensure standard data types are defined."""
    assert DataType.INTEGER == "integer"
    assert DataType.STRING == "string"
    assert DataType.UNKNOWN == "unknown"