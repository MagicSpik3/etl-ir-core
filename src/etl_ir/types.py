from enum import Enum

class DataType(str, Enum):
    STRING = "string"
    INTEGER = "integer"
    DECIMAL = "decimal" # Explicitly added decimal support
    DATE = "date"
    UNKNOWN = "unknown"

class OpType(str, Enum):
    # IO
    LOAD_CSV = "load_csv"
    SAVE_BINARY = "save_binary"
    
    # Logic (Renamed keys to match values)
    COMPUTE_COLUMNS = "compute_columns"  # <--- WAS "COMPUTE"
    FILTER_ROWS = "filter_rows"          # <--- WAS "FILTER"
    AGGREGATE = "aggregate"
    JOIN = "join"
    SORT = "sort"
    
    # Structural / Legacy
    GENERIC_TRANSFORM = "generic_transform" # <--- WAS "GENERIC"
    MATERIALIZE = "materialize"
    
    # Optimizations
    BATCH_COMPUTE = "batch_compute"