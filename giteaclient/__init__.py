# coding: utf-8

# flake8: noqa

"""
    Gitea API.

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.16.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from giteaclient.api.admin_api import AdminApi
from giteaclient.api.issue_api import IssueApi
from giteaclient.api.miscellaneous_api import MiscellaneousApi
from giteaclient.api.notification_api import NotificationApi
from giteaclient.api.organization_api import OrganizationApi
from giteaclient.api.repository_api import RepositoryApi
from giteaclient.api.settings_api import SettingsApi
from giteaclient.api.user_api import UserApi
# import ApiClient
from giteaclient.api_client import ApiClient
from giteaclient.configuration import Configuration
# import models into sdk package
from giteaclient.models.api_error import APIError
from giteaclient.models.access_token import AccessToken
from giteaclient.models.add_collaborator_option import AddCollaboratorOption
from giteaclient.models.add_time_option import AddTimeOption
from giteaclient.models.annotated_tag import AnnotatedTag
from giteaclient.models.annotated_tag_object import AnnotatedTagObject
from giteaclient.models.attachment import Attachment
from giteaclient.models.branch import Branch
from giteaclient.models.branch_protection import BranchProtection
from giteaclient.models.combined_status import CombinedStatus
from giteaclient.models.comment import Comment
from giteaclient.models.commit import Commit
from giteaclient.models.commit_affected_files import CommitAffectedFiles
from giteaclient.models.commit_date_options import CommitDateOptions
from giteaclient.models.commit_meta import CommitMeta
from giteaclient.models.commit_status import CommitStatus
from giteaclient.models.commit_status_state import CommitStatusState
from giteaclient.models.commit_user import CommitUser
from giteaclient.models.contents_response import ContentsResponse
from giteaclient.models.create_access_token_option import CreateAccessTokenOption
from giteaclient.models.create_branch_protection_option import CreateBranchProtectionOption
from giteaclient.models.create_branch_repo_option import CreateBranchRepoOption
from giteaclient.models.create_email_option import CreateEmailOption
from giteaclient.models.create_file_options import CreateFileOptions
from giteaclient.models.create_fork_option import CreateForkOption
from giteaclient.models.create_gpg_key_option import CreateGPGKeyOption
from giteaclient.models.create_hook_option import CreateHookOption
from giteaclient.models.create_hook_option_config import CreateHookOptionConfig
from giteaclient.models.create_issue_comment_option import CreateIssueCommentOption
from giteaclient.models.create_issue_option import CreateIssueOption
from giteaclient.models.create_key_option import CreateKeyOption
from giteaclient.models.create_label_option import CreateLabelOption
from giteaclient.models.create_milestone_option import CreateMilestoneOption
from giteaclient.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from giteaclient.models.create_org_option import CreateOrgOption
from giteaclient.models.create_pull_request_option import CreatePullRequestOption
from giteaclient.models.create_pull_review_comment import CreatePullReviewComment
from giteaclient.models.create_pull_review_options import CreatePullReviewOptions
from giteaclient.models.create_release_option import CreateReleaseOption
from giteaclient.models.create_repo_option import CreateRepoOption
from giteaclient.models.create_status_option import CreateStatusOption
from giteaclient.models.create_tag_option import CreateTagOption
from giteaclient.models.create_team_option import CreateTeamOption
from giteaclient.models.create_user_option import CreateUserOption
from giteaclient.models.create_wiki_page_options import CreateWikiPageOptions
from giteaclient.models.cron import Cron
from giteaclient.models.delete_email_option import DeleteEmailOption
from giteaclient.models.delete_file_options import DeleteFileOptions
from giteaclient.models.deploy_key import DeployKey
from giteaclient.models.dismiss_pull_review_options import DismissPullReviewOptions
from giteaclient.models.edit_attachment_options import EditAttachmentOptions
from giteaclient.models.edit_branch_protection_option import EditBranchProtectionOption
from giteaclient.models.edit_deadline_option import EditDeadlineOption
from giteaclient.models.edit_git_hook_option import EditGitHookOption
from giteaclient.models.edit_hook_option import EditHookOption
from giteaclient.models.edit_issue_comment_option import EditIssueCommentOption
from giteaclient.models.edit_issue_option import EditIssueOption
from giteaclient.models.edit_label_option import EditLabelOption
from giteaclient.models.edit_milestone_option import EditMilestoneOption
from giteaclient.models.edit_org_option import EditOrgOption
from giteaclient.models.edit_pull_request_option import EditPullRequestOption
from giteaclient.models.edit_reaction_option import EditReactionOption
from giteaclient.models.edit_release_option import EditReleaseOption
from giteaclient.models.edit_repo_option import EditRepoOption
from giteaclient.models.edit_team_option import EditTeamOption
from giteaclient.models.edit_user_option import EditUserOption
from giteaclient.models.email import Email
from giteaclient.models.external_tracker import ExternalTracker
from giteaclient.models.external_wiki import ExternalWiki
from giteaclient.models.file_commit_response import FileCommitResponse
from giteaclient.models.file_delete_response import FileDeleteResponse
from giteaclient.models.file_links_response import FileLinksResponse
from giteaclient.models.file_response import FileResponse
from giteaclient.models.gpg_key import GPGKey
from giteaclient.models.gpg_key_email import GPGKeyEmail
from giteaclient.models.general_api_settings import GeneralAPISettings
from giteaclient.models.general_attachment_settings import GeneralAttachmentSettings
from giteaclient.models.general_repo_settings import GeneralRepoSettings
from giteaclient.models.general_ui_settings import GeneralUISettings
from giteaclient.models.generate_repo_option import GenerateRepoOption
from giteaclient.models.git_blob_response import GitBlobResponse
from giteaclient.models.git_entry import GitEntry
from giteaclient.models.git_hook import GitHook
from giteaclient.models.git_object import GitObject
from giteaclient.models.git_service_type import GitServiceType
from giteaclient.models.git_tree_response import GitTreeResponse
from giteaclient.models.hook import Hook
from giteaclient.models.id_assets_body import IdAssetsBody
from giteaclient.models.identity import Identity
from giteaclient.models.inline_response200 import InlineResponse200
from giteaclient.models.inline_response2001 import InlineResponse2001
from giteaclient.models.internal_tracker import InternalTracker
from giteaclient.models.issue import Issue
from giteaclient.models.issue_deadline import IssueDeadline
from giteaclient.models.issue_labels_option import IssueLabelsOption
from giteaclient.models.issue_template import IssueTemplate
from giteaclient.models.label import Label
from giteaclient.models.markdown_option import MarkdownOption
from giteaclient.models.merge_pull_request_option import MergePullRequestOption
from giteaclient.models.migrate_repo_form import MigrateRepoForm
from giteaclient.models.migrate_repo_options import MigrateRepoOptions
from giteaclient.models.milestone import Milestone
from giteaclient.models.node_info import NodeInfo
from giteaclient.models.node_info_services import NodeInfoServices
from giteaclient.models.node_info_software import NodeInfoSoftware
from giteaclient.models.node_info_usage import NodeInfoUsage
from giteaclient.models.node_info_usage_users import NodeInfoUsageUsers
from giteaclient.models.note import Note
from giteaclient.models.notification_count import NotificationCount
from giteaclient.models.notification_subject import NotificationSubject
from giteaclient.models.notification_thread import NotificationThread
from giteaclient.models.notify_subject_type import NotifySubjectType
from giteaclient.models.o_auth2_application import OAuth2Application
from giteaclient.models.organization import Organization
from giteaclient.models.organization_permissions import OrganizationPermissions
from giteaclient.models.pr_branch_info import PRBranchInfo
from giteaclient.models.payload_commit import PayloadCommit
from giteaclient.models.payload_commit_verification import PayloadCommitVerification
from giteaclient.models.payload_user import PayloadUser
from giteaclient.models.permission import Permission
from giteaclient.models.public_key import PublicKey
from giteaclient.models.pull_request import PullRequest
from giteaclient.models.pull_request_meta import PullRequestMeta
from giteaclient.models.pull_review import PullReview
from giteaclient.models.pull_review_comment import PullReviewComment
from giteaclient.models.pull_review_request_options import PullReviewRequestOptions
from giteaclient.models.reaction import Reaction
from giteaclient.models.reference import Reference
from giteaclient.models.release import Release
from giteaclient.models.repo_commit import RepoCommit
from giteaclient.models.repo_topic_options import RepoTopicOptions
from giteaclient.models.repo_transfer import RepoTransfer
from giteaclient.models.repository import Repository
from giteaclient.models.repository_meta import RepositoryMeta
from giteaclient.models.review_state_type import ReviewStateType
from giteaclient.models.search_results import SearchResults
from giteaclient.models.server_version import ServerVersion
from giteaclient.models.state_type import StateType
from giteaclient.models.stop_watch import StopWatch
from giteaclient.models.submit_pull_review_options import SubmitPullReviewOptions
from giteaclient.models.tag import Tag
from giteaclient.models.team import Team
from giteaclient.models.time_stamp import TimeStamp
from giteaclient.models.timeline_comment import TimelineComment
from giteaclient.models.topic_name import TopicName
from giteaclient.models.topic_response import TopicResponse
from giteaclient.models.tracked_time import TrackedTime
from giteaclient.models.transfer_repo_option import TransferRepoOption
from giteaclient.models.update_file_options import UpdateFileOptions
from giteaclient.models.user import User
from giteaclient.models.user_heatmap_data import UserHeatmapData
from giteaclient.models.user_settings import UserSettings
from giteaclient.models.user_settings_options import UserSettingsOptions
from giteaclient.models.watch_info import WatchInfo
from giteaclient.models.wiki_commit import WikiCommit
from giteaclient.models.wiki_commit_list import WikiCommitList
from giteaclient.models.wiki_page import WikiPage
from giteaclient.models.wiki_page_meta_data import WikiPageMetaData
