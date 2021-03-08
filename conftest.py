import pytest

from src.fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application("D:\\TOOLS\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

