import pytest

from aws_parameter_store_client.aws_parameter_store_client import (
    AwsParameterStoreClient,
    ParameterAlreadyExists,
    ParameterNotFound,
)


class TestPutParameter:
    def test_happy_flow(self):
        client = AwsParameterStoreClient()
        client.put_parameter(
            path="/test/aws/parameter/store/client",
            value="yesss!",
            do_overwrite=False,
        )

    def test_do_not_overwrite(self):
        client = AwsParameterStoreClient()
        with pytest.raises(ParameterAlreadyExists):
            client.put_parameter(
                path="/test/aws/parameter/store/client",
                value="nooo!",
                do_overwrite=False,
            )

    def test_overwrite(self):
        client = AwsParameterStoreClient()
        client.put_parameter(
            path="/test/aws/parameter/store/client",
            value="nooo!",
            do_overwrite=True,
        )


class TestGetParameter:
    def test_happy_flow(self):
        client = AwsParameterStoreClient()
        data = client.get_parameter(path="/test/aws/parameter/store/client")
        assert data == "nooo!"

    def test_does_not_exist(self):
        client = AwsParameterStoreClient()
        with pytest.raises(ParameterNotFound):
            client.get_parameter(path="/test/aws/XXX")


class TestPutSecret:
    def test_happy_flow(self):
        client = AwsParameterStoreClient()
        client.put_secret(
            path="/test/aws/parameter/store/client/secret",
            value="yesss!",
            do_overwrite=False,
        )

    def test_do_not_overwrite(self):
        client = AwsParameterStoreClient()
        with pytest.raises(ParameterAlreadyExists):
            client.put_secret(
                path="/test/aws/parameter/store/client/secret",
                value="nooo!",
                do_overwrite=False,
            )

    def test_overwrite(self):
        client = AwsParameterStoreClient()
        client.put_secret(
            path="/test/aws/parameter/store/client/secret",
            value="nooo!",
            do_overwrite=True,
        )


class TestGetSecret:
    def test_happy_flow(self):
        client = AwsParameterStoreClient()
        data = client.get_secret(path="/test/aws/parameter/store/client/secret")
        assert data == "nooo!"

    def test_does_not_exist(self):
        client = AwsParameterStoreClient()
        with pytest.raises(ParameterNotFound):
            client.get_secret(path="/test/aws/XXX")
