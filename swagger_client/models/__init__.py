# coding: utf-8

# flake8: noqa
"""
    Nexus Repository Manager REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.29.2-02
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.abstract_api_repository import AbstractApiRepository
from swagger_client.models.anonymous_access_settings_xo import AnonymousAccessSettingsXO
from swagger_client.models.api_certificate import ApiCertificate
from swagger_client.models.api_create_user import ApiCreateUser
from swagger_client.models.api_email_configuration import ApiEmailConfiguration
from swagger_client.models.api_email_validation import ApiEmailValidation
from swagger_client.models.api_license_details_xo import ApiLicenseDetailsXO
from swagger_client.models.api_privilege import ApiPrivilege
from swagger_client.models.api_privilege_application_request import ApiPrivilegeApplicationRequest
from swagger_client.models.api_privilege_repository_admin_request import ApiPrivilegeRepositoryAdminRequest
from swagger_client.models.api_privilege_repository_content_selector_request import ApiPrivilegeRepositoryContentSelectorRequest
from swagger_client.models.api_privilege_repository_view_request import ApiPrivilegeRepositoryViewRequest
from swagger_client.models.api_privilege_script_request import ApiPrivilegeScriptRequest
from swagger_client.models.api_privilege_wildcard_request import ApiPrivilegeWildcardRequest
from swagger_client.models.api_user import ApiUser
from swagger_client.models.api_user_source import ApiUserSource
from swagger_client.models.apt_hosted_api_repository import AptHostedApiRepository
from swagger_client.models.apt_hosted_repositories_attributes import AptHostedRepositoriesAttributes
from swagger_client.models.apt_hosted_repository_api_request import AptHostedRepositoryApiRequest
from swagger_client.models.apt_proxy_api_repository import AptProxyApiRepository
from swagger_client.models.apt_proxy_repositories_attributes import AptProxyRepositoriesAttributes
from swagger_client.models.apt_proxy_repository_api_request import AptProxyRepositoryApiRequest
from swagger_client.models.apt_signing_repositories_attributes import AptSigningRepositoriesAttributes
from swagger_client.models.asset_xo import AssetXO
from swagger_client.models.blob_store_api_soft_quota import BlobStoreApiSoftQuota
from swagger_client.models.blob_store_quota_result_xo import BlobStoreQuotaResultXO
from swagger_client.models.bower_attributes import BowerAttributes
from swagger_client.models.bower_group_repository_api_request import BowerGroupRepositoryApiRequest
from swagger_client.models.bower_hosted_repository_api_request import BowerHostedRepositoryApiRequest
from swagger_client.models.bower_proxy_api_repository import BowerProxyApiRepository
from swagger_client.models.bower_proxy_repository_api_request import BowerProxyRepositoryApiRequest
from swagger_client.models.cleanup_policy_attributes import CleanupPolicyAttributes
from swagger_client.models.cocoapods_proxy_repository_api_request import CocoapodsProxyRepositoryApiRequest
from swagger_client.models.component_xo import ComponentXO
from swagger_client.models.conan_proxy_repository_api_request import ConanProxyRepositoryApiRequest
from swagger_client.models.conda_proxy_repository_api_request import CondaProxyRepositoryApiRequest
from swagger_client.models.content_selector_api_create_request import ContentSelectorApiCreateRequest
from swagger_client.models.content_selector_api_response import ContentSelectorApiResponse
from swagger_client.models.content_selector_api_update_request import ContentSelectorApiUpdateRequest
from swagger_client.models.create_ldap_server_xo import CreateLdapServerXo
from swagger_client.models.docker_attributes import DockerAttributes
from swagger_client.models.docker_group_api_repository import DockerGroupApiRepository
from swagger_client.models.docker_group_repository_api_request import DockerGroupRepositoryApiRequest
from swagger_client.models.docker_hosted_api_repository import DockerHostedApiRepository
from swagger_client.models.docker_hosted_repository_api_request import DockerHostedRepositoryApiRequest
from swagger_client.models.docker_proxy_api_repository import DockerProxyApiRepository
from swagger_client.models.docker_proxy_attributes import DockerProxyAttributes
from swagger_client.models.docker_proxy_repository_api_request import DockerProxyRepositoryApiRequest
from swagger_client.models.file_blob_store_api_create_request import FileBlobStoreApiCreateRequest
from swagger_client.models.file_blob_store_api_model import FileBlobStoreApiModel
from swagger_client.models.file_blob_store_api_update_request import FileBlobStoreApiUpdateRequest
from swagger_client.models.generic_blob_store_api_response import GenericBlobStoreApiResponse
from swagger_client.models.git_lfs_hosted_repository_api_request import GitLfsHostedRepositoryApiRequest
from swagger_client.models.golang_group_repository_api_request import GolangGroupRepositoryApiRequest
from swagger_client.models.golang_proxy_repository_api_request import GolangProxyRepositoryApiRequest
from swagger_client.models.group_attributes import GroupAttributes
from swagger_client.models.group_deploy_attributes import GroupDeployAttributes
from swagger_client.models.helm_hosted_repository_api_request import HelmHostedRepositoryApiRequest
from swagger_client.models.helm_proxy_repository_api_request import HelmProxyRepositoryApiRequest
from swagger_client.models.hosted_storage_attributes import HostedStorageAttributes
from swagger_client.models.http_client_attributes import HttpClientAttributes
from swagger_client.models.http_client_connection_attributes import HttpClientConnectionAttributes
from swagger_client.models.http_client_connection_authentication_attributes import HttpClientConnectionAuthenticationAttributes
from swagger_client.models.input_stream import InputStream
from swagger_client.models.iq_connection_verification_xo import IqConnectionVerificationXo
from swagger_client.models.iq_connection_xo import IqConnectionXo
from swagger_client.models.maven_attributes import MavenAttributes
from swagger_client.models.maven_group_repository_api_request import MavenGroupRepositoryApiRequest
from swagger_client.models.maven_hosted_api_repository import MavenHostedApiRepository
from swagger_client.models.maven_hosted_repository_api_request import MavenHostedRepositoryApiRequest
from swagger_client.models.maven_proxy_api_repository import MavenProxyApiRepository
from swagger_client.models.maven_proxy_repository_api_request import MavenProxyRepositoryApiRequest
from swagger_client.models.negative_cache_attributes import NegativeCacheAttributes
from swagger_client.models.npm_attributes import NpmAttributes
from swagger_client.models.npm_group_repository_api_request import NpmGroupRepositoryApiRequest
from swagger_client.models.npm_hosted_repository_api_request import NpmHostedRepositoryApiRequest
from swagger_client.models.npm_proxy_api_repository import NpmProxyApiRepository
from swagger_client.models.npm_proxy_repository_api_request import NpmProxyRepositoryApiRequest
from swagger_client.models.nuget_attributes import NugetAttributes
from swagger_client.models.nuget_group_repository_api_request import NugetGroupRepositoryApiRequest
from swagger_client.models.nuget_hosted_repository_api_request import NugetHostedRepositoryApiRequest
from swagger_client.models.nuget_proxy_api_repository import NugetProxyApiRepository
from swagger_client.models.nuget_proxy_repository_api_request import NugetProxyRepositoryApiRequest
from swagger_client.models.p2_proxy_repository_api_request import P2ProxyRepositoryApiRequest
from swagger_client.models.page import Page
from swagger_client.models.page_asset_xo import PageAssetXO
from swagger_client.models.page_component_xo import PageComponentXO
from swagger_client.models.page_task_xo import PageTaskXO
from swagger_client.models.proxy_attributes import ProxyAttributes
from swagger_client.models.pypi_group_repository_api_request import PypiGroupRepositoryApiRequest
from swagger_client.models.pypi_hosted_repository_api_request import PypiHostedRepositoryApiRequest
from swagger_client.models.pypi_proxy_repository_api_request import PypiProxyRepositoryApiRequest
from swagger_client.models.r_group_repository_api_request import RGroupRepositoryApiRequest
from swagger_client.models.r_hosted_repository_api_request import RHostedRepositoryApiRequest
from swagger_client.models.r_proxy_repository_api_request import RProxyRepositoryApiRequest
from swagger_client.models.raw_attributes import RawAttributes
from swagger_client.models.raw_group_repository_api_request import RawGroupRepositoryApiRequest
from swagger_client.models.raw_hosted_repository_api_request import RawHostedRepositoryApiRequest
from swagger_client.models.raw_proxy_repository_api_request import RawProxyRepositoryApiRequest
from swagger_client.models.read_ldap_server_xo import ReadLdapServerXo
from swagger_client.models.read_only_state import ReadOnlyState
from swagger_client.models.realm_api_xo import RealmApiXO
from swagger_client.models.repository_xo import RepositoryXO
from swagger_client.models.request import Request
from swagger_client.models.result import Result
from swagger_client.models.role_xo_request import RoleXORequest
from swagger_client.models.role_xo_response import RoleXOResponse
from swagger_client.models.routing_rule_xo import RoutingRuleXO
from swagger_client.models.ruby_gems_group_repository_api_request import RubyGemsGroupRepositoryApiRequest
from swagger_client.models.ruby_gems_hosted_repository_api_request import RubyGemsHostedRepositoryApiRequest
from swagger_client.models.ruby_gems_proxy_repository_api_request import RubyGemsProxyRepositoryApiRequest
from swagger_client.models.s3_blob_store_api_advanced_bucket_connection import S3BlobStoreApiAdvancedBucketConnection
from swagger_client.models.s3_blob_store_api_bucket import S3BlobStoreApiBucket
from swagger_client.models.s3_blob_store_api_bucket_configuration import S3BlobStoreApiBucketConfiguration
from swagger_client.models.s3_blob_store_api_bucket_security import S3BlobStoreApiBucketSecurity
from swagger_client.models.s3_blob_store_api_encryption import S3BlobStoreApiEncryption
from swagger_client.models.s3_blob_store_api_model import S3BlobStoreApiModel
from swagger_client.models.script_result_xo import ScriptResultXO
from swagger_client.models.script_xo import ScriptXO
from swagger_client.models.simple_api_group_deploy_repository import SimpleApiGroupDeployRepository
from swagger_client.models.simple_api_group_repository import SimpleApiGroupRepository
from swagger_client.models.simple_api_hosted_repository import SimpleApiHostedRepository
from swagger_client.models.simple_api_proxy_repository import SimpleApiProxyRepository
from swagger_client.models.stack_trace_element import StackTraceElement
from swagger_client.models.storage_attributes import StorageAttributes
from swagger_client.models.support_zip_xo import SupportZipXO
from swagger_client.models.task_xo import TaskXO
from swagger_client.models.throwable import Throwable
from swagger_client.models.update_ldap_server_xo import UpdateLdapServerXo
from swagger_client.models.upload_definition_xo import UploadDefinitionXO
from swagger_client.models.upload_field_definition_xo import UploadFieldDefinitionXO
from swagger_client.models.yum_attributes import YumAttributes
from swagger_client.models.yum_group_repository_api_request import YumGroupRepositoryApiRequest
from swagger_client.models.yum_hosted_api_repository import YumHostedApiRepository
from swagger_client.models.yum_hosted_repository_api_request import YumHostedRepositoryApiRequest
from swagger_client.models.yum_proxy_repository_api_request import YumProxyRepositoryApiRequest
