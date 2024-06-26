"""
This type stub file was generated by pyright.
"""

from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class OrganizationsService(_BaseService):
    def __init__(self, api_client: Incomplete | None = ...) -> None: ...
    def delete_orgs_id(self, org_id, **kwargs): ...
    def delete_orgs_id_with_http_info(self, org_id, **kwargs): ...
    async def delete_orgs_id_async(self, org_id, **kwargs): ...
    def delete_orgs_id_members_id(self, user_id, org_id, **kwargs): ...
    def delete_orgs_id_members_id_with_http_info(self, user_id, org_id, **kwargs): ...
    async def delete_orgs_id_members_id_async(self, user_id, org_id, **kwargs): ...
    def delete_orgs_id_owners_id(self, user_id, org_id, **kwargs): ...
    def delete_orgs_id_owners_id_with_http_info(self, user_id, org_id, **kwargs): ...
    async def delete_orgs_id_owners_id_async(self, user_id, org_id, **kwargs): ...
    def get_orgs(self, **kwargs): ...
    def get_orgs_with_http_info(self, **kwargs): ...
    async def get_orgs_async(self, **kwargs): ...
    def get_orgs_id(self, org_id, **kwargs): ...
    def get_orgs_id_with_http_info(self, org_id, **kwargs): ...
    async def get_orgs_id_async(self, org_id, **kwargs): ...
    def get_orgs_id_members(self, org_id, **kwargs): ...
    def get_orgs_id_members_with_http_info(self, org_id, **kwargs): ...
    async def get_orgs_id_members_async(self, org_id, **kwargs): ...
    def get_orgs_id_owners(self, org_id, **kwargs): ...
    def get_orgs_id_owners_with_http_info(self, org_id, **kwargs): ...
    async def get_orgs_id_owners_async(self, org_id, **kwargs): ...
    def patch_orgs_id(self, org_id, patch_organization_request, **kwargs): ...
    def patch_orgs_id_with_http_info(
        self, org_id, patch_organization_request, **kwargs
    ): ...
    async def patch_orgs_id_async(
        self, org_id, patch_organization_request, **kwargs
    ): ...
    def post_orgs(self, post_organization_request, **kwargs): ...
    def post_orgs_with_http_info(self, post_organization_request, **kwargs): ...
    async def post_orgs_async(self, post_organization_request, **kwargs): ...
    def post_orgs_id_members(
        self, org_id, add_resource_member_request_body, **kwargs
    ): ...
    def post_orgs_id_members_with_http_info(
        self, org_id, add_resource_member_request_body, **kwargs
    ): ...
    async def post_orgs_id_members_async(
        self, org_id, add_resource_member_request_body, **kwargs
    ): ...
    def post_orgs_id_owners(
        self, org_id, add_resource_member_request_body, **kwargs
    ): ...
    def post_orgs_id_owners_with_http_info(
        self, org_id, add_resource_member_request_body, **kwargs
    ): ...
    async def post_orgs_id_owners_async(
        self, org_id, add_resource_member_request_body, **kwargs
    ): ...
