import pytest

from NAGATO import SNMP


@pytest.mark.flaky
def test_snmpwalk():

    snmp = SNMP()
    output = snmp.snmpwalk("demo.pysnmp.com", "1.3.6.1.2.1.1", 161, "public")

    print(output)
    assert output is not None
    assert isinstance(output, dict)


@pytest.mark.flaky
def test_get_request():

    snmp = SNMP()
    output = snmp.get_request("demo.pysnmp.com", "1.3.6.1.2.1.1.1.0", 161, "public")

    print(output)
    assert output is not None
    assert output == "#SNMP Agent on .NET Standard"
