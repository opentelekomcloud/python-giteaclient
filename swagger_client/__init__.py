# coding: utf-8

# flake8: noqa

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.19.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.activitypub_api import ActivitypubApi
from swagger_client.api.admin_api import AdminApi
from swagger_client.api.issue_api import IssueApi
from swagger_client.api.miscellaneous_api import MiscellaneousApi
from swagger_client.api.notification_api import NotificationApi
from swagger_client.api.organization_api import OrganizationApi
from swagger_client.api.package_api import PackageApi
from swagger_client.api.repository_api import RepositoryApi
from swagger_client.api.settings_api import SettingsApi
from swagger_client.api.user_api import UserApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.api_error import APIError
from swagger_client.models.access_token import AccessToken
from swagger_client.models.activity_pub import ActivityPub
from swagger_client.models.add_collaborator_option import AddCollaboratorOption
from swagger_client.models.add_time_option import AddTimeOption
from swagger_client.models.annotated_tag import AnnotatedTag
from swagger_client.models.annotated_tag_object import AnnotatedTagObject
from swagger_client.models.attachment import Attachment
from swagger_client.models.branch import Branch
from swagger_client.models.branch_protection import BranchProtection
from swagger_client.models.changed_file import ChangedFile
from swagger_client.models.combined_status import CombinedStatus
from swagger_client.models.comment import Comment
from swagger_client.models.commit import Commit
from swagger_client.models.commit_affected_files import CommitAffectedFiles
from swagger_client.models.commit_date_options import CommitDateOptions
from swagger_client.models.commit_meta import CommitMeta
from swagger_client.models.commit_stats import CommitStats
from swagger_client.models.commit_status import CommitStatus
from swagger_client.models.commit_status_state import CommitStatusState
from swagger_client.models.commit_user import CommitUser
from swagger_client.models.contents_response import ContentsResponse
from swagger_client.models.create_access_token_option import CreateAccessTokenOption
from swagger_client.models.create_branch_protection_option import CreateBranchProtectionOption
from swagger_client.models.create_branch_repo_option import CreateBranchRepoOption
from swagger_client.models.create_email_option import CreateEmailOption
from swagger_client.models.create_file_options import CreateFileOptions
from swagger_client.models.create_fork_option import CreateForkOption
from swagger_client.models.create_gpg_key_option import CreateGPGKeyOption
from swagger_client.models.create_hook_option import CreateHookOption
from swagger_client.models.create_hook_option_config import CreateHookOptionConfig
from swagger_client.models.create_issue_comment_option import CreateIssueCommentOption
from swagger_client.models.create_issue_option import CreateIssueOption
from swagger_client.models.create_key_option import CreateKeyOption
from swagger_client.models.create_label_option import CreateLabelOption
from swagger_client.models.create_milestone_option import CreateMilestoneOption
from swagger_client.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from swagger_client.models.create_org_option import CreateOrgOption
from swagger_client.models.create_pull_request_option import CreatePullRequestOption
from swagger_client.models.create_pull_review_comment import CreatePullReviewComment
from swagger_client.models.create_pull_review_options import CreatePullReviewOptions
from swagger_client.models.create_push_mirror_option import CreatePushMirrorOption
from swagger_client.models.create_release_option import CreateReleaseOption
from swagger_client.models.create_repo_option import CreateRepoOption
from swagger_client.models.create_status_option import CreateStatusOption
from swagger_client.models.create_tag_option import CreateTagOption
from swagger_client.models.create_team_option import CreateTeamOption
from swagger_client.models.create_user_option import CreateUserOption
from swagger_client.models.create_wiki_page_options import CreateWikiPageOptions
from swagger_client.models.cron import Cron
from swagger_client.models.delete_email_option import DeleteEmailOption
from swagger_client.models.delete_file_options import DeleteFileOptions
from swagger_client.models.deploy_key import DeployKey
from swagger_client.models.dismiss_pull_review_options import DismissPullReviewOptions
from swagger_client.models.edit_attachment_options import EditAttachmentOptions
from swagger_client.models.edit_branch_protection_option import EditBranchProtectionOption
from swagger_client.models.edit_deadline_option import EditDeadlineOption
from swagger_client.models.edit_git_hook_option import EditGitHookOption
from swagger_client.models.edit_hook_option import EditHookOption
from swagger_client.models.edit_issue_comment_option import EditIssueCommentOption
from swagger_client.models.edit_issue_option import EditIssueOption
from swagger_client.models.edit_label_option import EditLabelOption
from swagger_client.models.edit_milestone_option import EditMilestoneOption
from swagger_client.models.edit_org_option import EditOrgOption
from swagger_client.models.edit_pull_request_option import EditPullRequestOption
from swagger_client.models.edit_reaction_option import EditReactionOption
from swagger_client.models.edit_release_option import EditReleaseOption
from swagger_client.models.edit_repo_option import EditRepoOption
from swagger_client.models.edit_team_option import EditTeamOption
from swagger_client.models.edit_user_option import EditUserOption
from swagger_client.models.email import Email
from swagger_client.models.external_tracker import ExternalTracker
from swagger_client.models.external_wiki import ExternalWiki
from swagger_client.models.file_commit_response import FileCommitResponse
from swagger_client.models.file_delete_response import FileDeleteResponse
from swagger_client.models.file_links_response import FileLinksResponse
from swagger_client.models.file_response import FileResponse
from swagger_client.models.gpg_key import GPGKey
from swagger_client.models.gpg_key_email import GPGKeyEmail
from swagger_client.models.general_api_settings import GeneralAPISettings
from swagger_client.models.general_attachment_settings import GeneralAttachmentSettings
from swagger_client.models.general_repo_settings import GeneralRepoSettings
from swagger_client.models.general_ui_settings import GeneralUISettings
from swagger_client.models.generate_repo_option import GenerateRepoOption
from swagger_client.models.git_blob_response import GitBlobResponse
from swagger_client.models.git_entry import GitEntry
from swagger_client.models.git_hook import GitHook
from swagger_client.models.git_object import GitObject
from swagger_client.models.git_tree_response import GitTreeResponse
from swagger_client.models.hook import Hook
from swagger_client.models.identity import Identity
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.internal_tracker import InternalTracker
from swagger_client.models.issue import Issue
from swagger_client.models.issue_deadline import IssueDeadline
from swagger_client.models.issue_form_field import IssueFormField
from swagger_client.models.issue_form_field_type import IssueFormFieldType
from swagger_client.models.issue_labels_option import IssueLabelsOption
from swagger_client.models.issue_template import IssueTemplate
from swagger_client.models.issue_template_labels import IssueTemplateLabels
from swagger_client.models.label import Label
from swagger_client.models.markdown_option import MarkdownOption
from swagger_client.models.merge_pull_request_option import MergePullRequestOption
from swagger_client.models.migrate_repo_options import MigrateRepoOptions
from swagger_client.models.milestone import Milestone
from swagger_client.models.node_info import NodeInfo
from swagger_client.models.node_info_services import NodeInfoServices
from swagger_client.models.node_info_software import NodeInfoSoftware
from swagger_client.models.node_info_usage import NodeInfoUsage
from swagger_client.models.node_info_usage_users import NodeInfoUsageUsers
from swagger_client.models.note import Note
from swagger_client.models.notification_count import NotificationCount
from swagger_client.models.notification_subject import NotificationSubject
from swagger_client.models.notification_thread import NotificationThread
from swagger_client.models.notify_subject_type import NotifySubjectType
from swagger_client.models.o_auth2_application import OAuth2Application
from swagger_client.models.organization import Organization
from swagger_client.models.organization_permissions import OrganizationPermissions
from swagger_client.models.pr_branch_info import PRBranchInfo
from swagger_client.models.package import Package
from swagger_client.models.package_file import PackageFile
from swagger_client.models.payload_commit import PayloadCommit
from swagger_client.models.payload_commit_verification import PayloadCommitVerification
from swagger_client.models.payload_user import PayloadUser
from swagger_client.models.permission import Permission
from swagger_client.models.public_key import PublicKey
from swagger_client.models.pull_request import PullRequest
from swagger_client.models.pull_request_meta import PullRequestMeta
from swagger_client.models.pull_review import PullReview
from swagger_client.models.pull_review_comment import PullReviewComment
from swagger_client.models.pull_review_request_options import PullReviewRequestOptions
from swagger_client.models.push_mirror import PushMirror
from swagger_client.models.reaction import Reaction
from swagger_client.models.reference import Reference
from swagger_client.models.release import Release
from swagger_client.models.repo_collaborator_permission import RepoCollaboratorPermission
from swagger_client.models.repo_commit import RepoCommit
from swagger_client.models.repo_topic_options import RepoTopicOptions
from swagger_client.models.repo_transfer import RepoTransfer
from swagger_client.models.repository import Repository
from swagger_client.models.repository_meta import RepositoryMeta
from swagger_client.models.review_state_type import ReviewStateType
from swagger_client.models.search_results import SearchResults
from swagger_client.models.server_version import ServerVersion
from swagger_client.models.state_type import StateType
from swagger_client.models.stop_watch import StopWatch
from swagger_client.models.submit_pull_review_options import SubmitPullReviewOptions
from swagger_client.models.tag import Tag
from swagger_client.models.team import Team
from swagger_client.models.time_stamp import TimeStamp
from swagger_client.models.timeline_comment import TimelineComment
from swagger_client.models.topic_name import TopicName
from swagger_client.models.topic_response import TopicResponse
from swagger_client.models.tracked_time import TrackedTime
from swagger_client.models.transfer_repo_option import TransferRepoOption
from swagger_client.models.update_file_options import UpdateFileOptions
from swagger_client.models.user import User
from swagger_client.models.user_heatmap_data import UserHeatmapData
from swagger_client.models.user_settings import UserSettings
from swagger_client.models.user_settings_options import UserSettingsOptions
from swagger_client.models.watch_info import WatchInfo
from swagger_client.models.wiki_commit import WikiCommit
from swagger_client.models.wiki_commit_list import WikiCommitList
from swagger_client.models.wiki_page import WikiPage
from swagger_client.models.wiki_page_meta_data import WikiPageMetaData
