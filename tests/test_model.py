import pytest
from pydantic import ValidationError
from src.ir.model import Pipeline, Operation, Dataset
from src.ir.types import OpType, DataType

class TestDataset:
    def test_create_valid_dataset(self):
        ds = Dataset(
            id="ds_001", 
            source="file", 
            columns=[{"name": "revenue", "type": "integer"}]
        )
        assert ds.id == "ds_001"
        assert ds.columns[0].name == "revenue"

    def test_fails_without_required_fields(self):
        with pytest.raises(ValidationError):
            # Missing 'source'
            Dataset(id="ds_broken", columns=[])

class TestOperation:
    def test_create_valid_operation(self):
        op = Operation(
            id="op_1",
            type=OpType.LOAD_CSV,
            inputs=[],
            outputs=["ds_1"],
            parameters={"filename": "data.csv"}
        )
        assert op.type == OpType.LOAD_CSV

    def test_parameters_default_to_empty_dict(self):
        """Parameters should be optional and default to {}."""
        op = Operation(
            id="op_2",
            type=OpType.MATERIALIZE,
            inputs=["in"],
            outputs=["out"]
        )
        assert op.parameters == {}

class TestPipeline:
    def test_pipeline_serialization_roundtrip(self):
        """Can we dump to JSON and read it back? (Crucial for CLI)"""
        pipeline = Pipeline(
            datasets=[
                Dataset(id="d1", source="file", columns=[])
            ],
            operations=[
                Operation(id="op1", type=OpType.LOAD_CSV, inputs=[], outputs=["d1"])
            ]
        )
        
        # Serialize
        json_str = pipeline.model_dump_json()
        
        # Deserialize
        restored = Pipeline.model_validate_json(json_str)
        
        assert restored.operations[0].id == "op1"
        assert len(restored.datasets) == 1