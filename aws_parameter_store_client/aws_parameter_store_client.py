import boto3


class AwsParameterStoreClient:
    def __init__(self) -> None:
        self.client = boto3.client("ssm")

    def get_parameter(self, path: str) -> str:
        try:
            parameter = self.client.get_parameter(Name=path)
        except self.client.exceptions.ParameterNotFound as exc:
            raise ParameterNotFound(path) from exc
        return parameter["Parameter"]["Value"]

    def get_secret(self, path: str) -> str:
        try:
            parameter = self.client.get_parameter(Name=path, WithDecryption=True)
        except self.client.exceptions.ParameterNotFound as exc:
            raise ParameterNotFound(path) from exc
        return parameter["Parameter"]["Value"]

    def put_parameter(self, path: str, value: str, do_overwrite=False) -> None:
        try:
            self.client.put_parameter(
                Name=path,
                Description="string",
                Value=value,
                Type="String",
                Overwrite=do_overwrite,
            )
        except self.client.exceptions.ParameterAlreadyExists as exc:
            raise ParameterAlreadyExists(path) from exc

    def put_secret(self, path: str, value: str, do_overwrite=False) -> None:
        try:
            self.client.put_parameter(
                Name=path,
                Description="string",
                Value=value,
                Type="SecureString",
                Overwrite=do_overwrite,
            )
        except self.client.exceptions.ParameterAlreadyExists as exc:
            raise ParameterAlreadyExists(path) from exc


class BaseAwsParameterStoreClientException(Exception):
    pass


class ParameterAlreadyExists(BaseAwsParameterStoreClientException):
    def __init__(self, path):
        self.path = path


class ParameterNotFound(BaseAwsParameterStoreClientException):
    def __init__(self, path):
        self.path = path
