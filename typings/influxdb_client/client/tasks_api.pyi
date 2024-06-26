"""
This type stub file was generated by pyright.
"""

from datetime import datetime

from influxdb_client import (
    LabelResponse,
    LogEvent,
    Run,
    Task,
    TaskCreateRequest,
    TaskUpdateRequest,
)

class TasksApi:
    def __init__(self, influxdb_client) -> None: ...
    def find_task_by_id(self, task_id) -> Task: ...
    def find_tasks(self, **kwargs): ...
    def create_task(
        self,
        task: Task | None = ...,
        task_create_request: TaskCreateRequest | None = ...,
    ) -> Task: ...
    def create_task_every(self, name, flux, every, organization) -> Task: ...
    def create_task_cron(
        self, name: str, flux: str, cron: str, org_id: str
    ) -> Task: ...
    def delete_task(self, task_id: str): ...
    def update_task(self, task: Task) -> Task: ...
    def update_task_request(
        self, task_id, task_update_request: TaskUpdateRequest
    ) -> Task: ...
    def clone_task(self, task: Task) -> Task: ...
    def get_labels(self, task_id): ...
    def add_label(self, label_id: str, task_id: str) -> LabelResponse: ...
    def delete_label(self, label_id: str, task_id: str): ...
    def get_members(self, task_id: str): ...
    def add_member(self, member_id, task_id): ...
    def delete_member(self, member_id, task_id): ...
    def get_owners(self, task_id): ...
    def add_owner(self, owner_id, task_id): ...
    def delete_owner(self, owner_id, task_id): ...
    def get_runs(self, task_id, **kwargs) -> list[Run]: ...
    def get_run(self, task_id: str, run_id: str) -> Run: ...
    def get_run_logs(self, task_id: str, run_id: str) -> list[LogEvent]: ...
    def run_manually(self, task_id: str, scheduled_for: datetime | None = ...): ...
    def retry_run(self, task_id: str, run_id: str): ...
    def cancel_run(self, task_id: str, run_id: str): ...
    def get_logs(self, task_id: str) -> list[LogEvent]: ...
    def find_tasks_by_user(self, task_user_id): ...
