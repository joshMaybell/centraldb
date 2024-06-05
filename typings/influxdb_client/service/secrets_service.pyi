"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class SecretsService(_BaseService):
    def __init__(self, api_client: Incomplete | None = ...) -> None: ...
    def delete_orgs_id_secrets_id(self, org_id, secret_id, **kwargs): ...
    def delete_orgs_id_secrets_id_with_http_info(self, org_id, secret_id, **kwargs): ...
    async def delete_orgs_id_secrets_id_async(self, org_id, secret_id, **kwargs): ...
    def get_orgs_id_secrets(self, org_id, **kwargs): ...
    def get_orgs_id_secrets_with_http_info(self, org_id, **kwargs): ...
    async def get_orgs_id_secrets_async(self, org_id, **kwargs): ...
    def patch_orgs_id_secrets(self, org_id, request_body, **kwargs): ...
    def patch_orgs_id_secrets_with_http_info(self, org_id, request_body, **kwargs): ...
    async def patch_orgs_id_secrets_async(self, org_id, request_body, **kwargs): ...
    def post_orgs_id_secrets(self, org_id, secret_keys, **kwargs): ...
    def post_orgs_id_secrets_with_http_info(self, org_id, secret_keys, **kwargs): ...
    async def post_orgs_id_secrets_async(self, org_id, secret_keys, **kwargs): ...