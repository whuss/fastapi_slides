import schemathesis
from schemathesis.checks import ALL_CHECKS

from example.main import api

# Generates valid and also invalid data
schema = schemathesis.from_dict(
    api.openapi(),
    data_generation_methods=[
        schemathesis.DataGenerationMethod.positive,
        schemathesis.DataGenerationMethod.negative,
    ],
)


@schema.parametrize()
def test_schema_compliance(case):
    response = case.call_asgi(api)
    case.validate_response(response, checks=ALL_CHECKS)
